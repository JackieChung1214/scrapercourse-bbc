import requests
from bs4 import BeautifulSoup


response=requests.get("https://www.bbc.com/zhongwen/trad/topics/cq8nqywy37yt")

soup=BeautifulSoup(response.text,'lxml')
titles=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})

title_list=[]
for title in titles:
    title_list.append(title.getText())

print(title_list)