# coding:UTF-8
from bs4 import BeautifulSoup
import sys

all_time_line = ""
soup = BeautifulSoup(open('public/'+str(sys.argv[1])+'/index.html'),'lxml')
all_card_content = soup.find_all(name='div',attrs={"class":"card-content"})
for card_content in all_card_content:
    soup_card_content = BeautifulSoup(str(card_content),'lxml')
    has_time_line = str(soup_card_content.find(name='div',attrs={"class":"timeline"}))!='None'
    if (has_time_line):
        all_time_line += str(card_content)

all_time_line = all_time_line.replace("h3 class=\"tag is-primary\"", "h3 class=\"\"")
all_time_line = all_time_line.replace("<a href=\"./", "<a href=\"./"+str(sys.argv[1])+"/")
all_time_line = all_time_line.replace("h3", "h5")


all_time_line = all_time_line.replace("card-content", "")

def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()

    return read_all

# 写内容到文件
def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()

def replace(file, old_content, new_content):
    content = read_file(file)
    content = content.replace(old_content, new_content)
    rewrite_file(file, content)

replace(r'public/index.html', "<p>Timeline"+str(sys.argv[1])+"</p>", all_time_line)



# print(soup.find('a'))

# print(soup.p.string)

# print(soup.title.string)
