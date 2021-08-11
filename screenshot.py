from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from progress.bar import Bar
import os
import time

def ssw(url,x,stp):

    rep=int(url[-5:])
    url=url[:-5]
    stop=stp
    # if stp>50: stop= 50
    bar = Bar('Scraping...', max=stop, suffix="%(percent).1f%% - %(eta)ds")
    for i in range(rep,rep+stop):
        try:
            option=Options()
            option.headless=True
            d_url=url+str(i)
            driver = webdriver.Firefox(options=option)
            driver.maximize_window()
            driver.get(d_url)
            time.sleep(2)
            # identify element to capture the screenshot
            try:
                #l=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div")
                q=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div/ul/li/h1")
                a=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div/ul/li/div")
            except:
                q=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div/ul/li/h1")
                a=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div/ul/li/div")
            # capture the screenshot with screenshot method
            q_name="q_"+x+str(i)+".png"
            a_name="a_"+x+str(i)+".png"
            # q_name=os.path.join(x,q_name)
            # a_name=os.path.join(x,a_name)
            q.screenshot(q_name)
            a.screenshot(a_name)
            driver.quit()
            bar.next()
        except:
            driver.quit()
        finally:
            bar.finish()
