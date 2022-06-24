import requests
from bs4 import BeautifulSoup

response=requests.get('https://hiking.biji.co/index.php?q=trail&type=%E7%99%BE%E5%A4%A7%E5%BF%85%E8%A8%AA%E6%AD%A5%E9%81%93&page=1')
soup=BeautifulSoup(response.text,'lxml')
titles=soup.find_all('a',{'class':'text-current'})
title_list=[]
for title in titles:
    title_list.append(title.getText())
print(title_list)
