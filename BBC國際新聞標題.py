import requests
from bs4 import BeautifulSoup



response=requests.get("https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt")

soup=BeautifulSoup(response.text,'lxml')
titles=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})

title_list=[]
for title1 in titles:
    title_list.append(title1.getText())

urls=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})
print(urls)
for url in urls:
    print(url.get('href'))