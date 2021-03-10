from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class PageItems:

    def __init__(self, my_driver):
        self.no_results_banner = (By.XPATH, '//*[@id="center_column"]/p')
        self.title_banner = (By.XPATH, '//*[@id="center_column"]/h1/span[1]')
        self.driver = my_driver
        self.input_box = (By.ID, 'quantity_wanted')
        self.order = (By.ID, 'selectProductSort')
        self.input_select_talle = (By.NAME, 'group_1')

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