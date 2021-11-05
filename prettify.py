from bs4 import BeautifulSoup
import sys
soup = BeautifulSoup(open('public/Researches/index.html'),'lxml')
print (soup.prettify())