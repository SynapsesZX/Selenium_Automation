from selenium.webdriver.common.by import By

REG_ICON = (By.CSS_SELECTOR, ".header-actions__item--user button")
REG_BUTTON = (By.CSS_SELECTOR, "div .auth-modal__register-link")
USERNAME_INPUT_FIELD = (By.ID, 'registerUserName')
SURNAME_INPUT_FIELD = (By.ID, 'registerUserSurname')
USER_PHONE_INPUT_FIELD = (By.ID, 'registerUserPhone')
USER_EMAIL_INPUT_FIELD = (By.ID, 'registerUserEmail')
USER_PASSWORD_INPUT_FIELD = (By.ID, 'registerUserPassword')
REGISTRATION_LABEL = (By.CSS_SELECTOR, '.modal__header .modal__heading')
REGISTER_NAME_LABEL = (By.CSS_SELECTOR, '[for="registerUserName"]')
REGISTER_SURNAME_LABEL = (By.CSS_SELECTOR, '[for="registerUserSurname"]')
REGISTER_USER_PHONE_LABEL = (By.CSS_SELECTOR, '[for="registerUserPhone"]')
REGISTER_USER_EMAIL_LABEL = (By.CSS_SELECTOR, '[for="registerUserEmail"]')
REGISTER_USER_PASSWORD_LABEL = (By.CSS_SELECTOR, '[for="registerUserPassword"]')
SOCIAL_LABEL = (By.CSS_SELECTOR,'p.auth-modal__social-label')
HIDER_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.form__toggle-password')
USER_FORM_CAPTION = (By.CSS_SELECTOR, '.js-user-agreement .form__caption')
PERSONAL_DATA_LINK = (By.CSS_SELECTOR, '.js-user-agreement .form__caption .button_type_link')
PRIVACY_LINK = (By.CSS_SELECTOR, '.js-user-agreement .form__caption .button--link')
REGISTER_BUTTON = (By.CSS_SELECTOR, '[type="submit"]')
REGISTERED_BUTTON = (By.CSS_SELECTOR, 'button.auth-modal__register-link')
MODAL_DIVIDER = (By.CSS_SELECTOR,'span.auth-modal__divider')
FACEBOOK_BUTTON = (By.CSS_SELECTOR,'button.auth-modal__social-button_type_facebook')
GOOGLE_BUTTON = (By.XPATH,'//button[@class="button button--large button--gray button--with-icon auth-modal__social-button"] ')
CLOSE_BUTTON = (By.CSS_SELECTOR,'button.modal__close')
VACANCY_BUTTON = (By.CSS_SELECTOR,'div .filter-vacancies__show')