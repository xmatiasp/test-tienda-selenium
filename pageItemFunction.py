from selenium.webdriver.common.by import By


class PageItemsFunction:

    def __init__(self, mi_driver):
        self.driver = mi_driver
        self.input_box = (By.ID, 'quantity_wanted')
        self.orange_color = (By.ID, 'color_1')

    def hacer_click_by_xpath(self, elemento_by_xpath,cantidad_clicks):
        for clicks in range(cantidad_clicks):
            self.driver.find_element_by_xpath(elemento_by_xpath).click()

    def introducir_cantidad(self, cantidad):
        self.driver.find_element(*self.input_box).clear()
        self.driver.find_element(*self.input_box).send_keys(cantidad)

    def color_change(self):
        self.driver.find_element(*self.orange_color).click()


    def obtener_numero_Input(self):
        return self.driver.find_element_by_id("quantity_wanted").get_attribute("value")