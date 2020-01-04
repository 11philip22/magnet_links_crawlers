from time import sleep
from re import compile
from bs4 import BeautifulSoup
from requests import get


def get_magnets(soup):
    try:
        for link in soup.findAll('a', attrs={'href': compile("^magnet")}):
            return link['href']
    except Exception:
        return


def get_soup(html):
    if html is not None:
        soup = BeautifulSoup(html, 'lxml')
        return soup
    else:
        return


def get_list():
    print("Enter/Paste your links")
    contents = []
    try:
        while True:
            line = input()
            if line:
                contents.append(line)	
            else:
                break
        return contents
    except Exception:
        print("Enter/Paste urls")
        exit(1)


for url in get_list():
    print(get_magnets(get_soup(get(url).content)))
    sleep(0.5)