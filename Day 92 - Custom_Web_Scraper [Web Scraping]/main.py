import os
import requests
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()

GOOGLE_FORM_URL = os.getenv('GOOGLE_FORM_URL')
SURVEY_URL = os.getenv('STACKOVERFLOW_SURVEY')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ka;q=0.7,ru;q=0.6"
}

response = requests.get(SURVEY_URL, headers=header)
data = response.text

soup = BeautifulSoup(data, "html.parser")

languages_txt = soup.select("#languageepiif .lh-sm")
languages = [lang.get_text() for lang in languages_txt]

ratings_txt = soup.select("#languageepiif .bar ")
ratings = [rate.get("data-percentage") for rate in ratings_txt]
        
for idx in range(len(languages)):
    driver.get(GOOGLE_FORM_URL)
    sleep(2)
    language = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rating = driver.find_element("xpath",
        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element("xpath", '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    language.send_keys(languages[idx])
    rating.send_keys(ratings[idx])
    submit.click()