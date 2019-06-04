from tkinter import *
import requests
from bs4 import BeautifulSoup
import time, threading

root = Tk()
root.geometry('500x150')
root.title("博客点击量刷新系统")
fup = Frame(root)
fup.pack()

address = StringVar()
pageNum = StringVar()
num = StringVar()

label = Label(fup, text="博客地址：", width=8, anchor=E)
label.grid(row=1, column=1)
entry = Entry(fup, textvariable=address, width=20)
entry.grid(row=1, column=2)

label2 = Label(fup, text="博客页数：", width=8, anchor=E)
label2.grid(row=2, column=1)
entry2 = Entry(fup, textvariable=pageNum, width=20)
entry2.grid(row=2, column=2)

label3 = Label(fup, text="访问次数：", width=8, anchor=E)
label3.grid(row=3, column=1)
entry3 = Entry(fup, textvariable=num, width=20)
entry3.grid(row=3, column=2)

label4 = Label(fup, text="", width=8, anchor=E)
label4.grid(row=4, column=1)


def done():
    for i in range(0, int(num.get())):
        for Page in range(1, int(pageNum.get()) + 1):
            print('Page=', Page)
            # 博客地址，这里是我的CSDN博客地址
            # url = 'https://blog.csdn.net/qq_41430142/article/list/' + str(Page)
            # print(url)
            url = address.get() + '/article/list/' + str(Page)
            html = GetHtmlText(url)
            soup = BeautifulSoup(html, 'html.parser')
            Find_Click(soup)
    label4.config(text="结束")


# 解析源码
def GetHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return ''


# 查找博文地址并进行一次点击
def Find_Click(soup):
    Divs = soup.find_all('div', {'class': 'article-item-box csdn-tracking-statistics'})
    for Div in Divs:
        ClickUrl = Div.find('h4').find('a')['href']
        # 点一下
        Click = requests.get(ClickUrl, timeout=30)


# t = threading.Thread(target=done)

def loop():
    label4.config(text="扫描中.......")
    t = threading.Thread(target=done)
    t.setDaemon(True)
    t.start()

fdown = Frame(root)
fdown.pack()
bt1 = Button(fdown, text="开始访问", command=loop)
bt1.pack()
mainloop()
