from TiendaDeRopa.tests.page_objects.pageItemLogin import PageItemLogin
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageFunctionLogin():

    def __init__(self, driver):
        self.driver = driver
        self.itemsPageLogin = PageItemLogin(self.driver)

    def llenar_mail(self, keys):
        llenar_mail = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.itemsPageLogin.mail_input))
        llenar_mail.send_keys(keys)
        #self.driver.find_element(*self.itemsPageLogin.mail_input).send_keys(keys)

    def llenar_pswrd(self, keys):
        self.driver.find_element(*self.itemsPageLogin.pswrd_input).send_keys(keys)

    def click_login(self):
        self.driver.find_element(*self.itemsPageLogin.login_button).click()