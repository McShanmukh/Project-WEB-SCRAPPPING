from bs4 import BeautifulSoup
import requests
import lxml
soup=BeautifulSoup
mb="https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa,Residential-Plot&Locality=Lingampally-Serilingampally&cityName=Hyderabad"
x=requests.get(mb).text
y=soup(x,"lxml")
#master = tkx.ThemedTk()
##        # Disable resizing the window
##        #self.master.resizable(0,0)
##        lst_themes=["aquativo", "arc","black","arc","clearlooks","equilux",\
##                    "itft1","smog", \
##                    "elegance","kroc","keramik",\
##                    "plastik","radiance",\
##                    "winxpblue"]
#window=master        
#master.set_theme("plastik")
#        #self.master.set_theme(lst_themes[np.random.randint(low=0, high=14)])
#
#master.title("WEB SCRAPING STOCK DATA")
#
#tabControl = ttk.Notebook()
#
#tab_input = ttk.Frame(tabControl)
#tabControl.add(tab_input, text='Stock Display')
#tabControl.pack(expand=1, fill="both") 
#parameters_frame = ttk.LabelFrame(tab_input, text="list)
#parameters_frame.grid(column=0, row=0, padx=4, pady=4)
#data=json.load(open("updated.txt"))
##print (data)
# data=y.prettify()
datas=y.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})
data=datas[0]
# print(soup.prettify(data)) # title=data.div.img["alt"]# print(title)# cost=y.find_all("div",{"class" : "m-srp-card__price"})# print(cost[0].text)# areacost=y.find_all("div",{"class":"m-srp-card__area"})# print(areacost[0].text)# st0=y.find_all("div",{"class":"m-srp-card__summary__title"})# # print(st1[0].text.strip())# si1=y.find_all("div",{"class":"m-srp-card__summary__info"})# # print(si1[0].text.strip())# print(st1[0].text.strip()+" : "+si1[0].text.strip())# areaaval=y.find_all("div",{"class":"m-srp-card__summary__info"}) # # print(areaaval[0].text)# st1=y.find_all("div",{"class":"m-srp-card__summary__title"}# # print(st1[1].text.strip())# si1=y.find_all("div",{"class":"m-srp-card__summary__info"})# # print(si1[1].text.strip())# print(st1[1].text.strip()+" : "+si1[1].text.strip())# st2=y.find_all("div",{"class":"m-srp-card__summary__title"})# # print(st1[2].text.strip())# si2=y.find_all("div",{"class":"m-srp-card__summary__info"})# # print(si1[2].text.strip())# print(st1[2].text.strip()+" : "+si1[2].text.strip())# st3=y.find_all("div",{"class":"m-srp-card__summary__title"})# # print(st1[4].text.strip())# si3=y.find_all("div",{"class":"m-srp-card__summary__info"})# # print(si1[1].text.strip())# print(st1[3].text.strip()+" : "+si1[3].text.strip())# st4=y.find_all("div",{"class":"m-srp-card__summary__title"})# # print(st1[1].text.strip())# si4=y.find_all("div",{"class":"m-srp-card__summary__info"})# # print(si1[1].text.strip())# print(st1[4].text.strip()+" : "+si1[4].text.strip())# # print(y.prettify())# desc=y.find_all("div",{"class":"m-srp-card__description js-content-read-more truncated"})# print(desc[0].text.strip())
for data in datas:
    name=data.div.img["alt"]
    print("Site Name : "+name,"\n")
    cost=y.find_all("div",{"class" : "m-srp-card__price"})
    print("Cost : "+cost[0].text,"\n")
    areacost=y.find_all("div",{"class":"m-srp-card__area"})
    print("AREASFT : "+areacost[0].text,"\n")
    st0=y.find_all("div",{"class":"m-srp-card__summary__title"})
    # print(st1[0].text.strip())
    si0=y.find_all("div",{"class":"m-srp-card__summary__info"})
    # print(si1[0].text.strip())
    print(st0[0].text.strip()+" : "+si0[0].text.strip(),"\n")# areaaval=y.find_all("div",{"class":"m-srp-card__summary__info"}) 
    # print(areaaval[0].text)
    st1=y.find_all("div",{"class":"m-srp-card__summary__title"})
    # print(st1[1].text.strip())
    si1=y.find_all("div",{"class":"m-srp-card__summary__info"})
    # print(si1[1].text.strip())
    print(st1[1].text.strip()+" : "+si1[1].text.strip(),"\n")
    st2=y.find_all("div",{"class":"m-srp-card__summary__title"})
    # print(st1[2].text.strip())
    si2=y.find_all("div",{"class":"m-srp-card__summary__info"})
    # print(si1[2].text.strip())
    print(st1[2].text.strip()+" : "+si1[2].text.strip(),"\n")
    st3=y.find_all("div",{"class":"m-srp-card__summary__title"})
    # print(st1[4].text.strip())
    si3=y.find_all("div",{"class":"m-srp-card__summary__info"})
    # print(si1[1].text.strip())
    print(st1[3].text.strip()+" : "+si1[3].text.strip(),"\n")
    st4=y.find_all("div",{"class":"m-srp-card__summary__title"})
    # print(st1[1].text.strip())
    si4=y.find_all("div",{"class":"m-srp-card__summary__info"})
    # print(si1[1].text.strip())
    print(st1[4].text.strip()+" : "+si1[4].text.strip(),"\n")
    # print(y.prettify())
    desc=y.find_all("div",{"class":"m-srp-card__description js-content-read-more truncated"})
    print(desc[0].text.strip())
    print("\n============================================================================================================================\n\n")
    
    