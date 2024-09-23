import requests
from bs4 import BeautifulSoup
import pandas as pd


def web_scrape(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return
    soup = BeautifulSoup(response.content,'lxml')
    titles = soup.find_all('h2')

    headlines = soup.find_all('h2')
    for headline in headlines:
        print(headline.txt)