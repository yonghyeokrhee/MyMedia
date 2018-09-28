from urllib.request import urlopen
import bs4

url = "https://news.naver.com/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

print(bs_obj)