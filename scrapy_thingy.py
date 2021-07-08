from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

def scrape(url,x,stp):

    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    rep=int(url[-5:])
    #print(rep)
    url=url[:-5]
    #print(url)
    x+='.txt'
    text=''
    file=open(x,'a',encoding='utf-8')
    for i in range(rep,rep+stp):
        driver = webdriver.Firefox(r"C:\Users\Rashmi\Desktop\Development\one-good-project")
        d_url=url+str(i)
        print(d_url)
        driver.get(d_url)
        try:
            txt=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text
        except:
            txt=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div").text
        print(txt)
        text=text + txt+ '\n\n\n'
        driver.close()
        file.write(txt+'\n\n\n\n')
    #print(text)


#scrape('https://www.studyadda.com/question-bank/assertion-and-reason_q1/1162/84237','afg',21)