from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from PIL import Image

import time

class CaptchaImage():
    #browser = webdriver.Chrome(executable_path='./chromedriver')

    def getCaptchaImage(self, browser):
        self.browser = browser
        self.openSATHomePage()
        self.openDownloadInvoicesPage()
        self.getDownloadPageScreenshot()
        self.cropCaptchaImage()

    def openSATHomePage(self):
        self.browser.get("https://www.sat.gob.mx/personas/factura-electronica")

    def openDownloadInvoicesPage(self):
        e = self.browser.find_element_by_link_text('Cancela y recupera tus facturas')
        e.click()
        self.browser.switch_to_window(self.browser.window_handles[1])

    def getDownloadPageScreenshot(self):
        delay = 3 # seconds
        try:
            WebDriverWait(self.browser, delay).until(EC.presence_of_element_located((By.ID, 'buttonFiel')))
            print("Page is ready!")
            time.sleep(3)
            self.browser.save_screenshot("captcha.png")
        except TimeoutException:
            print("Loading took too much time!")

    def cropCaptchaImage(self):
        img = Image.open("captcha.png")
        area= (75, 325, 317, 425)
        cropped=img.crop(area)
        cropped.save("captcha.png", "PNG")
        img.close()
        print("Captcha saved")
