import time
from inspect import getfile
import os
import re
from urllib import request
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

site_url = 'https://fow.kr'
url = "https://fow.kr/find/"


def main():
    get_player_list()


def aaaa(name):
    res = requests.get(url + name)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    tag_A_s = soup.find_all('a', attrs={"class": "sbtn green small"})  # 전체 영역에서 'a' 태그를 찾지 않고 인기 급상승 영역으로 범위 제한
    for i in tag_A_s:
        href = i.attrs['href']

        temp = href.split('&')[2]
        ID = temp.split('=')[1]

        os.chdir('C:/Users/gpark/PycharmProjects/flaskProject/project/save2')
        request.urlretrieve(site_url + href, 'fow_' + ID + '.bat')
        print(f"{ID} Done")
        time.sleep(2)
    print(f"{name} Done")
    time.sleep(4)


def get_player_list():
    driver = webdriver.Chrome('./chromedriver')
    driver.implicitly_wait(1)
    driver.get('https://fow.kr/ranking#51')
    driver.implicitly_wait(1)
    table = driver.find_element_by_class_name('tablesorter.rank_ranking')
    tbody = table.find_element_by_tag_name("tbody")
    rows = tbody.find_elements_by_tag_name("tr")
    for index, value in enumerate(rows):
        body = value.find_elements_by_tag_name("td")[1]
        a = body.find_element_by_tag_name("a").get_attribute('href')
        name = a.split('/')[4]
        aaaa(name)


main()