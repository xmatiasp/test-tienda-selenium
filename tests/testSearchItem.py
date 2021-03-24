import unittest
from selenium import webdriver
from TiendaDeRopa.tests.page_objects.pageIndex import PageIndex
from TiendaDeRopa.tests.page_objects.pageItem import PageItems
from TiendaDeRopa.tests.page_objects.pageItemFunction import PageItemsFunction
from selenium.webdriver.chrome.options import Options
import time


class SearchCases(unittest.TestCase):

    def setUp(self):
        option = Options()
        option.add_argument("start-maximized")
        option.add_argument("--headless")
        self.driver = webdriver.Chrome('drivers/chromedriver.exe', options=option)
        #self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        self.indexPage = PageIndex(self.driver)
        self.itemsPage = PageItems(self.driver)
        self.functionItemsPage = PageItemsFunction(self.driver)

    def test_search_no_elements(self):
        self.indexPage.search('hola')
        self.assertEqual('No results were found for your search "hola"', self.itemsPage.return_no_element_text())
        #self.driver.save_screenshot("no_elements.jpg")

    def test_search_find_dresses(self):
        self.indexPage.search('dress')
        self.assertTrue('DRESS' in self.itemsPage.return_section_title())

    def test_search_find_tshirt(self):

        self.indexPage.search('t-shirt')
        self.assertTrue('T-SHIRT' in self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text, self.driver.find_element_by_xpath('//*[@id="center_column"]/h1/span[1]').text)


    def test_carrito_tshirts(self):
        self.indexPage.search('t-shirt')
        self.functionItemsPage.color_change()
        self.functionItemsPage.introducir_cantidad(25)
        self.functionItemsPage.clickear_mas(3)
        self.assertEqual(self.itemsPage.return_cantidad(), '28')


    def test_selections(self):
        self.indexPage.search('t-shirt')
        self.itemsPage.select_by_text('Product Name: Z to A')
        self.itemsPage.select_by_value('reference:asc')
        self.itemsPage.select_by_index(1)

    def test_comprar_vestido(self):
        self.functionItemsPage.click_en_dress()
        self.functionItemsPage.comprar_vestido_casual()
        self.functionItemsPage.agregar_vestidos(4)
        self.itemsPage.select_talle('L')
        self.functionItemsPage.add_to_cart()
        #self.assertEqual(self.itemsPage.return_cantidad_productos(), 'There are 5 items in your cart.')
        self.assertEqual(self.itemsPage.return_total_productos(), '$130.00')
        self.assertEqual(self.itemsPage.return_total_shipping(), '$2.00')
        self.assertEqual(self.itemsPage.return_cart_total(), '$132.00')
        self.assertEqual(self.itemsPage.return_product_name(), 'Printed Dress')

    def test_comprar_vestido_por_orden(self):
        self.functionItemsPage.click_en_dress()
        self.itemsPage.select_by_value('reference:asc')
        self.functionItemsPage.click_en_list_icon()
        self.functionItemsPage.click_en_segundo_vestido()
        self.assertEqual(self.itemsPage.return_total_productos(), '$50.99')
        self.assertEqual(self.itemsPage.return_total_shipping(), '$2.00')
        self.assertEqual(self.itemsPage.return_cart_total(), '$52.99')
        self.assertEqual(self.itemsPage.return_product_name(), 'Printed Dress')

    def test_dresses_options(self):
        self.indexPage.click_dresses()
        self.itemsPage.click_checkbox(2)
        self.itemsPage.click_checkbox(4)
        self.itemsPage.click_colors(2)
        time.sleep(4)


    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':

    unittest.main()