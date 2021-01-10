import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')

url = 'https://twitter.com/login'
driver.get(url)

driver.implicitly_wait(10)

email_id = 'your email'
email_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/
div/div[1]/label/div/div[2]/div/input"""
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

driver.implicitly_wait(2)

password = '********'
password_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/
div/div[2]/label/div/div[2]/div/input"""
find_password_element = driver.find_element_by_xpath(password_xpath)
find_password_element.send_keys(password)
find_password_element.send_keys(Keys.ENTER)

driver.implicitly_wait(10)

explore_xpath = """//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[2]"""
find_explore_element = driver.find_element_by_xpath(explore_xpath)
find_explore_element.click()

driver.implicitly_wait(10)

search_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div/div/div/div/
div[1]/div[2]/div/div/div/form/div[1]/div/div/div[2]/input"""
find_search_element = driver.find_element_by_xpath(search_xpath)
find_search_element.send_keys('Google')

time.sleep(1)

find_search_element.send_keys(Keys.ENTER)

driver.implicitly_wait(10)

follow_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div
[3]/div/div/div/div[2]/div[1]/div[2]/div/div/span/span"""
find_follow_element = driver.find_element_by_xpath(follow_xpath)
find_follow_element.click()

driver.implicitly_wait(10)

google_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/
div[3]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span/span"""
find_google_element = driver.find_element_by_xpath(google_xpath)
find_google_element.click()

driver.implicitly_wait(10)

post_xpath = """//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[2]/section/div/div/
div[1]/div/div/article/div/div/div/div[2]/div[2]/div[2]/div[1]/div/span[1]"""
find_post_element = driver.find_element_by_xpath(post_xpath)
print(find_post_element.text)

driver.quit()
