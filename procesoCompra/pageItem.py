class PageItems:
    def __init__(self, mi_driver):
        self.driver = mi_driver

    def hacer_click_by_xpath(self, elemento_by_xpath,cantidad_clicks):
        for clicks in range(cantidad_clicks):
            self.driver.find_element_by_xpath(elemento_by_xpath).click()