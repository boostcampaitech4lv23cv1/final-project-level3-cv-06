import io
import itertools
import logging
import os
import sys

import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import requests
import yaml

# from webp import WebP
from google.cloud import storage
from PIL import Image

# request timeout
TIMEOUT = 60

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
print(f"AIRFLOW_HOME: {AIRFLOW_HOME}")
KEYWORD, SITE, SCRAPED_TIME, N_IMGS = sys.argv[1:]
N_IMGS = int(N_IMGS)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{AIRFLOW_HOME}/m2-key.json"

with open(f"{AIRFLOW_HOME}/secret.yml", "r") as f:
    secret = yaml.load(f, Loader=yaml.FullLoader)


class PixabayCrawler:
    def __init__(self, key_words, params, bucket):
        self.keywords = key_words
        self.params = params
        self.bucket = bucket

    def get_json(self):
        try:
            url = f"https://pixabay.com/api/?key={self.params['key']}"
            for k, v in self.params.items():
                if k != "key":
                    url += f"&{k}={v}"
            r = requests.get(url, allow_redirects=False, timeout=TIMEOUT)
            logging.debug(f"json url - {r.url}")
        except requests.exceptions.Timeout as err:
            logger.warning(err)

        try:
            return r
        except Exception as err:
            logger.warning(err)

    def download_img(self, url):
        try:
            r = requests.get(url, allow_redirects=False, timeout=TIMEOUT)
            logging.debug(f"image url - {r.url}")
        except requests.exceptions.Timeout as err:
            logger.warning(err)

        try:
            return r.content
        except Exception as err:
            logger.warning(err)

    def get_available_images(self):
        self.params["page"] = 1
        # self.params["per_page"] = MIN_IMG_PER_PAGE
        j_response = self.get_json().json()
        return j_response["total"]

    def scraper(self, n_imgs=1):
        logger.debug((self, self.keywords, n_imgs))
        # go to https://pixabay.com/api/docs/ to look up these values

        # path = Path(path)
        df = pd.DataFrame(
            columns=[
                "tag",
                "img_path",
                "img_width",
                "img_height",
                "crawled_time",
                "label",
            ]
        )
        logger.info("Starting")
        for keyword in self.keywords:
            try:
                self.params["q"] = keyword

                try:
                    class_path = (
                        f"{AIRFLOW_HOME}/dags/data/{keyword}/{SITE}/{SCRAPED_TIME}"
                    )
                    os.makedirs(class_path, exist_ok=True)

                except Exception:
                    logger.warning(
                        f"Something went wrong while creating path for {keyword}"
                    )

                logger.info(f"Downloading class: {keyword} to {class_path}")

                # testing if pixabay can serve the amount of wanted images
                n_imgs = self.test_if_pixabay_can_serve(n_imgs)

                Pbar = Progressbar(n_imgs)

                # creating the params list for all pages
                imgs_progress = 0
                n_imgs2gcs = 0

                run = True

                for page in itertools.count(1):
                    try:
                        if not run:
                            break

                        self.params["page"] = page
                        j_response = self.get_json().json()

                        for img_dict in j_response["hits"]:
                            try:
                                if imgs_progress >= n_imgs:
                                    run = False
                                    break
                                if self.is_valid(img_dict["id"]):
                                    self.send_img2gcs(img_dict)
                                    df = self.add_data2df(df, keyword, img_dict)
                                    n_imgs2gcs += 1

                                imgs_progress += 1
                                Pbar.set(imgs_progress)

                            except Exception as err:
                                logger.warning(err)
                                logger.warning(
                                    f"an error occured proccesing this images {img_dict['largeImageURL']}"
                                )

                    except Exception as err:
                        logger.warning(err)
                        logger.warning(f"an error occured proccesing page {page}")
                        logger.warning(
                            f"downloaded {imgs_progress} images from {keyword}"
                        )
                        break
            except Exception as err:
                logger.warning(err)
                logger.warning(f"an error occured proccesing the class {keyword}")
        return df, n_imgs2gcs

    def add_data2df(self, df, keyword, img_dict):

        df = pd.concat(
            [
                pd.DataFrame(
                    [
                        [
                            img_dict["tags"],
                            f"{keyword}/{SITE}/{SCRAPED_TIME}/{img_dict['id']}.webp",
                            img_dict["webformatWidth"],
                            img_dict["webformatHeight"],
                            SCRAPED_TIME,
                            "NaN",
                        ]
                    ],
                    columns=df.columns,
                ),
                df,
            ],
            ignore_index=True,
        )

        return df

    def test_if_pixabay_can_serve(self, n_imgs: int) -> int:
        """test if pixabay can serve the amount of wanted images

        Args:
            n_imgs (int): the amount of wanted images

        Returns:
            int: the amount of wanted images
        """
        available_imgs = self.get_available_images()
        print(f"There are {available_imgs} available images...")
        if available_imgs < n_imgs:
            logger.info(
                f"There are only {available_imgs} available images... starting download"
            )
            n_imgs = available_imgs - 1
        return n_imgs

    def is_valid(self, img_id: int) -> bool:
        """check img_id is a duplicate

        Args:
            img_id (str): img id of pixabay

        Returns:
            bool: True if not duplicate
        """
        url = f"{secret['api_url']}/api/v1/meta/duplicate_check"
        data = {"id": str(img_id), "category": keyword[0]}

        try:
            res = requests.post(url, json=data)
            res.raise_for_status()
            return res.json()["valid"]
        except Exception as err:
            logger.warning(err)
            logger.warning("an error occured requesting duplicate check")

    def send_img2gcs(self, img_dict):
        file_name = f"{KEYWORD}/{SITE}/{SCRAPED_TIME}/{str(img_dict['id'])}.webp"
        img_bytes = self.download_img(img_dict["webformatURL"])
        img_PIL = Image.open(io.BytesIO(img_bytes))
        webp_io = io.BytesIO()
        img_PIL.save(webp_io, format="WEBP", quality=80)
        try:
            blob = self.bucket.blob(file_name)
            blob.upload_from_string(webp_io.getvalue(), content_type="image/webp")
        except Exception as err:
            logger.warning(err)
            logger.warning(
                f"an error occured saving this images {img_dict['largeImageURL']}"
            )

    def resize_keep_aspect_ratio(self, img, size: int = 640):
        """resize image while keeping aspect ratio

        Args:
            img (PIL image): image to resize
            size (int): (resize size)

        Returns:
            PIL image: resized image
        """
        original_w, original_h = img.size
        if original_w >= 640 or original_h >= 640:
            if original_w > original_h:
                img = img.resize(
                    (size, int(size / original_w * original_h)), resample=Image.NEAREST
                )
            else:
                img = img.resize(
                    (int(size / original_h * original_w), size), resample=Image.NEAREST
                )
        return img, img.size


class Progressbar:
    def __init__(self, to_value, name="", prefix="Progress:", suffix="Complete"):
        self.to_value = to_value
        self.is_value = 0
        self.name = name
        self.prefix = prefix
        self.suffix = suffix
        self.form = "\r{prefix} [{bar}] {is_value}/{to_value} {name} {suffix} "
        self.print_bar()

    def print_bar(self):
        BAR_SIZE = 30
        test_value = lambda isv: 1 if (isv > 0) else 0
        equal = round(BAR_SIZE * self.is_value / self.to_value) - 1
        under = BAR_SIZE - equal

        if self.is_value == 0:
            equal = 0
            under = BAR_SIZE
        if self.is_value == self.to_value:
            under = 0
            equal = BAR_SIZE

        bar = (
            "=" * equal + ">" * test_value(self.is_value / self.to_value) + "_" * under
        )

        print(
            self.form.format(
                bar=bar,
                prefix=self.prefix,
                name=self.name,
                suffix=self.suffix,
                is_value=self.is_value,
                to_value=self.to_value,
            ),
            end="\r",
        )
        if self.is_value == self.to_value:
            print()

    def add(self, value):
        self.is_value += value
        self.print_bar()

    def set(self, value):
        self.is_value = value
        self.print_bar()


def send_metadata2api(df):
    url = f"{secret['api_url']}/api/v1/meta/create"

    buffer = pa.BufferOutputStream()
    feather.write_feather(df, buffer)

    file = {"file": buffer.getvalue().to_pybytes()}
    category = {"category": KEYWORD}

    try:
        res = requests.post(url, files=file, data=category)
    except Exception as err:
        logger.warning(err)
        logger.warning("an error occured sending feather file to api")

    # Check the status code of the response
    if res.status_code == 200:
        print("metadata sent successfully")
    else:
        print("Failed to send data")


if __name__ == "__main__":
    category = [
        "animals",
        "backgrounds",
        "fashion",
        "nature",
        "science",
        "education",
        "feelings",
        "health",
        "people",
        "religion",
        "places",
        "industry",
        "computer",
        "food",
        "sports",
        "transportation",
        "travel",
        "buildings",
        "business",
        "music",
    ]

    MAX_IMG_PER_PAGE = 200
    MIN_IMG_PER_PAGE = 3

    params = {
        "key": secret["pixabay_api"],
        "q": "None",
        "image_type": "photo",
        "page": 1,  # Returned search results are paginated. Use this parameter to select the page number.
        "per_page": MAX_IMG_PER_PAGE,  # Determine the number of results per page. Accepted values: 3 - 200. Default: 20.
        "category": "None",
        "safesearch": "true",
        "order": "popular",
    }

    storage_client = storage.Client()
    bucket_name = "scraped-img"
    bucket = storage_client.bucket(bucket_name)

    if KEYWORD == "animal":
        keyword = [KEYWORD, "mammal"]
        #     '금붕어', '상어', '가오리', '닭', '타조', '까치', '독수리', '올빼미', '개구리', '거북이',
        #    '도마뱀', '카멜레온', '악어', '뱀', '전갈', '거미', '공작', '앵무새', '오리', '거위',
        #    '백조', '코끼리', '오리너구리', '캥거루', '코알라', '해파리', '말미잘', '달팽이', '게', '홍학',
        #    '펠리컨', '펭귄', '고래', '범고래', '바다사자', '개', '늑대', '하이에나', '여우', '고양이',
        #    '퓨마', '표범', '재규어', '사자', '호랑이', '치타', '곰', '미어캣', '무당벌레', '벌',
        #    '개미', '메뚜기', '사마귀', '잠자리', '나비', '불가사리', '성게', '해삼', '토끼', '햄스터',
        #    '호저', '다람쥐', '비버', '기니피그', '얼룩말', '돼지', '멧돼지', '하마', '소', '양',
        #    '낙타', '족제비', '수달', '스컹크', '오소리', '아르마딜로', '나무늘보', '오랑우탄', '고릴라',
        #    '침팬지', '원숭이', '레서판다', '판다', '복어'
        params["category"] = category[0]
    elif KEYWORD == "landmark":
        keyword = [KEYWORD, "places"]
        params["category"] = category[10]
    scraper = PixabayCrawler(keyword, params, bucket)
    df, n_imgs2gcs = scraper.scraper(n_imgs=N_IMGS)
    print(f"Number of img2gcs is {n_imgs2gcs}")
    send_metadata2api(df)
    # TODO: 이전에 크롤링했던 사진 이후부터 크롤링
    # TODO: pixabay에서 url전부 뽑고 url리스트를 api에 전달해서 한번에 중복체크, 그 후 멀티프로세싱이나 비동기로 이미지 다운
