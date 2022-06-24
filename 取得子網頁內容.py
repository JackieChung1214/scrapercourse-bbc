import requests
from bs4 import BeautifulSoup



response=requests.get("https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt")

soup=BeautifulSoup(response.text,'lxml')
titles=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})

title_list=[]
for title1 in titles:
    title_list.append(title1.getText())

urls=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})
tag_list=[]
for url in urls:
    sub_response=requests.get(url.get('href'))
    sub_soup=BeautifulSoup(sub_response.text,'lxml')
    tags=sub_soup.find_all('li',{'class':'bbc-1msyfg1 eqijop70'})
    for tag in tags:
        tag_list.append(tag.find('a').getText())

print(tag_list)