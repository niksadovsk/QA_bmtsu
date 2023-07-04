from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

URL = 'https://www.saucedemo.com/'
LOGIN = 'standard_user'
PASSWORD = 'secret_sauce'

def get_driver():
  chrome_options = Options()
  chrome_options.add_argument("--window-size=1920,800")
  chrome_options.add_argument('--headless')
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                              options=chrome_options)
  driver.implicitly_wait(10)
  return driver

def get_element(driver, id):
  element = driver.find_element(By.ID, id)
  return element

def open_page(driver, url):
  driver.get(url)

def fill_form (driver, id, data):
  element = get_element(driver, id)
  element.send_keys(data)
  
def element_click (driver, id):
  element = get_element(driver, id)
  element.click()

def login(driver, name, password):
  fill_form(driver, 'user-name', name)
  fill_form(driver, 'password', password)
  element_click(driver, 'login-button')

  
driver = get_driver() 
open_page(driver, URL)
login(driver = driver, name = LOGIN, password = PASSWORD)
driver.quit()


