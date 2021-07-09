from selenium import webdriver
from progress.bar import Bar

def scrape00(url,x,stp):

    #driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    rep=int(url[-5:])
    #print(rep)
    url=url[:-5]
    #print(url)
    x+='.txt'
    text=''
    driver = webdriver.Firefox(r"C:\Users\Rashmi\Desktop\Development\one-good-project")
    driver.get('www.google.com')
    file=open(x,'a',encoding='utf-8')
    bar = Bar('Scraping...', max=stp, suffix="%(percent).1f%% - %(eta)ds")
    for i in range(rep,rep+stp):
        try:
            d_url=url+str(i)
            #print(d_url)
            driver.execute_script(f"window.open('about:blank',{i});")
            driver.switch_to.window(i)
            driver.get(d_url)
            try:
                txt=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text
            except:
                txt=driver.find_element_by_xpath("/html/body/div[3]/div/div/section/div[1]/div[1]/div").text
            #print(txt)
            text=text + txt+ '\n\n\n'
            driver.close()
            file.write(txt+'\n\n\n\n')
            bar.next()
        except:
            bar.next()
    bar.finish()