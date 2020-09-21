from bs4 import BeautifulSoup as soup
import lxml
import requests
from fake_useragent import UserAgent
from selenium import webdriver
import smtplib
import schedule 
import time
import threading


url=input("Enter the Url:")
driver=webdriver.Chrome()
driver.get(url)
req=driver.execute_script("return document.documentElement.outerHTML")

# Search input process


# Search input correction process


# wb_url=requests.get(url)
wb_sp=soup(req,"lxml")
#Adding headers with UserAgent
# ua=UserAgent()
# header={'user-agent': ua.chrome}

#Stock Description:

print()
stkname=wb_sp.find("p",{"class":"title"},{"span id":"companyName"})
print("Stock Name:"+stkname.text)
stkser=wb_sp.find("ul",{"class":"series"},{"id":"otherSeries"})
print(stkser.text)
stksbl=wb_sp.find("span",{"id":"symbol"})
print(stksbl["id"]+":"+stksbl.text)
stkisin=wb_sp.find("span",{"id":"isinCode"})
print("ISIN:"+stkisin.text)
stksts=wb_sp.find("span",{"id":"statusCode"})
print(stksts["id"]+":"+stksts.text)
stkdet=wb_sp.find("ul",{"id":"pe_details"})
print(stkdet.text.strip())

def checkprice():
    #Stock values:
    stkva=wb_sp.find("span",{"id":"lastPrice"})
    print(stkva)
    stkval=stkva.text.strip()
    print(stkval)
    stkval=stkval.split(",")
    print(stkval)
    stkval="".join(stkval)
    print(stkval)
    stkvalue=float(stkval)
    print(stkva['id'],":",stkvalue)

#     print(stkva['id'],":",stkvalue)
    try:
        stklg=wb_sp.find('span',{'class':"up"},{'id':"change"})

    except:
        print("Loss/Gain:",stklg.text.strip())
    try:
        stkdn=wb_sp.find('span',{'class':"down"},{'id':"change"})
    except:
        print("Loss/Gain:",stkdn.text.strip())
    stkper=wb_sp.find('a',{'id':"pChange"})
    print("Loss/Gain(%):",stkper.text.strip())
    stkprcl=wb_sp.find('div',{'id':"previousClose"})
    print(stkprcl['id'],":",stkprcl.text.strip())
    stkopn=wb_sp.find('div',{'id':"open"})
    print(stkopn['id'],":",stkopn.text.strip())
    stkdyhi=wb_sp.find('div',{'id':"dayHigh"})
    print(stkdyhi['id'],":",stkdyhi.text.strip())
    stkdylw=wb_sp.find('div',{'id':"dayLow"})
    print(stkdylw['id'],":",stkdylw.text.strip())
    stkclsp=wb_sp.find('div',{'id':"closePrice"})
    print(stkclsp['id'],":",stkclsp.text.strip())

checkprice()
    
# Email sending process
def  send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("mohanmcsn8@gmail.com","kfskryzgiqqcgcjw")
    
    subject="Price is Down react now "
    body = "check price Immediately!!! If not You might miss this Price "
    
    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail(
        'mohanmcsn8@gmail.com',
        'mcs8686357610@gmail.com',
        msg
    )
    print("hey mail sent")
    print()
    print()
    server.quit()
def  send_mail1():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("mohanmcsn8@gmail.com","kfskryzgiqqcgcjw")
    
    subject="Price is High react now If not you might get loss"
    body = "Go to App to Check Price "
    
    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail(
        'mohanmcsn8@gmail.com',
        'mcs8686357610@gmail.com',
        msg
    )
    print("hey mail sent")
    print()
    print()
    server.quit()
    
 schedule.every(5).seconds.do(checkprice)

 desva=input("Enter desired stock value that you dream to buy: ")
 desval=float(desva)

 if(stkvalue < desval):
     send_mail()
 if(stkvalue > desval):
     send_mail1()
 if(stkvalue == desval):
     send_mail() 
 threading.Thread()    
    
 def scheduler_five():
     schedule.every(5).seconds.do(checkprice)
     while 1:
         schedule.run_pending()
         time.sleep(1)
 stkaddr=wb_sp.find("ul",{"id":"address"})
 print(stkaddr.text)