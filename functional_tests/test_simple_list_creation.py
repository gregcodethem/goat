# First testing script from TDD with Python book

from .base import FunctionalTest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_for_one_user(self):
        # Bob goes to look at webpage
        self.browser.get(self.live_server_url)

        # He notices the page title and header mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He's invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
            inputbox.get_attribute('placeholder'), 'Enter a to-do item'
        )

        # He types "Buy feathers" into a text box.
        inputbox.send_keys('Buy feathers')
        # When he hits enter, the page updates, and now the page lists
        #"1: Buy feathers" as an item in a to-do list.
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy feathers')

        # There is still a text box inviting him to add another item.
        # He enters: "Use feathers to make a fly"
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Use feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items in his list.
        self.wait_for_row_in_list_table('1: Buy feathers')
        self.wait_for_row_in_list_table('2: Use feathers to make a fly')

        # satisfied, he goes back to sleep.

    def test_multiple_users_can_start_lists_at_different_urls(self):

        # Bob starts a new to-do list
        self.browser.get(self.live_server_url)
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy feathers')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy feathers')

        # He notices that his list has a unique URL
        bob_list_url = self.browser.current_url
        self.assertRegex(bob_list_url, '/lists/.+')

        # Now a new user, Francesca, comes along to the site.

        # We use a new browser session to make sure
        # that no information of Bob's is coming through
        # from cookies etc.
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francesca visits the home page.  There is no
        # sign of Bob's list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francesca starts a new list by entering
        # a new item.
        inputbox = self.get_item_input_box()
        inputbox.send_keys('Buy Ostrich milk')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy Ostrich milk')

        # Francesca gets her own unique URL
        francesca_list_url = self.browser.current_url
        self.assertRegex(francesca_list_url, '/lists/.+')
        self.assertNotEqual(francesca_list_url, bob_list_url)

        # Again there is no trace of Bob's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy feathers', page_text)
        self.assertIn('Buy Ostrich milk', page_text)

        # satisfied, they both go back to sleep

