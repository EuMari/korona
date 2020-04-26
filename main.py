import unittest
from selenium import webdriver
from time import sleep


class MojPrzypadekTestowy(unittest.TestCase):
    def setUp(self):
        print("Przygotowanie testu")
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.sukienkimm.pl/")
        self.driver.maximize_window()

    def testSelenium(self):
        driver = self.driver
        print("wylaczam alert")
        al = driver.find_element_by_id('onesignal-popover-cancel-button')
        al.click()
        print("klikam zaloguj sie")
        zaloguj_btn = driver.find_element_by_xpath('//span[text()=" zaloguj się"]')
        sleep(4)
        zaloguj_btn.click()
        #sleep(4)

    def tearDown(self):
        print("sprzatanie po tescie")
        self.driver.quit()

if __name__=='__main__':
    unittest.main()