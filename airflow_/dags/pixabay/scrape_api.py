import io
import itertools
import logging
import os
import sys

import pandas as pd
import pyarrow as pa
import pyarrow.feather as feather
import requests
from PIL import Image

# request timeout
TIMEOUT = 60

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(levelname)s:%(message)s")
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
print(f"AIRFLOW_HOME: {AIRFLOW_HOME}")
KEYWORD, SITE, SCRAPED_TIME, N_IMGS = sys.argv[1:]
# KEYWORD, SITE, SCRAPED_TIME, N_IMGS = "animal", "pixabay", "01-31_16", 30

# AIRFLOW_HOME = "/opt/ml/final-project-level3-cv-06/airflow_"


class PixabayCrawler:
    def __init__(self, key_words, params):
        self.keywords = key_words
        self.params = params

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
        self.params["per_page"] = MIN_IMG_PER_PAGE
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
                    print(class_path)
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
                imgs_downloaded = 0
                run = True

                for page in itertools.count(1):
                    try:
                        if not run:
                            break

                        self.params["page"] = page
                        j_response = self.get_json().json()

                        for img_dict in j_response["hits"]:
                            try:
                                if imgs_downloaded >= n_imgs:
                                    run = False
                                    break

                                img_path = self.save_img(class_path, img_dict)
                                df = self.add_data2df(df, keyword, img_dict)

                                imgs_downloaded += 1
                                Pbar.set(imgs_downloaded)

                            except Exception as err:
                                logger.warning(err)
                                logger.warning(
                                    f"an error occured proccesing this images {img_dict['largeImageURL']}"
                                )

                    except Exception as err:
                        logger.warning(err)
                        logger.warning(f"an error occured proccesing page {page}")
                        logger.warning(
                            f"downloaded {imgs_downloaded} images from {keyword}"
                        )
                        break
            except Exception as err:
                logger.warning(err)
                logger.warning(f"an error occured proccesing the class {keyword}")
        return df

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
                            "",
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

    def save_img(self, class_path, image):

        img_bytes = self.download_img(image["largeImageURL"])
        img_PIL = Image.open(io.BytesIO(img_bytes))

        img_path = os.path.join(class_path, f"{str(image['id'])}.webp")
        img_PIL.save(img_path, format="WEBP", quality=80)
        return img_path


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


def save_metadata(keyword, df):
    print("make_data_dir os.getcwd(): ", os.getcwd())
    save_path = f"{AIRFLOW_HOME}/dags/data/{keyword[0]}/{SITE}/{SCRAPED_TIME}"

    os.makedirs(save_path, exist_ok=True)
    df["img_path"] = df["img_path"].astype(str)
    # df.to_feather(f"{save_path}/metadata.feather")
    table = pa.Table.from_pandas(df)
    feather.write_feather(table, f"{save_path}/metadata.feather")
    print(f"saved metadata for {keyword[0]} at {save_path}/metadata.feather")


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
        "key": "33032380-426e7c126c233898d98f2cb2b",
        "q": "None",
        "image_type": "photo",
        "page": 1,  # Returned search results are paginated. Use this parameter to select the page number.
        "per_page": MAX_IMG_PER_PAGE,  # Determine the number of results per page. Accepted values: 3 - 200. Default: 20.
        "category": category[0],
        "min_width": 640,
        "min_height": 640,
        "safesearch": "true",
        "order": "latest",
    }

    keyword = [KEYWORD]
    scraper = PixabayCrawler(keyword, params)
    df = scraper.scraper(n_imgs=N_IMGS)
    save_metadata(keyword, df)
    # TODO: 한번 실행할 때 크롤링할 이미지 개수 정하기 n_imgs
    # TODO: 이전에 크롤링했던 사진 이후부터 크롤링
