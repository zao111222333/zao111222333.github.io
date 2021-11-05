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

# <p>Timeline"+str(sys.argv[1])+"</p>
def correct_file(file, type):

    replace(file, "<a class=\"navbar-item is-active\" href=\"/Archive\">", "<a class=\"navbar-item\" href=\"/Archive\">")
    replace(file, "<a class=\"navbar-item\" href=\"/"+type+"\">", "<a class=\"navbar-item is-active\" href=\"/"+type+"\">")
    replace(file, "<title>Category: ", "<title>"+type+"-")

import os

def list_all_files(rootdir):
    _files = []
    l1 = os.listdir(rootdir)# 列出文件夹下的所有目录和文件
    for i in range(0,len(l1)):
        path = os.path.join(rootdir, l1[i])
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files

def correct_all_files(type):
    file_list = list_all_files('./public/'+type)
    for file in file_list:
        if os.path.splitext(file)[-1]=='.html':
            correct_file(file,type)
    file_list = list_all_files('./public/Categories/'+type)
    for file in file_list:
        if os.path.splitext(file)[-1]=='.html':
            correct_file(file,type)


correct_all_files("News")
correct_all_files("Researches")
correct_all_files("Projects")
correct_all_files("Blogs")

type="Archive"
file_list = list_all_files('./public/'+type)
for file in file_list:
    if os.path.splitext(file)[-1]=='.html':
        correct_file(file,type)
# is-active

# <a class="navbar-item" href="/Projects">

# <a class="navbar-item is-active" href="/Archive">