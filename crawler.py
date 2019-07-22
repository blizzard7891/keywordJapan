from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://headlines.yahoo.co.jp/hl?a=20190722-00000110-jij-pol'

class Crawler:
	webdriverFile = '/Users/osujin/Documents/python/keywordJapan/chromedriver'

	def __init__(self):
		driver = webdriver.Chrome(self.webdriverFile)
		driver.implicitly_wait(2)
		self.driver = driver

	def setURL(self, url):
		self.url = url
		self.driver.get(self.url)
		time.sleep(0.5)

	def crawl(self):
		target = self.driver.find_element_by_id('footer')
		self.driver.execute_script("arguments[0].scrollIntoView(true);", target)
		time.sleep(0.5)

		self.switchFrame("#commentTabContents > div > iframe")
		self.clickElement("#loadMoreComments")

		pages = 1
		try:
			while True:
				print("{}-------".format(pages))
				pages += 1

				self.switchFrame('#main > div.mainBox > div.article.comment > div:nth-child(5) > div > iframe')
				html = self.driver.page_source
				soup = BeautifulSoup(html, 'html.parser')
				time.sleep(0.5)
				contents = soup.find_all('span', {'class' : 'cmtBody'})

				self.printElement(contents)
				self.clickElement('#ft > ul > li.next > a')

		except Exception as e:
			print(e)
			pass

	def switchFrame(self, selector):
		commentFrame = self.driver.find_element_by_css_selector(selector)
		self.driver.switch_to.frame(commentFrame)

	def clickElement(self, selector):
		self.driver.find_element_by_css_selector(selector).click()
		time.sleep(1)

	def printElement(self, contents):
		for n in contents:
		   	print(n.text.strip())
		

if __name__ == "__main__":
	crawler = Crawler()
	crawler.setURL(url)
	crawler.crawl()