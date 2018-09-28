
from urllib.request import urlopen
import bs4
url = "http://jmagazine.joins.com/economist/view/320905"
url_click_thru = "http://jmagazine.joins.com/economist/view/322926"
#html = urlopen(url)
html = urlopen(url_click_thru)

bs_obj = bs4.BeautifulSoup(html.read(), "html.parser")
div = bs_obj.find("div", {"class": "tit_area"})

print(div)