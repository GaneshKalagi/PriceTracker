import requests
from bs4 import BeautifulSoup
#URL='https://www.amazon.in/Samsung-Galaxy-M12-Storage-Replacement/dp/B08XJG8MQM/ref=sr_1_1_sspa?dchild=1&keywords=mobile&qid=1627738580&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN1g1SFM5OEkzUExYJmVuY3J5cHRlZElkPUEwNjAxNjYxMlZLUDFOSTNZMkJSQSZlbmNyeXB0ZWRBZElkPUEwNzc5NjgzM0daT0ZXME43RTUyRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
#URL="https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_3?dchild=1&keywords=mobile&qid=1627738580&sr=8-3"
#URL="https://www.amazon.in/Nokia-G20-Smartphone-4G-Storage/dp/B09878S5FX/ref=sr_1_2_sspa?dchild=1&keywords=mobile&qid=1627738580&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN1g1SFM5OEkzUExYJmVuY3J5cHRlZElkPUEwNjAxNjYxMlZLUDFOSTNZMkJSQSZlbmNyeXB0ZWRBZElkPUEwODQxNDg2M01UNEQ2MzRWTkZJNSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

products_to_track=[
    {
        "product_url":"https://www.amazon.in/Samsung-Galaxy-M12-Storage-Replacement/dp/B08XJG8MQM/ref=sr_1_1_sspa?dchild=1&keywords=mobile&qid=1627738580&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN1g1SFM5OEkzUExYJmVuY3J5cHRlZElkPUEwNjAxNjYxMlZLUDFOSTNZMkJSQSZlbmNyeXB0ZWRBZElkPUEwNzc5NjgzM0daT0ZXME43RTUyRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name" : "Samsung Galaxy M12", "target_price":10000
    },
    {
        "product_url":"https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_3?dchild=1&keywords=mobile&qid=1627738580&sr=8-3",
        "name": "Redmin9A", "target_price":7000
    },
    {
        "product_url":"https://www.amazon.in/Nokia-G20-Smartphone-4G-Storage/dp/B09878S5FX/ref=sr_1_2_sspa?dchild=1&keywords=mobile&qid=1627738580&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExN1g1SFM5OEkzUExYJmVuY3J5cHRlZElkPUEwNjAxNjYxMlZLUDFOSTNZMkJSQSZlbmNyeXB0ZWRBZElkPUEwODQxNDg2M01UNEQ2MzRWTkZJNSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=",
        "name": "Nokia-G20", "target_price":14000
    },
    {
        "product_url":"https://www.amazon.in/Test-Exclusive_2020_1112-Multi-3GB-Storage/dp/B089MS7D8F/ref=sr_1_20?dchild=1&keywords=mobile&qid=1628670796&s=electronics&sr=1-20",
        "name": "Redmi 9", "target_price":10000
    },
     {
        "product_url":"https://www.amazon.in/realme-Racing-Storage-Additional-Exchange/dp/B099T7XNGW/ref=sr_1_18?dchild=1&keywords=mobile&qid=1628670796&s=electronics&sr=1-18",
        "name": "realme narzo", "target_price":12500
    }
]


#my user agent in google from which i will get below link for browser
headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        }

def give_product_price(URL):
    
    
    
    page=requests.get(URL, headers=headers)
    
    #print(page)

    Soup=BeautifulSoup(page.content,'html.parser')
    
    #print(Soup.prettify()) it print or pull complete html code but i need only price from that so iwrite below code using right click inspect
    #Beautiful Soup is a Python library that is used for web scraping purposes to pull the data out of HTML and XML files. It creates a parse tree
    #from page source code that can be used to extract data in a hierarchical and more readable manne

    product_price=Soup.find(id="priceblock_ourprice")

    if (product_price==None):
        product_price=Soup.find(id="priceblock_dealprice")

        #print(product_price)
   # print(product_price.getText())
   
    return product_price.getText()

result_file=open("my_result_file.csv", "w")

try:
    
    for every_product in products_to_track:
        product_price_returned=give_product_price(every_product.get("product_url"))
        print(product_price_returned+"="+ every_product.get("name"))

        my_product_price=product_price_returned[1:]
        my_product_price=my_product_price.replace(',','')
        my_product_price=int(float(my_product_price))

        print(my_product_price)

        
        if my_product_price < every_product.get("target_price") :
            print("Congrats, available at your price")
            result_file.write(every_product.get("name")+"- \t"+"available at your price"+str(my_product_price)+"\n")
        else:
            print("Still available at the same price")
finally:
    result_file.close()
