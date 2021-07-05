from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox(r"C:\Users\Rashmi\Desktop\Development\one-good-project")


text=''

for i in range(84237,84259):
    url='https://www.studyadda.com/question-bank/assertion-and-reason_q2/1162/84237'
    url.replace(str(84327),str(i))
    driver.get(url)
    text+=driver.find_element_by_xpath("/html/body/div[2]/div/div/section/div[1]/div[1]/div").text

#driver.implicitly_wait(10)
print(text)