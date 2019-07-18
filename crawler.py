from selenium import webdriver
from bs4 import BeautifulSoup
import time

url = 'https://headlines.yahoo.co.jp/cm/main?d=20190718-00000113-asahi-soci'

driver = webdriver.Chrome('/Users/osujin/Documents/python/chromedriver')
driver.implicitly_wait(5)

driver.get(url)
target = driver.find_element_by_id('footer')
print(target.text)
driver.execute_script("arguments[0].scrollIntoView(true);", target)
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
notices = soup.find_all('span', {'class' : 'cmtBody'})

for n in notices:
    print(n.text.strip())
    print()