from page_objects.base_page import BasePage
import api.api_body, api.application_detail_page
import globals.info
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import globals
import pytest
import requests
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture()
def driver(request):
    """
    Fixture for browser selection and browser launching
    """
    print("\nstart browser for test..")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = Options()
        options.add_argument('--no-sandbox')
        # options.add_argument("--disable-gpu")
        # options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument("--incognito")
        driver = webdriver.Chrome(service=service, options=options)
        driver.implicitly_wait(5)



    elif browser_name == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = FirefoxOptions()
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-gpu")
        options.add_argument("--headless")
        options.add_argument("window-size=1920,1080")
        options.add_argument("--incognito")
        driver = webdriver.Firefox(service=service, options=options)
        driver.implicitly_wait(5)

    else:
        print(f"Browser <browser_name> is still not implemented")
    yield driver
    #   if sys.exc_info():
    #       now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    #       driver.get_screenshot_as_file('Screenshots\screenshot-%s.png' % now)
    #      allure.attach(driver.save_screenshot('screenie.png'), name="Screenshot", attachment_type=AttachmentType.PNG)
    allure.attach(driver.get_screenshot_as_png(), attachment_type=allure.attachment_type.PNG)
    allure.attach(body=str(driver.get_log('browser')), name="Console out from browser",
                  attachment_type=allure.attachment_type.HTML)
    print("\nquit browser..")
    driver.quit()


@pytest.fixture()
def api_setup_created_status():
    app_name = BasePage.randomWord(value=15)
    request = requests.post('https://qa-h360-marketplace.softservetest.com/api/applications',
                            json=api.api_body.create_app_body(app_name=app_name), headers=globals.info.bearer)
    response_body = request.json()
    assert response_body['data']['name'] == app_name
    app_id = response_body['data']['id']
    yield app_id
    request = requests.delete(
        f"https://qa-h360-marketplace.softservetest.com/api/applications/{app_id}",
        headers=globals.info.bearer)
    return request


@pytest.fixture()
def api_setup_with_in_progress_status(api_setup_created_status):
    print(api_setup_created_status)

    requests.post(
        f'https://qa-h360-marketplace.softservetest.com/api/applications/{api_setup_created_status}/tech-details',
        json=api.api_body.app_in_progress_body(), headers=globals.info.bearer)
    requests.post(
        f"https://qa-h360-marketplace.softservetest.com/api/applications/{api_setup_created_status}/description",
        headers=globals.info.bearer, json=api.api_body.app_in_progress_description_body())
    yield api_setup_created_status


@pytest.fixture()
def api_setup_with_in_review_status(api_setup_with_in_progress_status):
    requests.patch(
        f'https://qa-h360-marketplace.softservetest.com/api/applications/{api_setup_with_in_progress_status}/change-status',
        json=api.api_body.app_in_review_body(), headers=globals.info.bearer)

    yield api_setup_with_in_progress_status


@pytest.fixture()
def api_setup_with_approved_status(api_setup_with_in_review_status):
    requests.patch(
        f'https://qa-h360-marketplace.softservetest.com/api/applications/{api_setup_with_in_review_status}/change-status',
        json=api.api_body.app_approved_body(), headers=globals.info.admin_bearer)

    yield api_setup_with_in_review_status


@pytest.fixture()
def api_setup_partner_with_active_status():
    request = requests.post(' https://b08cbmkhu1.execute-api.us-west-2.amazonaws.com/api/partners',
                            json=api.api_body.partner_body(), headers=globals.info.admin_bearer)
    response_body = request.json()
    partner_id = response_body['data']['id']
    yield partner_id
