import unittest
from selenium import webdriver
import time
from pageIndex import PageIndex
from pageItem import PageItems
from pageItemFunction import PageItemsFunction

class SearchCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.functionItemsPage = PageItemsFunction(self.driver)

    def test_search_no_elements(self):
        self.indexPage.search('hola')
        time.sleep(2)
        self.assertEqual(self.itemsPage.return_no_element_text(), 'No results were found for your search "hola"')

    def test_search_find_dresses(self):

        self.indexPage.search('dress')
        time.sleep(2)
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirt(self):

        self.indexPage.search('t-shirt')
        time.sleep(2)
        self.assertTrue('T-SHIRT' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text,self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)

    def test_carrito_tshirts(self):
        self.driver.find_element_by_xpath('//*[@id="block_top_menu"]/ul/li[3]/a').click()
        self.driver.find_element_by_id('color_1').click()
        self.functionItemsPage.introducir_cantidad('25')
        self.functionItemsPage.hacer_click_by_xpath('//*[@id="quantity_wanted_p"]/a[2]/span/i', 3)
        time.sleep(3)
        self.assertEqual(self.driver.find_element_by_id("quantity_wanted").get_attribute("value"), '28')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()