import time

from bs4 import BeautifulSoup as Bs4
from selenium import webdriver

driver = webdriver.Chrome(executable_path='C:/WebDrivers/chromedriver.exe')

url = "https://www.linkedin.com"
driver.get(url)

time.sleep(3)

email_xpath = """//*[@id="session_key"]"""
email_id = 'Your Email'
find_email_element = driver.find_element_by_xpath(email_xpath)
find_email_element.send_keys(email_id)

time.sleep(3)

password_xpath = """//*[@id="session_password"]"""
password = 'Your Password'
find_pass_element = driver.find_element_by_xpath(password_xpath)
find_pass_element.send_keys(password)

time.sleep(2)

sign_in_xpath = """/html/body/main/section[1]/div[2]/form/button"""
find_sign_in_element = driver.find_element_by_xpath(sign_in_xpath)
find_sign_in_element.click()

time.sleep(1)

exact_url = 'https://www.linkedin.com/company/google/about/'
driver.get(exact_url)

time.sleep(3)

src = driver.page_source
html_soup = Bs4(src, 'lxml')

required_material_0 = html_soup.find_all('dt', {'class': 'org-page-details__definition-term t-14 t-black t-bold'})
getting_text_0 = required_material_0[2].get_text().strip()
print(getting_text_0 + ':')

required_material_1 = html_soup.find('dd', {'class': 'org-about-company-module__company-size-definition-text'
                                                     ' t-14 t-black--light mb1 fl'})
getting_text_1 = required_material_1.get_text().strip()
print('     ' + getting_text_1)

required_material_2 = html_soup.find('dd', {'class': 'org-page-details__employees-on-linkedin-count'
                                                     ' t-14 t-black--light mb5'})
getting_text_2 = required_material_2.get_text().strip()
print('     ' + getting_text_2[0:19])

driver.quit()
