import pandas as pd
from bs4 import BeautifulSoup as Bs4
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


url = 'https://www.facebook.com/login'
driver.get(url)

driver.implicitly_wait(10)

email = '03244307348'
email_xpath = """//*[@id="email"]"""
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email)

driver.implicitly_wait(10)

password = '6789qwerty'
password_xpath = """//*[@id="pass"]"""
find_password_element = driver.find_element_by_xpath(password_xpath)
find_password_element.send_keys(password)
find_password_element.send_keys(Keys.ENTER)

sleep(6)

group_url = 'https://www.facebook.com/groups/Love.EI/members'
driver.get(group_url)

driver.implicitly_wait(10)
person_class = "oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o" \
               " kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr" \
               " f1sip0of lzcic4wl oo9gr5id gpro0wi8 lrazzd5p"
find_person_element = driver.find_element_by_class_name(person_class)
find_person_element.click()

# scroll(driver, 2)
