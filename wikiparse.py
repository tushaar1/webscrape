from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup



my_url = input()
uClient = uReq(my_url)  # open up a connection and grabs the webpage
page_html = uClient.read()  # puts the content into a variable
uClient.close()  # closes the file

page_soup = soup(page_html, 'html.parser')  # parses the html into a new variable
test = page_soup.find_all('div', {'class': 'mw-category'})
product_name = test[0].text
