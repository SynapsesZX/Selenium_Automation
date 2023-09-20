from selenium.webdriver.common.by import By

LOGIN = (By.CSS_SELECTOR, '.header_sectionTwo__10AW3 a')
USERNAME_INPUT_FIELD = (By.XPATH, '(//input[@id="signInFormUsername"])[2]')
PASSWORD_INPUT_FIELD = (By.XPATH, '(//input[@id="signInFormPassword"])[2]')
SUBMIT_BUTTON = (By.XPATH, '(//input[@name="signInSubmitButton"])[2]')
LOGIN_WINDOW = (By.CSS_SELECTOR,'[class*=visible-sm]')
