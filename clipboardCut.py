#win32api是隐性限制，写了一下午的元凶
#打包：pyinstaller.exe -F 文件路径/要打包的文件.py
import win32con,win32api
import win32clipboard  as b
import re
import sys,os
import time
#from selenium import webdriver
try:
    os.mkdir('configuration')
except Exception as e:
    #print(e)
    pass
try:
    #conf=open('configuration\cilpboardCut.conf','w')
    #conf.close()
    conf = open('configuration\cilpboardCut.conf','r',encoding='UTF-8')
except Exception as e:
    print(e)
    pass

#originalStdin=sys.stdin
sys.stdin=conf

inputStrings=[]

while True:
    try:
        inputStrings.append(input("Please input the string to be cut."))
    except Exception as e:
        print(e)
        break

conf.close()
#sys.stdin=originalStdin
content=""
#i=0
while True:
    #i+=1
    b.OpenClipboard()
    #content=b.GetClipboardData(win32con.CF_TEXT)
    content=b.GetClipboardData(win32con.CF_UNICODETEXT)
    print(content)
    for s in inputStrings:
        #content=str(content,encoding="gbk").replace(s,'')
        #print("s:",s)
        #print("content:",content)
        pattern=re.compile(s)
        content=re.sub(pattern,"",content)
    b.EmptyClipboard()
    #b.SetClipboardData(win32con.CF_TEXT,bytes(content,encoding="gbk"))
    b.SetClipboardData(win32con.CF_UNICODETEXT,content)

    print(b.GetClipboardData(win32con.CF_UNICODETEXT))
    
    b.CloseClipboard()
    
    print(content)
    #print(str(content,encoding="gbk"))
    time.sleep(1)
#driver = webdriver.Firefox()
#driver.get("http://www.baidu.com/s?wd="+content)
