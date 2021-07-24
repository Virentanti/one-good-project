from selenium import webdriver
from progress.bar import Bar
from time import sleep

def ssw(url,typ,stp):

    rep=int(url[-5:])
    url=url[:-5]
    bar = Bar('Scraping...', max=stp, suffix="%(percent).1f%% - %(eta)ds")
    for i in range(rep,rep+stp):
        try:
            d_url=url+str(i)
            driver = webdriver.Firefox()
            driver.maximize_window()
            driver.get(d_url)
            sleep(2)
            # identify element to capture the screenshot
            try:
                #l=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div")
                q=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div/ul/li/h1")
                a=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div/ul/li/div")
            except:
                q=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div/ul/li/h1")
                a=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div/ul/li/div")
            # capture the screenshot with screenshot method
            q_name="q_"+typ+"_"+str(i)+".png"
            a_name="a_"+typ+"_"+str(i)+".png"
            q.screenshot(q_name)
            a.screenshot(a_name)
            #remove_background(x)
            driver.quit()
            bar.next()
        except:
            bar.next
