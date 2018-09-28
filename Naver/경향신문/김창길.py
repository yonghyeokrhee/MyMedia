from urllib.request import urlopen
import bs4
url = "http://news.khan.co.kr/"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")


print(html.read())