import requests


from bs4 import BeautifulSoup
# page = page.content.decode("utf-8")  # ..decode("utf-8"): converts bytes to string


page = requests.get('http://www.example.com')
soup = BeautifulSoup(page.content, 'html.parser')

print(soup.find('h1').string)
print(soup.select_one('div p a').attrs['href'])

