from bs4 import BeautifulSoup
from selenium import webdriver


TARGET_URL = 'https://kr.investing.com/stock-screener/?sp=country::11|sector::a|industry::a|equityType::a|exchange::a<eq_market_cap;'
 
OUTPUT_FILE = open('korea_company_info.txt', 'w')
 
def crawl(url, output):
		driver = webdriver.PhantomJS()
		driver.get(url)

		html = driver.execute_script("return document.documentElement.innerHTML;")
		soup = BeautifulSoup(html, "lxml").find("table", {"id" : "resultsTable"}).find("tbody")
		rows = soup.find_all("tr")

		for row in rows:
			cols = row.find_all("td")
			linkInfo = cols[1].find("a")

			name = linkInfo.get("title")
			link = linkInfo.get("href") 
			code = cols[2].get_text()

			print(name)
			output.write(name + ' ')
			output.write(code + ' ')
			output.write(link + '\n')


def main():
	for i in range(1, 21):
		print("page %d crawl start" % i)
		crawl(TARGET_URL + str(i), OUTPUT_FILE)
	
	OUTPUT_FILE.close()

if __name__ == '__main__':
    main()

