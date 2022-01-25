from bs4.builder import HTMLTreeBuilder
from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'C:\\Users\\Devansh-PC\\Desktop\\Covid_Notification\\download.ico',
        timeout=5
    )

def getData(url):
    r= requests.get(url)
    return r.text


if __name__ == "__main__":
    while True:
        notifyMe("Dev", "Let's Stop the Spread of this virus together") 
        myHtmlData= getData("https://www.worldometers.info/coronavirus/")
        soup= BeautifulSoup(myHtmlData, 'html.parser')
        
        #print(soup.prettify())

        myDataStr=""
        for tr in soup.find_all('tbody')[6].find_all('tr'):
            myDataStr += tr.get_text()

        myDataStr= myDataStr[1:]
        itemList= myDataStr.split('\n\n')

        countries=['USA','India', 'Brazil']
        for item in itemList[77:100]:
            datalist=(item.split('\n'))
            if datalist[1] in countries:
                print(datalist)
                nTitle='Global Cases of Covid-19'
                nText = f"Country: {datalist[1]}\nTotal : {datalist[2]}\nNew Cases : {datalist[3]}\nTotal Deaths :  {datalist[4]}\nCured :  {datalist[6]}"
                notifyMe(nTitle, nText)
                time.sleep(3)
        time.sleep(3600) #after 1hr again live update
            