# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 12:54:00 2019

@author: huang
"""

from tkinter import *
import tkinter.messagebox as mb
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei'] 

t=open(r"C:\Users\huang\Desktop\大作业\英语.txt").read()
top=Tk()
top.title('文本编辑器')
def f1():
    t1.insert(1.0,t)
t1=Text(top)
t1.pack()

a=t.split()
b=[]
for i in a:
    if i[-1] in ['.',',']:
        b.append(i[0:-1].lower())
    else:
        b.append(i.lower())

def danci():
    top1=Tk()
    top1.title('单个单词')
    t2=Text(top1,width=80,height=30)
    for x in b:
        t2.insert('end',x+'  ')
    t2.pack()
def dczs():
    print('总词数:',len(b))
    print('* '*20)
word_count={}
for j in b:
    word_count[j]=b.count(j)
items=list(word_count.items())
items.sort(key=lambda x:x[1],reverse=True)

def dcs():
    print('出现过的单词数:',len(items))
    print('* '*20)
def tj():
    top2=Tk()
    top2.title('所有单词频数')
    t3=Text(top2)
    for i in range(len(items)):
        word,count=items[i]
        t3.insert(END,str(word)+':'+str(count)+'   ')
    t3.pack()
def czdc():
    top3=Tk()
    top3.title('查找单词频数')
    top3.geometry('250x150')
    l1=Label(top3,text='单词')
    l2=Label(top3,text='频数')
    t4=Text(top3,width=10,height=1)
    t5=Text(top3,width=10,height=1)
    l1.place(x=40,y=20)
    l2.place(x=40,y=60)
    t4.place(x=100,y=20)
    t5.place(x=100,y=60)
    def czdc1():
        s1=t4.get(1.0,END)[:-1]
        if s1 in b:
            t5.insert(1.0,word_count[s1])
        else:
            mb.showinfo('错误','该单词不存在')
    button=Button(top3,text='确定',command=czdc1)
    button.place(x=200,y=100)
    
ty1=list(open(r"C:\Users\huang\Desktop\大作业\英文停用词表.txt").read().split())

import matplotlib.pyplot as plt
import numpy as np
word_count1={}
for j in b:
    if j not in ty1:
        word_count1[j]=b.count(j)
items1=list(word_count1.items())
items1.sort(key=lambda x:x[1],reverse=True)
def gjctj():
    x=[]
    y=[]
    print('关键词:',end='  ')
    for i in range(6):
        word,count=items1[i]
        print(word,end='  ')
        x.append(word)
        y.append(count)
    fig, ax = plt.subplots()
    tu=ax.bar(x,y,width=0.50,label='频数')
    plt.xlabel('关键词')
    plt.ylabel('次数')
    plt.title("关键词统计图")
    plt.legend()
    plt.show()

    menubar = Menu(top)
def f2():
    top.quit()
def sc():
    t1.delete(1.0,END)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='打开',command=f1)
filemenu.add_separator()
filemenu.add_command(label='退出',command=f2)
menubar.add_cascade(label='文件',menu=filemenu)

editmenu=Menu(menubar,tearoff=0)
editmenu.add_command(label='删除',command=sc)
editmenu.add_command(label='查看单词',command=danci)
menubar.add_cascade(label='编辑',menu=editmenu)

countmenu=Menu(menubar,tearoff=0)
countmenu.add_command(label='总词数',command=dczs)
countmenu.add_command(label='出现过的单词数',command=dcs)
countmenu.add_command(label='所有单词频数',command=tj)
countmenu.add_command(label='查找单词频数',command=czdc)
countmenu.add_command(label='关键词',command=gjctj)
menubar.add_cascade(label='统计',menu=countmenu)

top.config(menu=menubar)
top.mainloop()