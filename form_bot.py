from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from data_puller import Rent


FORM_LINK = 'https://forms.gle/vkAyuqyXraNYRUgJ9'


class DataEntry:
    def __init__(self):
        preferences = webdriver.ChromeOptions()
        preferences.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=preferences)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 5)
        self.driver.get(FORM_LINK)

    def fill_form(self, rent: Rent):
        address_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div['
                                                           '2]/div/div[1]/div/div[1]/input')

        price_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div['
                                                         '2]/div/div[1]/div/div[1]/input')

        link_input = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div['
                                                        '2]/div/div[1]/div/div[1]/input')

        submit_bttn = self.driver.find_element(By.CSS_SELECTOR, 'div.lRwqcd div[aria-label="Submit"]')

        self.wait.until(EC.element_to_be_clickable(address_input)).click()
        address_input.send_keys(rent.address)
        price_input.click()
        price_input.send_keys(rent.price)
        link_input.click()
        link_input.send_keys(rent.link)
        submit_bttn.click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.c2gzEf a'))).click()
