import tkinter as tk
import json
from tkinter import ttk, scrolledtext, Menu, Spinbox, \
                    filedialog as fd, messagebox as mBox
#import nsescrapy
from bs4 import BeautifulSoup as soup
import lxml
import requests
#from fake_useragent import UserAgent
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import smtplib
import schedule 
import time
import threading
from ttkthemes import themed_tk  as tkx
#driver=webdriver.Chrome()
#window=tk.Tk()
master = tkx.ThemedTk()
#        # Disable resizing the window
#        #self.master.resizable(0,0)
#        lst_themes=["aquativo", "arc","black","arc","clearlooks","equilux",\
#                    "itft1","smog", \
#                    "elegance","kroc","keramik",\
#                    "plastik","radiance",\
#                    "winxpblue"]
window=master        
master.set_theme("plastik")
        #self.master.set_theme(lst_themes[np.random.randint(low=0, high=14)])

master.title("WEB SCRAPING STOCK DATA")
        

data=json.load(open("updated.txt"))
#print (data)
global url
global dsm
global set_ml
global dsp1

tabControl = ttk.Notebook()

tab_input = ttk.Frame(tabControl)
tabControl.add(tab_input, text='Stock Display')
tabControl.pack(expand=1, fill="both")  

tab_input2 = ttk.Frame(tabControl)
tabControl.add(tab_input2, text='Price Details')
tabControl.pack(expand=1, fill="both")

tab_input3 = ttk.Frame(tabControl)
tabControl.add(tab_input3, text='Alert Pane')
tabControl.pack(expand=1, fill="both")

parameters_frame = ttk.LabelFrame(tab_input, text=' Stock list')
parameters_frame.grid(column=0, row=0, padx=4, pady=4)

parameters_frame4 = ttk.LabelFrame(tab_input3, text='Desired stock Price')
parameters_frame4.grid(column=0, row=0, padx=4, pady=4)

parameters_frame5 = ttk.LabelFrame(tab_input3, text='Email Details')
parameters_frame5.grid(column=0, row=8, padx=4, pady=4)
# = ttk.(window)
mailentry = ttk.Entry(parameters_frame5, width=48)
mailentry.grid(column=0, row=6, padx=8, pady=4, sticky='W') 

lst_companynames=list(data.values())
lst_companysbl=list(data.keys())
stcklist = ttk.Combobox(parameters_frame, width=48)
stcklist.config(value = lst_companynames)
#stcklist.set("Select a stock name from list")
stcklist.grid(column=1, row=0, padx=8, pady=4, sticky='W')

def  send_mail():
    server=smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login("mohanmcsn8@gmail.com","kfskryzgiqqcgcjw")
    
    subject="Price is Down react now "
    body = "go to check price Immediately!!! If not You might miss this Price "
    
    msg=f"Subject:{subject}\n\n{body}"
    
    server.sendmail(
        'mohanmcsn8@gmail.com',
        meil,
        msg
    )
    print("hey mail sent")
    print()
    print()
    server.quit()
    
def send_mail1():
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
        meil,
        msg
    )
    print("hey mail sent")
    print()
    print()
    server.quit()



def gtreq():
    kfkf=stcklist.get()
    if kfkf in data.values():
        kfkfkey=lst_companysbl[lst_companynames.index(kfkf)]
        global url
        url="https://nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol="+kfkfkey
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)     
        req=driver.execute_script("return document.documentElement.outerHTML")
        wb_sp=soup(req,"lxml")
        stkname=wb_sp.find("p",{"class":"title"},{"span id":"companyName"}).text

        l2.config(text=f"{stkname}")
        stkser=wb_sp.find("ul",{"class":"series"},{"id":"otherSeries"}).text
        print(stkser)
        l4.config(text=f"{stkser}")
        stksbl=wb_sp.find("span",{"id":"symbol"}).text
        l6.config(text=f"{stksbl}")
        stkisin=wb_sp.find("span",{"id":"isinCode"}).text
        l8.config(text=f"{stkisin}")
        stksts=wb_sp.find("span",{"id":"statusCode"}).text
        l10.config(text=f"{stksts}")
        stkdet=wb_sp.find("ul",{"id":"pe_details"}).text.strip()
        l12.config(text=f"{stkdet}")
        global stkvalue
        stkva=wb_sp.find("span",{"id":"lastPrice"})
        stkval=stkva.text.strip()
        stkval=stkval.split(",")
        stkval="".join(stkval)
        stkvalue = float(stkval)
        print(stkva['id'],":",stkvalue) 
        l13.config(text=f"{stkva['id']}:{stkvalue}")
        try:
            stklg=wb_sp.find('span',{'class':"up"},{'id':"change"}).text
            print(f"Loss/Gain: {stklg}")
            l15.config(text=f"{stklg}")
        except:
            pass
        try:
            stkdn=wb_sp.find('span',{'class':"down"},{'id':"change"}).text
            print(f"Loss/Gain:{stkdn}")
            l17.config(text=f"{stkdn}")
        except: 
            pass
            
        stkper=wb_sp.find('a',{"id":"pChange"}).text.strip()
        print(f"Loss/Gain(%):{stkper}")
        l19.config(text=f"{  stkper}")
        stkprcl=wb_sp.find('div',{'id':"previousClose"})
        stkprcl2=stkprcl.text.strip()
        print(f"{stkprcl['id']}:{stkprcl2}")
        l20.config(text=f"{stkprcl['id']}:{stkprcl2}")
        stkopn=wb_sp.find('div',{'id':"open"})
        stkopn2=stkopn.text.strip()
        print(f"{stkopn['id']}:{stkopn2}")
        l21.config(text=f"{stkopn['id']}:{stkopn2}")
        stkdyhi=wb_sp.find('div',{'id':"dayHigh"})
        stkdyhi2=stkdyhi.text.strip()
        print(f"{stkdyhi['id']}:{stkdyhi2}")
        l22.config(text=f"{stkdyhi['id']}:{stkdyhi2}")
        stkdylw=wb_sp.find('div',{'id':"dayLow"})
        stkdylw2=stkdylw.text.strip()
        print(f"{stkdylw}")
        l23.config(text=f"{stkdylw['id']}:{stkdylw2}")
        stkclsp=wb_sp.find('div',{'id':"closePrice"})
        stkclsp2=stkclsp.text.strip()
        print(f"{stkclsp['id']}:{stkclsp2}")
        l24.config(text=f"{stkclsp['id']}:{stkclsp2}")
    else:
        print("else")

def set_ml():
    global meil
    meil=mailentry.get()
    print(meil)
    return meil
def dsp1():
    global dspp
    dspp=dsp.get()
    dspp=float(dspp)
    print(dspp)
    return dspp
def dsm():
    #if(stkvalue < dspp):
     #   send_mail()
    #if(stkvalue > dspp):
    #     send_mail1()
    #if(stkvalue == dspp):
        # send_mail() 
        pass
### PRINTING STOCK DETAILS NAME,TYPE etc.,.
def schd():
    schedule.every(10).seconds.do(gtreq)
    schedule.every().day.at("09:00").do(gtreq)

t1 = threading.Thread(target=gtreq) 
t2 = threading.Thread(target=dsm) 
t3 = threading.Thread(target=schd) 
#t2 = threading.Thread(target=) 
#t1.start() 
t2.start() 
t3.start() 

btn3 = tk.Button(parameters_frame5,width=18, text ="Update Email",command=set_ml)
btn3.grid(row=6, column=4)

dsp = ttk.Entry(parameters_frame4, width=48)
dsp.grid(column=2, row=1, padx=8, pady=4, sticky='W') 

btn2 = tk.Button(parameters_frame4,width=18, text ="Update",command=dsp1)
btn2.grid(row=1, column=4)
btn = tk.Button(parameters_frame,width=18, text ="Search",command=gtreq)
btn.grid(row=0, column=4)

parameters_frame2 = tk.LabelFrame(tab_input, text=' Stock Details')
parameters_frame2.grid(column=0, row=0, columnspan=1, padx=4, pady=4)
#
l1 = tk.Label(tab_input, text="Stock Name : ", font=("Constantia", 14))
l1.grid(column=0, row=1,columnspan=1, padx=1, pady=1)

l2 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l2.grid(column=1, row=1,columnspan=1, padx=1, pady=1)

l3 = tk.Label(tab_input, text="Series - ", font=("Constantia", 14))
l3.grid(column=0, row=2,columnspan=1, padx=4, pady=4)

l4 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l4.grid(column=1, row=2,columnspan=1, padx=4, pady=4)

l5 = tk.Label(tab_input, text="Stock symbol : ", font=("Constantia", 14))
l5.grid(column=0, row=3,columnspan=1, padx=4, pady=4)

l6 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l6.grid(column=1, row=3,columnspan=1, padx=4, pady=4)

l7 = tk.Label(tab_input, text="ISIN : ", font=("Constantia", 14))
l7.grid(column=0, row=4,columnspan=1, padx=4, pady=4)

l8 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l8.grid(column=1, row=4,columnspan=1, padx=4, pady=4)

l9 = tk.Label(tab_input, text="Stock Status : ", font=("Constantia", 14))
l9.grid(column=0, row=5,columnspan=1, padx=4, pady=4)

l10 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l10.grid(column=1, row=5,columnspan=1, padx=4, pady=4)

l11 = tk.Label(tab_input, text="Stock details : ", font=("Constantia", 14))
l11.grid(column=0, row=6,columnspan=1, padx=4, pady=4)

l12 = tk.Label(tab_input, text=" ", font=("Constantia", 14))
l12.grid(column=1, row=6,columnspan=1, padx=4, pady=4)

parameters_frame3 = tk.LabelFrame(tab_input2, text=' Stock Details')
parameters_frame3.grid(column=0, row=0, columnspan=4, padx=4, pady=4)

l13 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l13.grid(column=0, row=1,columnspan=2, padx=4, pady=4)

l14 = tk.Label(tab_input2, text="Gain: ", font=("Constantia", 14))
l14.grid(column=0, row=2,columnspan=2, padx=4, pady=4)

l15 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l15.grid(column=1, row=2,columnspan=2, padx=4, pady=4)

l16 = tk.Label(tab_input2, text="Loss: ", font=("Constantia", 14))
l16.grid(column=0, row=3,columnspan=2, padx=4, pady=4)

l17 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l17.grid(column=1, row=3,columnspan=2, padx=4, pady=4)

l18 = tk.Label(tab_input2, text="Loss/Gain(%):", font=("Constantia", 14))
l18.grid(column=0, row=4,columnspan=2, padx=4, pady=4)

l19 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l19.grid(column=1, row=4,columnspan=2, padx=4, pady=4)

l20 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l20.grid(column=0, row=5,columnspan=2, padx=4, pady=4)

l21 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l21.grid(column=0, row=6,columnspan=2, padx=4, pady=4)

l22 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l22.grid(column=0, row=7,columnspan=2, padx=4, pady=4)

l23 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l23.grid(column=0, row=8,columnspan=2, padx=4, pady=4)

l24 = tk.Label(tab_input2, text="", font=("Constantia", 14))
l24.grid(column=0, row=9,columnspan=2, padx=4, pady=4)





window.mainloop()