from bs4 import BeautifulSoup
import urllib.request
 
KOSPI_INFO_URL = 'http://finance.naver.com/sise/sise_market_sum.nhn?&sosok=0&page='
KOSDAQ_INFO_URL = 'http://finance.naver.com/sise/sise_market_sum.nhn?&sosok=1&page='
 
KOSPI_FILE = open('kospi_companies.txt', 'w')
KOSDAQ_FILE = open('kosdaq_companies.txt', 'w')
 

def crawl(url, output):
	for i in range(1, 100):
		sourceCode = urllib.request.urlopen(url + str(i))
		soup = BeautifulSoup(sourceCode, 'lxml', from_encoding='utf-8')
		items = soup.find_all('a', attrs={'class': 'tltle'})

		if not items:
			break

		for item in items:
			output.write(item.get_text() + '\n')
 

def main():
	crawl(KOSPI_INFO_URL, KOSPI_FILE)
	crawl(KOSDAQ_INFO_URL, KOSDAQ_FILE)
	
	KOSPI_FILE.close()
	KOSDAQ_FILE.close()

if __name__ == '__main__':
    main()

