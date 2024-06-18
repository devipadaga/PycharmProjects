from pages.BasePage import BasePage
from selenium.webdriver.common.by import By

class RegPage(BasePage):

    FIRSTNAME = (By.NAME, "firstname")
    MIDDLENAME = (By.NAME, "middlename")
    LASTNAME = (By.NAME, "lastname")
    COARSE = (By.XPATH, "//select")
    GENDER = (By.XPATH, "//input[@name='male']")
    MobileNum = (By.XPATH, "//input[@name='phone']")
    ADDRESS = (By.XPATH, "//textarea[@value='address']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PASSWORD = (By.XPATH, "//input[@id='pass']")
    RETYPE_PWD = (By.XPATH, "//input[@id='repass']")
    SUBMIT = (By.XPATH, "//input[@value='Submit']")

    # driver: webdriver

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def navigate_REGPAGE_url(self):
        self.driver.get("C://Users//SPURGE//Desktop//Html%20Files//RegPage.html")

    def fill_firstname_middlename_and_lastname(self, firstname, middlename, lastname):
        self.enter_text(self.FIRSTNAME, firstname)
        self.enter_text(self.MIDDLENAME, middlename)
        self.enter_text(self.LASTNAME, lastname)

    def select_gender(self):
        self.click_on(self.GENDER)

    def enter_all_inputFields(self, mobilenum, address, email, password, retypePWD):
        self.enter_text(self.MobileNum, mobilenum)
        self.enter_text(self.ADDRESS, address)
        self.enter_text(self.EMAIL, email)
        self.enter_text(self.PASSWORD, password)
        self.enter_text(self.RETYPE_PWD, retypePWD)

    def click_Submit(self):
        self.click_on(self.SUBMIT)
