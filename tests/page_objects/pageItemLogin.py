from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class PageItemLogin():

    def __init__(self, driver):
        self.driver = driver
        self.mail_input = (By.NAME, 'email')
        self.pswrd_input = (By.NAME, 'passwd')
        self.login_button = (By.ID, 'SubmitLogin')
        self.return_error_banner = (By.XPATH, '//*[@id="center_column"]/div[1]/ol/li')

    def return_banner_text(self):
        return_error_banner_text = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.return_error_banner))
        return return_error_banner_text.text
