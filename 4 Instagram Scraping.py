from bs4 import BeautifulSoup as Bs4
from time import sleep
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

def scroll(browser, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = browser.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = browser.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height


driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')

driver.maximize_window()

url = 'https://www.instagram.com/'
driver.get(url)


driver.implicitly_wait(10)

fb_xpath = """//*[@id="loginForm"]/div/div[5]/button/span[2]"""
get_fb_element = driver.find_element_by_xpath(fb_xpath)
get_fb_element.click()

driver.implicitly_wait(10)

email = 'Email'
email_xpath = """//*[@id="email"]"""
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email)

driver.implicitly_wait(10)

password = 'Password'
password_xpath = """//*[@id="pass"]"""
find_password_element = driver.find_element_by_xpath(password_xpath)
find_password_element.send_keys(password)
find_password_element.send_keys(Keys.ENTER)

sleep(6)

try:
    os.mkdir(os.path.join(os.getcwd(), 'images'))

except:
    pass

os.chdir(os.path.join(os.getcwd(), 'images'))

profile_url = 'https://www.instagram.com/pic.the.nature/'
driver.get(profile_url)

driver.implicitly_wait(10)

scroll(driver, 4)

source = driver.page_source
html_soup = Bs4(source, 'lxml')
html_soup.prettify()

images = html_soup.find_all('img', {'class': 'FFVAD'})

for image in images:
    name = image['alt'][:10]
    link = image['src']
    try:
        with open(name.replace('.', '-').replace('_', '-').replace(' ', '-').replace('/', '') + '.png', 'wb') as f:
            img = requests.get(link)
            f.write(img.content)

    except:
        print('fail')



driver.quit()
