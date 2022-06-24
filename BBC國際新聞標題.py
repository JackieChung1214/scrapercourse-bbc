import requests
from bs4 import BeautifulSoup



response=requests.get("https://www.bbc.com/zhongwen/trad/topics/c83plve5vmjt")

soup=BeautifulSoup(response.text,'lxml')
titles=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})

title_list=[]
for title2 in titles:
    title_list.append(title2.getText())

<<<<<<< HEAD
urls=soup.find_all('a',{'class':'bbc-uk8dsi emimjbx0'})
print(urls)
for url in urls:
    print(url.get('href'))
=======
print(title_list)
>>>>>>> 275c2f89b8d902b9b020f8f5d4102a5f0ffcc8fd
