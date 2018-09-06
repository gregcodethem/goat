# First testing script from TDD with Python book

from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Bob goes to look at webpage
        self.browser.get('http://localhost:8000')

        # He notices the page title mentions to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail("Finish the test!")

        # He's invited to enter a to-do item straight away

        # He types "Buy feathers" into a text box.

        # When he hits enter, the page updates, and now the page lists
        #"1: Buy feathers" as an item in a to-do list.

        # There is still a text box inviting him to add another item.
        # He enters: "Use feathers to make a fly"

        # The page updates again, and now shows both items in his list.

        # Bobh wonders whether the site will remember his list.
        # Then he sees that the site has generated a unique URL
        # for him -- there is some explanatory text to that
        # effect.

        # He visits that URL - his to-do list is still there.

        # satisfied, he goes back to sleep.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
