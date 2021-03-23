import unittest
from selenium import webdriver
from TiendaDeRopa.tests.page_objects.pageItemFunction import PageItemsFunction
from TiendaDeRopa.tests.page_objects.pageFunctionLogin import PageFunctionLogin
from TiendaDeRopa.tests.page_objects.pageItemLogin import PageItemLogin
import time


class LoginCases(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get('http://automationpractice.com/index.php')
        self.functionItemsPage = PageItemsFunction(self.driver)
        self.functionLoginPage = PageFunctionLogin(self.driver)
        self.itemPageLogin = PageItemLogin(self.driver)


    def test_login_formato_negativo(self):
        self.functionItemsPage.click_en_sign_in()
        self.functionLoginPage.llenar_mail('3213-@@om.com.')
        time.sleep(5)
        self.functionLoginPage.llenar_pswrd('a-a-a-a-a-a-a')
        self.functionLoginPage.click_login()
        self.assertEqual(self.itemPageLogin.return_banner_text(), 'Invalid email address.')

    def test_login_cuenta_inexistente(self):
        self.functionItemsPage.click_en_sign_in()
        self.functionLoginPage.llenar_mail('xmatiasp@gmail.com')
        self.functionLoginPage.llenar_pswrd('123456')
        self.functionLoginPage.click_login()
        self.assertEqual(self.itemPageLogin.return_banner_text(), 'Authentication failed.')


    def tearDown(self):
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':

    unittest.main()