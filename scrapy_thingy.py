from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from lxml import html
import requests
  
def scrape(url,x,stp):
    rep=int(url[-5:])
    url=url[:-5]
    x+='.txt'
    text=[]
    file=open(x,'a')
    for i in range(rep,stp):
        d_url=url+str(i)
        print(d_url)
        page = requests.get(d_url)
        tree = html.fromstring(page.content)
        #driver.get(d_url)
        #txt=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text

        txt = tree.xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div")
        print(txt)
        text.append(txt)
        file.write(txt)

    

def scrape0(url,x,stp):

    driver = webdriver.Firefox(r"C:\Users\Rashmi\Desktop\Development\one-good-project")
    rep=int(url[-5:])
    url=url[:-5]
    x+='.txt'
    text=[]
    file=open(x,'a')
    for i in range(rep,stp):
        d_url=url+str(i)
        print(d_url)
        driver.get(d_url)
        txt=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text
        print(txt)
        text.append(txt)
    file.write(str(text))