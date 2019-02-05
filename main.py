import requests
from bs4 import BeautifulSoup

root='http://122.200.75.13'
path='/道藏/藏外/庄子.html'
useless=open('useless.txt',mode='w+')
convertion=open('convertion.txt',mode='w+')
#第一次循环
r=requests.get(root+path)
r.encoding='utf-8'
raw=BeautifulSoup(r.content,features="html.parser")
#遍历至最后一页之前
while raw.find_all('a',text='下一页'):
    for line in raw.body.span:
        if '无用' in str(line):
            print(line)
            useless.write(str(line))
        if '物化' in str(line):
            print(line)
            convertion.write(str(line))
    print(raw.find_all('a', text='下一页')[0]['href'])
    new_path = raw.find_all('a', text='下一页')[0]['href']
    r = requests.get(root+new_path)
    r.encoding = 'utf-8'
    raw = BeautifulSoup(r.content, features="html.parser")
