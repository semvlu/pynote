import urllib.request as request
from bs4 import BeautifulSoup

link= "https://www.ntust.edu.tw/p/403-1000-167-1.php?Lang=zh-tw"
with request.urlopen(link) as response:
    data=response.read().decode("utf-8")
print(data)
soup=BeautifulSoup(data, 'html.parser') #use BeautifulSoup to parse HTML
result= soup.select("div.d-img a img")
for res in result:
    print(res.get("src"))
print(soup.prettify())
