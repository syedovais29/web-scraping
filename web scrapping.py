import requests
from urllib.request import urlopen 
from bs4 import BeautifulSoup as bs
import logging

logging.basicConfig(filename="ovais.log",level=logging.INFO)

yt_url=('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=iphone+12&_sacat=0https://www.ebay.com/itm/115890296667?hash=item1afb99975b:g:SOsAAOSwTCFk3Vtq&amdata=enc%3AAQAIAAAA4LokLeJHcSF9G6x5m%2BxnBKLV5CTf73k5S3WAwDs0qO3%2FLpBAkVacmMFTmFXA4P63%2FZDVIUPNkDewukzf7aD0K0%2FFZeT3x3mqwQ394R3pXFD9mkvelbuUYEONwIsCTdswH9NNnQT%2B62JxW4U%2FLUiG3bEBFINkWOtRUnjaX2VpAhocu8nlDNfsRGvNyOehe2bp2UMDgAINIWcJtprew9dL3nvbK4FJjryQqqYEzx%2BMPUNVWinsfdfhtcYRo58g1kZl3iLiYZxtOJYdjntMK4CBhenaCIp%2BMOQ0MFrXzdpGFaDB%7Ctkp%3ABFBM3sfmpYFj')
client=urlopen(yt_url)
content = client.read()
     
# print(content)
yt_html=bs(content,'html.parser')   
# logging.info(yt_html)
try:
     href_tags = yt_html.find_all("div",{"class":"s-item__wrapper clearfix"})
     del href_tags[0] 
     print(href_tags[60].div.div.a['href']) 
except TypeError as e :        
   print(e)

for i in href_tags:  
     logging.info(i.div.div.a['href'])

product_link =i.div.div.a['href']
product_req=requests.get(product_link)
logging.info(product_req)   
logging.info(product_link)
print(product_link)
product_html=bs(product_req.text,'html.parser')
logging.info(product_html)

comment_box=product_html.div.find_all("div",{"class":"fdbk-container"})
for i in comment_box:
    logging.info(i.find("div", {"class": "fdbk-container__details__info__username"}).span.text)
for i in comment_box:
    logging.info(i.find("div",{"class":"fdbk-container__details__comment"}).span.text)
  

