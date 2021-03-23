from TiendaDeRopa.tests.page_objects.pageItemLogin import PageItemLogin


class PageFunctionLogin():

    def __init__(self, driver):
        self.driver = driver
        self.itemsPageLogin = PageItemLogin(self.driver)

    def llenar_mail(self, keys):
        self.driver.find_element(*self.itemsPageLogin.mail_input).send_keys(keys)

    def llenar_pswrd(self, keys):
        self.driver.find_element(*self.itemsPageLogin.pswrd_input).send_keys(keys)

    def click_login(self):
        self.driver.find_element(*self.itemsPageLogin.login_button).click()