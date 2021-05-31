# import time
# from selenium.webdriver.common.keys import Keys
from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
chromedriver = r"C:\Users\Bharat\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver)
driver.get('https://munet.mu-sigma.com/Enterpriseview.aspx?html.app=EMuSigmaQMS1744d1')

# searchbox = driver.find_element_by_id("search")



# searchbox = driver.find_element_by_xpath('//*[@id="search"]')
# searchbox.send_keys("StatQuest with Josh Starmer")

# driver.find_element_by_name("Value").send_keys(Keys.ENTER)

# searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/button')
# searchbutton.click()
