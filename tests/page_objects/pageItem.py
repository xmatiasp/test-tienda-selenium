from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class PageItems:

    def __init__(self, my_driver):
        self.no_results_banner = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.driver = my_driver
        self.input_box = (By.ID, 'quantity_wanted')
        self.order = (By.ID, 'selectProductSort')
        self.input_select_talle = (By.NAME, 'group_1')
        self.cantidad_productos = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/h2/span[1]')
        self.total_products = (By.CLASS_NAME, 'ajax_block_products_total')
        self.total_shipping = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[2]/span')
        self.cart_total = (By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[3]/span')
        self.product_name = (By.ID, 'layer_cart_product_title')
        self.checkbox = (By.CLASS_NAME, 'checkbox')
        self.color_check = (By.CLASS_NAME, 'color-option  ')

    def return_no_element_text(self):
        return self.driver.find_element(*self.no_results_banner).text

    def return_section_title(self):
        return self.driver.find_element(*self.title_banner).text

    def select_by_text(self, text):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_visible_text(text)

    def select_by_value(self, value):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_value(value)

    def select_by_index(self, number):
        order = Select(self.driver.find_element(*self.order))
        order.select_by_index(number)

    def select_talle(self, talle):
        select = Select(self.driver.find_element(*self.input_select_talle))
        select.select_by_visible_text(talle)

    def return_cantidad(self):
        return self.driver.find_element(*self.input_box).get_attribute('value')

    def return_cantidad_productos(self):
        return_cantidad_productos = WebDriverWait(self.driver, 7).until(EC.text_to_be_present_in_element(self.cantidad_productos))
        return return_cantidad_productos.text

    def return_total_productos(self):
        return_total_productos = WebDriverWait(self.driver, 7).until(EC.visibility_of_element_located(self.total_products))
        return return_total_productos.text

    def return_total_shipping(self):
        return_total_shipping = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.total_shipping))
        return return_total_shipping.text

    def return_cart_total(self):
        return_cart_total = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.cart_total))
        return return_cart_total.text

    def return_product_name(self):
        return_product_name = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.product_name))
        return return_product_name.text

    def click_checkbox(self, number):
        self.driver.find_elements(*self.checkbox)[number].click()

    def click_colors(self,number):
        self.driver.find_elements(*self.color_check)[number].click()