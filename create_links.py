from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import bs4 as bs

driver = webdriver.Chrome("/usr/local/bin/chromedriver")
links = []
names = []

url = "https://www.freeimages.com/"
driver.get(url)


content = driver.page_source
soup = BeautifulSoup(content, features="lxml")
for a in soup.findAll('img'):
	link = a.get('src')
	name = a.get('alt')
	links.append(link)
	names.append(name)
	
df = pd.DataFrame({'Names': names, 'Links':links}) 
df.to_csv('exported_links.csv', index=False, encoding='utf-8')
