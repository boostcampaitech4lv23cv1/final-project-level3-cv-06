import datetime
import io
import os
import sys
import urllib.request
from time import sleep

import pandas as pd
import yaml
from bs4 import BeautifulSoup
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from tqdm import tqdm
from webdriver_manager.chrome import ChromeDriverManager

os.environ["no_proxy"] = "*"
AIRFLOW_HOME = os.environ.get("AIRFLOW_HOME")
# This is for Negsignal.SIGSEGV error


# reference : https://kimcoder.tistory.com/259
# brew install --cask chromedriver
# sudo mv chromedriver /usr/local/bin
class PixabayCrawler:
    def __init__(self, keyword, pages):
        self.keyword = keyword
        self.pages = pages

    def make_data_dir(self, keyword):
        print("make_data_dir os.getcwd(): ", os.getcwd())
        save_path = f"{AIRFLOW_HOME}/dags/crawled_img/pixabay/{keyword}"
        os.makedirs(save_path, exist_ok=True)
        return save_path

    def set_browser(self):
        options = webdriver.ChromeOptions()
        options.add_argument("headless")  # 창 띄우지 않고 실행
        options.add_argument("--disable-gpu")  # gpu 사용 x
        # options.add_argument("lang=ko_KR")  # 언어 한글
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
        options.add_argument(f"user-agent={user_agent}")
        browser = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()), options=options
        )
        print("Finish set_browser")
        return browser

    def save_img(self, save_path, srcset):
        if len(srcset):
            src = str(srcset).split()[2]  # 480 크기 이미지 가져옴 (기본 340)
            filename = src.split("/")[-1]  # 이미지 경로에서 날짜 부분뒤의 순 파일명만 추출
            save_url = os.path.abspath(os.path.join(save_path, filename))  # 저장 경로 결정

            # 파일 저장
            # user-agent 헤더를 가지고 있어야 접근 허용하는 사이트도 있을 수 있음(pixabay가 이에 해당)
            req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
            try:
                img_byte = urllib.request.urlopen(req).read()  # 웹 페이지 상의 이미지를 불러옴
                with open(save_url, "wb") as f:  # 디렉토리 오픈
                    f.write(img_byte)  # 파일 저장
                img = Image.open(io.BytesIO(img_byte))
                return save_url, img.size
            except urllib.error.HTTPError:
                print("에러")
                sys.exit(0)
        else:
            print(f"No image: {srcset}")

        return save_url

    def save_metadata(self, dfs, keyword):
        concat_df = pd.concat(dfs).reset_index(drop=True)
        save_path = self.make_data_dir("metadata")
        concat_df.to_feather(f"{save_path}/{keyword}.feather")

    def get_srcset_from_img_html(self, img):
        if img.get("srcset") is None:
            return img.get("data-lazy-srcset")
        else:
            return img.get("srcset")

    def get_img_alt_from_img_html(self, img):
        if img.get("alt") is None:
            print(f"{img.get('src')} has No alt")
        else:
            return img.get("alt")

    def get_imgs_html(self, browser, keyword, page):
        pixabay_url = f"https://pixabay.com/ko/images/search/{keyword}/?pagi={page}"
        browser.get(pixabay_url)
        sleep(0.1)
        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
        return soup.select("div.row-masonry.search-results img")

    def make_feather(
        self, keyword: str, img_alt: str, srcset: str, img_path: str, img_size: tuple
    ):
        """make feather dataframe from crawled data"""
        return pd.DataFrame(
            [
                {
                    "category": keyword,
                    "alt": img_alt,
                    "srcset": srcset,
                    "img_path": img_path,
                    "img_width": img_size[0],
                    "img_height": img_size[1],
                    "label": None,
                    "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            ]
        )

    def crawling(self):
        """crawl a keyword from 'pixabay.com'

        Args:
            keyword (str): keyword to crawl
            pages (int): how many pages to crawl
        """

        save_path = self.make_data_dir(self.keyword)
        browser = self.set_browser()

        print(f"{self.keyword} crawling start!")

        count = 0
        dfs = []
        for page in range(1, self.pages + 1):
            print(f"Page: {page}")
            imgs = self.get_imgs_html(browser, self.keyword, page)

            for img in tqdm(imgs):
                srcset = self.get_srcset_from_img_html(img)
                img_alt = self.get_img_alt_from_img_html(img)
                img_path, img_size = self.save_img(save_path, srcset)
                dfs.append(
                    self.make_feather(self.keyword, img_alt, srcset, img_path, img_size)
                )
                count += 1
        browser.quit()

        self.save_metadata(dfs, self.keyword)
        print("Crawling finished!")
        print(f"{count} {self.keyword} images are crawled in {self.pages} pages")


def crawl_img_by_keyword():
    print("os.getcwd(): ", os.getcwd())
    with open(f"{AIRFLOW_HOME}/dags/pixabay/keyword.yml", "r") as f:
        words_pages = yaml.load(f, Loader=yaml.FullLoader)
        print("read keywords.yml")
        for words_pages in words_pages:
            print("word: ", words_pages["word"])
            crawler = PixabayCrawler(
                keyword=words_pages["word"], pages=words_pages["pages"]
            )
            print("init crawler")
            crawler.crawling()
            print("crawling finished!")


def crawl_img_by_category():
    print("os.getcwd(): ", os.getcwd())
    with open(f"{AIRFLOW_HOME}/dags/pixabay/category.yml", "r") as f:
        words_pages = yaml.load(f, Loader=yaml.FullLoader)
        print("read category.yml")
        for words_pages in words_pages:
            print("word: ", words_pages["word"])
            crawler = PixabayCrawler(
                keyword=words_pages["word"], pages=words_pages["pages"]
            )
            print("init crawler")
            crawler.crawling()
            print("crawling finished!")


if __name__ == "__main__":

    # crawl_img_by_keyword()
    crawl_img_by_category()
