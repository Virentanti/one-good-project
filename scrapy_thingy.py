from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def scrape(url,x,stp):

    driver = webdriver.Firefox(r"C:\Users\Rashmi\Desktop\Development\one-good-project")
    rep=int(url[-5:])
    url=url[:-5]
    x+='.txt'
    text=[]
    file=open(x,'a')
    for i in range(rep,stp):
        d_url=url+str(i)
        driver.get(d_url)
        txt=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text
        file.write(txt)
        text.append(txt)