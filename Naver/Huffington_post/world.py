from urllib.request import urlopen
import bs4
url1 = "https://www.huffingtonpost.kr/"
url  = "https://www.huffingtonpost.kr/entry/story_kr_5bad9551e4b0425e3c221b71?utm_hp_ref=kr-world"

html = urlopen(url)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")

print(bs_obj)