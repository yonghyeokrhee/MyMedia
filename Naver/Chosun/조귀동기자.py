from urllib.request import urlopen
import bs4
url = "http://search.chosun.com/search/news.search?cont5=%EC%84%B8%EC%A2%85%3D%EC%A1%B0%EA%B7%80%EB%8F%99+%EA%B8%B0%EC%9E%90"
html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
div = bs_obj.find("div", {"class":"search_news_box"})

print(div)