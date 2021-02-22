import unittest
from selenium import webdriver
import time
from pageItem import PageItems



class CarritoCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.itemsPage = PageItems(self.driver)


    def test_search_find_tshirts(self):
        self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a').click()
        self.driver.find_element_by_id('color_1').click()
        self.driver.find_element_by_id('quantity_wanted').clear()
        self.driver.find_element_by_id('quantity_wanted').send_keys('25')
        self.itemsPage.hacer_click_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i', 3)
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_id("quantity_wanted").text, '')




    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()