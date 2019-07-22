from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://headlines.yahoo.co.jp/cm/videomain?d=20190719-00000055-ann-soci'
webdriverFile = '/Users/osujin/Documents/python/keywordJapan/chromedriver'

driver = webdriver.Chrome(webdriverFile)
driver.implicitly_wait(2)
driver.get(url)
time.sleep(1)

#target = driver.find_element_by_id('contentsBody')
#driver.execute_script("arguments[0].scrollIntoView(true);", target)


pages = 1
try:
	while True:
		print("{}-------".format(pages))
		pages += 1

		commentFrame = driver.find_element_by_css_selector('#main > div.mainBox > div.article.comment > div:nth-child(5) > div > iframe')
		driver.switch_to.frame(commentFrame)
		time.sleep(1)
		html = driver.page_source
		soup = BeautifulSoup(html, 'html.parser')
		time.sleep(1)
		notices = soup.find_all('span', {'class' : 'cmtBody'})
		for n in notices:
   			print(n.text.strip())

		nextBtn = driver.find_element_by_css_selector('#ft > ul > li.next > a')
		nextBtn.click()
		time.sleep(2)

except Exception as e:
	pass


