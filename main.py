import urllib
import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

page = urllib.request.urlopen("https://novosibirsk.hh.ru/catalog/informacionnye-tehnologii-internet-telekom/programmirovanie-razrabotka").read()
soup = BeautifulSoup (page,'html.parser')

list = []

for link in soup.find_all('a', class_="bloko-link"):

    url = link.get('href')

    if '/vacancy/' in url:
        list.append(url)


skills = []

for l in list:
    page_vacancy = urllib.request.urlopen(l)
    s = BeautifulSoup (page_vacancy, 'html.parser')

    for link in s.find_all('span', class_="bloko-tag__section bloko-tag__section_text"):

        link = str(link)
        page_skills = ' '.join(re.findall(r'>([^<>]+)<', link))
        skills.append(page_skills)
        print(page_skills)
cnt = Counter(skills).most_common(20)
# print(dict(cnt))
# print(skills)


import matplotlib.pyplot as plt

x = dict(cnt).values()
labels = (dict(cnt))

fig, ax = plt.subplots()
ax.pie(x, labels=labels,
       autopct='%.0f%%',
       shadow=True,
       startangle=180)

ax.set_title('20 самых востребованных навыков \nв области программирования и разработки \nв Новосибирске')
plt.show()