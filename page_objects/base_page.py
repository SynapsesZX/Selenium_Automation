import time
import random
from selenium.webdriver.common.keys import Keys
from random import randint
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.color import Color

EXPLICITLY_WAIT_TIMEOUT = 5


class BasePage:
    """
    Class with Base methods
    """

    def __init__(self, driver, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        BasePage constructor
        :param driver: driver instance
        :param timeout: an argument that indicates how long to wait
        """
        self.driver = driver
        self.driver.implicitly_wait(timeout)

    def is_element_present(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method of checking that an element isn't present
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        :return:  bool. return True if the element is present else it will return False
        """
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

    def wait_and_click(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to wait until button be clickable and click it
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))
        element.click()

    def wait_until_element_will_be_clickable(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to wait until button be clickable and click it
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((how, what)))

    def wait_until_element_will_be_visible(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to wait until button be clickable and click it
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))

    def get_element_text(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get text of the element
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element_text = self.driver.find_element(how, what).text
        return element_text

    def check_element_text(self, how, what, text, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get text of the element
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        :param text: value to assert the text
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element_text = self.driver.find_element(how, what).text
        if element_text == text:
            pass
        else:
            raise Exception("the element text is not the same as value")

    def check_if_element_selected(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get check if element is selected
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        if element.is_selected():
            pass
        else:
            raise Exception('element is not selected')

    def check_if_element_not_selected(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get check if element is selected
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how long to wait
        """

        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        if element.is_selected():
            raise Exception("Element should not be selected")
        else:
            pass

    def check_if_elements_selected(self, how, what, value, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to get check if element from list is selected
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param value an argument that indicated what value you want to select from list (selector int )
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located((how, what)))
        element[value].click()
        element[value].is_selected()

    def send_text_to_element(self, how, what, text, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to send text to elements
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param text: an argument that indicates by what text search element (string)
        :param timeout: an argument that indicates how long to wait
        """
        element = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element.send_keys(text)

    def check_element_attribute(self, how, what, attribute, attribute_result, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        Basic method to send text to elements
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param attribute: an argument that indicates by what property you want to select (selector,string)
        :param attribute_result: an argument that indicates by what result you want to assert ( int,string )
        :param timeout: an argument that indicates how long to wait
        """
        step = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        prop = step.get_attribute(attribute)
        assert prop == attribute_result

    def get_element_attribute(self, how, what, attribute):
        """
        Basic method to send text to elements
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param property_value: an argument that indicates by what attribute you want to select (selector,string)

        """
        element = self.driver.find_element(how, what).get_attribute(attribute)
        return element

    def open_link(self, link):
        """
        Basic method to open the link
        :param link: an argument that indicates what link you want to open (URL = string)
        """
        self.driver.get(url=link)

    # Random Generators #
    def randomWord(value):
        """
            Basic method to add random text to elements
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        consonants = "abcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value))

        # функция на рандомные имена кирилица

    def randomWord_rus(value):
        """
            Basic method to add random text to elements ( ru )
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        consonants = "абгдеёжзийклмнопрстуфхцчшщыьэюя"
        vowels = "абгдеёжзийклмнопрстуфхцчшщыьэюя"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value))

        # функция на лучшие пароли

    def randomWord_passwords(value):
        """
            Basic method to add random password to elements
            :param value: an argument that indicates how much characters you want to add (integer)

         """
        consonants = "ABCDIFGKGIFOGJFLGOOOfgfgfgfgferytyijyyuyyyyy1234567890"
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value))

        # функция на рандомные почты

    def randomWord_mails(value):
        """
            Basic method to add random email to elements
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        consonants = "abcdfghjklmnpqrstvwxyz"
        email = '@gmail.com'
        vowels = "aeiou"
        return "".join(random.choice((consonants, vowels)[i % 2]) for i in range(value)) + email

        # функция на рандомные телефоны

    def random_with_N_digits(value):
        """
            Basic method to add random numbers to elements
            :param value: an argument that indicates how much characters you want to add (integer)

        """
        range_start = 10 ** (value - 1)
        range_end = (10 ** value) - 1
        return randint(range_start, range_end)

    def check_url_march(self, url):
        """
        Basic method to check if there is not element
        :param url: an argument is required for checking the url ( url )
       """
        assert url == self.driver.current_url

    def is_element_no_present_DOM(self, how, what):
        """
           Basic method to check if there is not element
           :param how: an argument that indicates how to search (css, id, xpath и i.e.)
           :param what: an argument that indicates what to search for (selector string)

        """

        element = self.driver.find_element(how, what)
        if element.is_displayed():
            raise Exception("Element should not be found")
        else:
            pass

    def is_element_no_present_with_wait(self, how, what):
        try:
            WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((how, what)))
            not_found = False
        except:
            not_found = True

        assert not_found, ("The element is displayed")

    def drag_and_drop(self, how_drag, what_drag, what_drop, to_drop):
        """
            Basic method to check if there is not element
            :param how_drag: an argument that indicates how to search (css, id, xpath и i.e.) and what we want to click and hold
            :param what_drag: an argument that indicates what to search for (selector string)  and what we want to click and hold
            :param what_drop: an argument that indicates how to search (css, id, xpath и i.e.) and to what element we want to drop
            :param to_drop: an argument that indicates what to search for (selector string)  and to what element we want to drop
        """
        element_to_drug = self.driver.find_element(how_drag, what_drag)
        element_to_drop = self.driver.find_element(what_drop, to_drop)
        ActionChains(self.driver).click_and_hold(element_to_drug).move_to_element(element_to_drop).perform()

    def check_css_style(self, how, what, css, css_result):

        """
            Basic method to check the locator css styles
            :param how: an argument that indicates how to search (css, id, xpath и i.e.)
            :param what: an argument that indicates what to search for (selector string)
            :param css: an argument that indicates what css style of locator you want to select (css locator value)
            :param css_result: an argument that indicates by what css param of locator you want to assert ( css locator int,string )
            """

        element = self.driver.find_element(how, what)
        prop = element.value_of_css_property(css)
        assert prop == css_result

    def multiple_click(self, x_value, y_value, how, what):
        """
                   Basic method to click on the same element multiple times
                   :param how: an argument that indicates how to search (css, id, xpath и i.e.)
                   :param what: an argument that indicates what to search for (selector string)
                   :param x_value: an argument for while loop ( by default should be = 0, int )
                   :param y_value: an argument for while loop ( y = the times how much we want to click , int )
                   """

        x = x_value
        y = y_value
        while x < y:
            try:
                run_test = WebDriverWait(self.driver, 160).until( \
                    EC.presence_of_element_located((how, what)))
                run_test.click()
                x += 1
                time.sleep(2)
            except StaleElementReferenceException as e:
                raise e

    def switch_to_window(self, value):
        """
                           Basic method to select on what window you want to switch
                           :param value: an argument that indicates the number of window to switch ( int )

                           """
        window = self.driver.window_handles[value]
        self.driver.switch_to_window(window)

    def select_element_from_list(self, how, what, value):
        """
                Basic method to click the element from list
                :param how: an argument that indicates how to search (css, id, xpath и i.e.)
                :param what: an argument that indicates what to search for (selector string)
                :param value: an argument that indicates on which element from list you want to click ( value = int )
                """
        element = self.driver.find_elements(how, what, )
        element[value].click()

    def select_element_from_drop_down_list(self, how_select_container, what_select_container, how, what, value):
        """
        Basic method to click the element from list :param how_select_container: an argument that indicates how to
        search the click container with list (css, id, xpath и i.e.) :param what_select_container: an argument that
        indicates how to search the click container with list (css, id, xpath и i.e.) :param how: an argument that
        indicates how to search (css, id, xpath и i.e.) :param what: an argument that indicates what to search for (
        selector string) :param value: an argument that indicates on which element from list you want to click (
        value = int )
        """
        drop_down_container = self.driver.find_element(how_select_container, what_select_container, )
        drop_down_container.click()
        drop_down_container = self.driver.find_elements(how, what, )
        drop_down_container[value].click()
        drop_down_container = self.driver.find_element(how_select_container, what_select_container, )
        drop_down_container.click()

    def is_disappeared(self, how, what, timeout=4):
        """
        Basic method to wait when element disappears :param how_select_container: an argument that indicates how to
        search the click container with list (css, id, xpath и i.e.) :param what_select_container: an argument that
        indicates how to search the click container with list (css, id, xpath и i.e.) :param how: an argument that
        indicates how to search (css, id, xpath и i.e.) :param what: an argument that indicates what to search for (
        selector string) :param timeout: an argument that indicates how much time you want to wait )
        """
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def alert_accept(self):
        """
                        Basic method to accept the alert

                        """
        alert = self.driver.switch_to.alert
        alert.accept()

    def alert_dismiss(self):
        """
                         Basic method to dismiss the alert window

                        """
        alert = self.driver.switch_to.alert
        alert.dismiss()

    def alert_send_keys_and_accept(self, text):
        """
                        Basic method to accept the alert

                        """
        alert = self.driver.switch_to.alert
        alert.send_keys(text)
        alert.accept()

    def js_click(self, how, what):
        """
        Basic method for click by JS script
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        """
        element = self.driver.find_element(how, what)
        self.driver.execute_script("arguments[0].click();", element)

    def upload_the_file(self, how, what, file_part):
        """
        Basic method for upload the file
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        """
        self.driver.find_element(how, what, ).send_keys(file_part)

    def clear_input_field(self, how, what):
        """
        Basic method for clearing the input fields
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        """
        self.driver.find_element(how, what, ).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(how, what, ).send_keys(Keys.DELETE)

    def is_element_enabled(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
               Basic method for clearing checking the if element is enabled
               :param how: an argument that indicates how to search (css, id, xpath и i.e.)
               :param what: an argument that indicates what to search for (selector string)
        """
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        if element.is_enabled():
            pass
        else:
            raise Exception("Element should be enabled")

    def is_element_not_enabled(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
            Basic method for clearing checking the if element isn't enabled
            :param how: an argument that indicates how to search (css, id, xpath и i.e.)
            :param what: an argument that indicates what to search for (selector string)
        """
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        if element.is_enabled():
            raise Exception("Element should not be enabled")
        else:
            pass

    def back_to_previous_page(self):
        """
        Basic method for clicking Back button in browser
        """
        self.driver.back()

    def forward_to_previous_page(self):
        """
        Basic method for clicking forward button in browser
        """
        self.driver.forward()

    def get_css_color(self, how, what, css, hex_code_for_assert):
        colour = self.driver.find_element(how, what).value_of_css_property(css)
        result = Color.from_string(colour).hex
        assert result == hex_code_for_assert

    def refresh_page(self):
        self.driver.refresh()

    def check_input_field_empty_state(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT, ):
        """
            Basic method for clearing checking the if element isn't enabled
            :param how: an argument that indicates how to search (css, id, xpath и i.e.)
            :param what: an argument that indicates what to search for (selector string)
            :param timeout: an argument that indicates how much time you want to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element_text = self.driver.find_element(how, what).text
        if len(element_text) == 0:
            pass
        else:
            raise Exception('input field is not empty')

    def check_element_is_displayed_ui(self, how, what, timeout=EXPLICITLY_WAIT_TIMEOUT):
        """
        :param how: an argument that indicates how to search (css, id, xpath и i.e.)
        :param what: an argument that indicates what to search for (selector string)
        :param timeout: an argument that indicates how much time you want to wait
        """
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((how, what)))
        element = self.driver.find_element(how, what)
        if element.is_displayed():
            pass
        else:
            raise Exception('element not displayed in UI')
        return element
