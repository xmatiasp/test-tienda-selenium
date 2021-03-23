from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time


class PageItemsFunction:

    def __init__(self, mi_driver):
        self.driver = mi_driver
        self.input_box = (By.ID, 'quantity_wanted')
        self.icon_plus = (By.CLASS_NAME, 'icon-plus')
        self.t_shirt_card = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')
        self.dresses_button = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[2]/a')
        self.t_shirt_button = (By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
        self.orange_color = (By.ID, 'color_13')
        self.select_vestido_casual = (By.XPATH, '//*[@id="subcategories"]/ul/li[1]/div[1]/a/img')
        self.vestido_casual_card = (By.XPATH, '//*[@id="center_column"]/ul/li/div/div[2]/h5/a')
        self.add_to_cart_button = (By.XPATH, '//*[@id="add_to_cart"]/button/span')
        self.icon_list_button = (By.CLASS_NAME, 'icon-th-list')
        self.second_dress_card = (By.XPATH, '//*[@id="center_column"]/ul/li[2]/div/div/div[3]/div/div[2]/a[1]/span')
        self.sign_in_button = (By.CLASS_NAME, 'login')


    def hacer_click_by_xpath(self, elemento_by_xpath,cantidad_clicks):
        for clicks in range(cantidad_clicks):
            self.driver.find_element_by_xpath(elemento_by_xpath)

    def introducir_cantidad(self, cantidad):
        self.driver.find_element(*self.input_box).clear()
        self.driver.find_element(*self.input_box).send_keys(cantidad)

    def clickear_mas(self, clicks):
        for n in range(clicks):
            self.driver.find_element(*self.icon_plus).click()


    def color_change(self):
        self.driver.find_element(*self.t_shirt_card).click()
        self.driver.find_element(*self.orange_color).click()

    def click_en_dress(self):
        self.driver.find_element(*self.dresses_button).click()

    def click_en_t_shirt(self):
        self.driver.find_element(*self.t_shirt_button).click()

    def comprar_vestido_casual(self):
        self.driver.find_element(*self.select_vestido_casual).click()
        self.driver.find_element(*self.vestido_casual_card).click()

    def agregar_vestidos(self, clicks):
        for n in range(clicks):
            self.driver.find_element(*self.icon_plus).click()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()

    def click_en_list_icon(self):
        self.driver.find_element(*self.icon_list_button).click()

    def click_en_segundo_vestido(self):
        self.driver.find_element(*self.second_dress_card).click()

    def click_en_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()