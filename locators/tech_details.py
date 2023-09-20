from selenium.webdriver.common.by import By

EDIT_ICON = (By.CLASS_NAME, 'svg.tech-details-form_editIcon__GgwUH')

APP_LIST = (By.CSS_SELECTOR,'[class="app-list_table_container__2NAr-"]')
MOBILE_NATIVE = (By.ID, 'MOBILE')
WEB = (By.ID, 'WEB')
DESKTOP = (By.ID, 'DESKTOP')
RUN_INSIDE_PATIENT_CHART = (By.ID, 'RUN_INSIDE_PATIENT_CHART')
RUN_OUTSIDE_OF_PATIENT_CHART = (By.ID, 'RUN_OUTSIDE_OF_PATIENT_CHART')
BACKEND_SERVICE = (By.ID, 'BACKEND_SERVICE')
AUTHENTICATION_TYPE_DIV = (By.CLASS_NAME, '.tech-details-form_authTypeWrapper__qdjgD')
AUTHENTICATION_TYPE_PUBLIC = (By.ID, 'auth_type_public')
AUTHENTICATION_TYPE_CONFIDENTIAL = (By.ID, 'auth_type_confidential')
LAUNCH_CONTEXT_TYPE_DIV = (By.CLASS_NAME, 'tech-details-form_launchContextTitleWrapper__3Zz0S')
LAUNCH_CONTEXT_TYPE_PATIENT = (By.ID, 'launch_context_patient')
LAUNCH_CONTEXT_TYPE_ENCOUNTER = (By.ID, 'launch_context_encounter')
TOKEN_INTROSPECTION_DIV = (By.CLASS_NAME, 'tech-details-form_tokenIntrospectionWrapper__BaHc8')
TOKEN_INTROSPECTION_ONLINE = (By.ID, 'token_introspection_online')
TOKEN_INTROSPECTION_OFFLINE = (By.ID, 'token_introspection_offline')
PATIENT_INDIVIDUAL_SCOPE_BUTTON = (By.ID, 'patient_individual')
PATIENT_POPULATION_SCOPE_BUTTON = (By.ID, 'patient_population')
SCOPE_CHECKBOXES_ENABLED = (
By.CSS_SELECTOR, '[class="tech-details-form_scopesContainer__2Wrel"] [class="p-checkbox p-component"]')
SCOPE_CHECKBOXES_DISABLED = (By.XPATH, '//div[@class="p-checkbox p-component p-checkbox-disabled"]')
SMART_LAUNCH_URL_INPUT_FIELD = (By.ID, 'development_smart_launch_url')
REDIRECT_URI_INPUT_FIELD = (By.ID, 'development_redirect_uri')
CLIENT_ID_INPUT_FIELD = (By.ID, 'client_id')
CANCEL_BUTTON = (By.XPATH, '(//button[@class="p-button p-component"])[1]')
SAVE_BUTTON = (By.CSS_SELECTOR, '[class="tech-details-form_footerButtons__3QqdK"] [class*="button_primary__2-Qrd"] ')
SCOPE_LIST = (By.CSS_SELECTOR, "[class='scopes-item_scopesListItem__3B3kf']")
VERSION_DROP_DOWN = (By.CSS_SELECTOR, '[class*="dropdown_dropdown__1GI1I"]')
DROP_DOWN_LIST = (By.CSS_SELECTOR, 'ul[class*="p-dropdown-items"] > li')