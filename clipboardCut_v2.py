import win32con,win32api
import win32clipboard  as b
import re
import sys,os
import time
try:
    os.mkdir('configuration')
    print("Please create a file named 'cilpboardCut.conf' in the '\\configuration' folder to place the stirngs in lines which will be cut from clipboard")
except Exception as e:
    pass
try:
    conf = open('configuration\\cilpboardCut.conf','r',encoding='UTF-8')
except Exception as e:
    print(e)
sys.stdin=conf
inputStrings=[]
while True:
    try:
        print("Please input the string to be cut.")
        inputStrings.append(input())
    except Exception as e:
        break
conf.close()
content=""
while True:
    b.OpenClipboard()
    content=b.GetClipboardData(win32con.CF_UNICODETEXT)
    print("content:",content)
    if content!="":
        for s in inputStrings:
            pattern=re.compile(s)
            try:
                content=re.sub(pattern,"",content)
            except(e):
                print(e)
        b.EmptyClipboard()
        b.SetClipboardData(win32con. CF_UNICODETEXT,content)   
    b.CloseClipboard()
    time.sleep(1)
