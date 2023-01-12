import os
import sys
import urllib.request
from time import sleep

import pandas as pd
import requests as rq
from bs4 import BeautifulSoup
from selenium import webdriver
from tqdm import tqdm

# reference : https://kimcoder.tistory.com/259
# brew install --cask chromedriver
# sudo mv chromedriver /usr/local/bin


def make_data_dir(keyword):
    save_path = f"./crawled_img/{keyword}"
    os.makedirs(save_path, exist_ok=True)
    return save_path


def set_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("headless")  # 창 띄우지 않고 실행
    options.add_argument("--disable-gpu")  # gpu 사용 x
    # options.add_argument("lang=ko_KR")  # 언어 한글
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
    options.add_argument(f"user-agent={user_agent}")
    return webdriver.Chrome("/opt/homebrew/bin/chromedriver", options=options)


def save_img(save_path, srcset):
    if len(srcset):
        src = str(srcset).split()[2]  # 480 크기 이미지 가져옴 (기본 340)
        filename = src.split("/")[-1]  # 이미지 경로에서 날짜 부분뒤의 순 파일명만 추출
        save_url = os.path.abspath(os.path.join(save_path, filename))  # 저장 경로 결정

        # 파일 저장
        # user-agent 헤더를 가지고 있어야 접근 허용하는 사이트도 있을 수 있음(pixabay가 이에 해당)
        req = urllib.request.Request(src, headers={"User-Agent": "Mozilla/5.0"})
        try:
            img_path = urllib.request.urlopen(req).read()  # 웹 페이지 상의 이미지를 불러옴
            with open(save_url, "wb") as f:  # 디렉토리 오픈
                f.write(img_path)  # 파일 저장
        except urllib.error.HTTPError:
            print("에러")
            sys.exit(0)
    else:
        print(f"No image: {srcset}")
    return save_url


def save_metadata(dfs, keyword):
    result = pd.concat(dfs)
    save_path = make_data_dir("metadata")
    result.reset_index().to_feather(f"{save_path}/{keyword}.feather")


def get_srcset_from_img_html(img):
    if img.get("srcset") is None:
        return img.get("data-lazy-srcset")
    else:
        return img.get("srcset")


def get_img_alt_from_img_html(img):
    if img.get("alt") is None:
        print(f"{img.get('src')} has No alt")
    else:
        return img.get("alt")


def get_imgs_html(browser, keyword, page):
    pixabay_url = f"https://pixabay.com/ko/images/search/{keyword}/?pagi={page}"
    browser.get(pixabay_url)
    sleep(0.1)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    return soup.select("div.row-masonry.search-results img")


def make_feather(keyword: str, img_alt: str, srcset: str, img_path):
    """make feather dataframe from crawled data"""
    return pd.DataFrame(
        [
            {
                "keyword": keyword,
                "img_alt": img_alt,
                "srcset": srcset,
                "img_path": img_path,
            }
        ]
    )


def crawling(keyword: str, pages: int):
    """crawl a keyword from 'pixabay.com'

    Args:
        keyword (str): keyword to crawl
        pages (int): how many pages to crawl
    """

    save_path = make_data_dir(keyword)
    browser = set_browser()

    print("Crawling start!")

    count = 0
    dfs = []
    for page in range(1, pages + 1):
        print(f"Page: {page}")
        imgs = get_imgs_html(browser, keyword, page)

        for img in tqdm(imgs):
            srcset = get_srcset_from_img_html(img)
            img_alt = get_img_alt_from_img_html(img)
            img_path = save_img(save_path, srcset)
            dfs.append(make_feather(keyword, img_alt, srcset, img_path))
            count += 1
    browser.quit()

    save_metadata(dfs, keyword)
    print("Crawling finished!")
    print(f"{count} images are crawled")


if __name__ == "__main__":
    keyword = "soccer"
    pages = 1
    crawling(keyword, pages)
