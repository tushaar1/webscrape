from urllib.request import urlopen  as uReq
from bs4 import BeautifulSoup as soup



my_url = input()
uClient = uReq(my_url)  # open up a connection and grabs the webpage
page_html = uClient.read()  # puts the content into a variable
uClient.close()  # closes the file

page_soup = soup(page_html, 'html.parser')  # parses the html into a new variable
test = page_soup.find_all('div', {'class': 'mw-category'})
product_name = test[0].text
# prints 'A' or the first letter of the table every time, need to fix this
# so this works for everylist


# my_url = 'https://en.wikipedia.org/wiki/Category:Art_museums_in_Florida'  # this just looks at florida [works]
# my_url = 'https://en.wikipedia.org/wiki/Category:Art_museums_in_Missouri'  # test to see if it works for lists
# my_url = 'https://en.wikipedia.org/wiki/Category:Art_museums_in_the_United_States_by_state'  # whole u.s [works]
# testing regular categories, they work but ones with sub categories are harder

# museums2 = page_soup.find_all('div', {"class": "mw-category-generated"})  # finds all the classes w/ the "category"
# museums_list = museums2[0].text  # gets the first one

# [keep these just in case]
# title = page_soup.find_all('a', {"title": ""})
# title_container = container.find_all('a', {'class': 'item-title'})
# product_name = title_container[0].text
# print(museums2)
# print(museums_list)
# test = page_soup.find_all('div', {'class': 'mw-content-ltr'})
