from bs4 import BeautifulSoup
import requests

url = 'https://www.weather.gov'
 
req = requests.get(url)
print(req.status_code)

if req.status_code != 200:
    print('something went wrong')
    exit()

html_file = req.text
soup = BeautifulSoup(html_file ,'lxml')
match = soup.title.text
match = soup.find('div', class_='one-third-last')
print(match)