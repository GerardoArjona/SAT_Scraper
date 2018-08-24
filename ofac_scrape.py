from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from PIL import Image

import time

import urllib

browser = webdriver.Firefox(executable_path='/home/konsigue2/Documentos/scraping_SAT/geckodriver')

browser.get("https://www.sat.gob.mx/personas/factura-electronica")

e=browser.find_element_by_link_text('Cancela y recupera tus facturas')
e.click()
browser.switch_to_window(browser.window_handles[1])
delay = 3 # seconds
try:
    WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'buttonFiel')))
    print("Page is ready!")
    time.sleep(3)
    browser.save_screenshot("captcha.png")
    img = Image.open("captcha.png")
    area= (75, 325, 317, 425)
    cropped=img.crop(area)
    cropped.save("captcha.png", "PNG")
    img.close()

    print("Captcha saved")
    browser.quit()
except TimeoutException:
    print("Loading took too much time!")