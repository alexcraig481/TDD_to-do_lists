# Functional tests aka Acceptance tests aka End-to-End Test /Black Box:
# Lets us see how the application functions from the
# user's POV in a real browser (thanks to Selenium)
#
# They track user stories - follows how a user might work with a particular
# feature and how the app should respond to them

from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
    def tearDown(self):
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        # User goes to webpage to check out application
        self.browser.get("http://localhost:8000")

        # She notices the page title and header mention to do list
        self.assertIn("To-Do", self.browser.title)
        self.fail("Finish the test!")

 # She can start a to do list straight away

 # She types "Buy peakcock feathers" into a text Box

 # When she hits enter, the page updates, and now the page lists
 # "1: Buy peakcock feathers" as an item in a to-do lists

 # There is still a text box inviting her to add another item. she
 # enters "Use peakcock feathers to make a fly"

 # She presses enter. The page updates again, now showing both items

 # User doesn't know if site will save list. She sees that the site
 # has generated a unique URL for her -- there is some explanatory text to that
 # effect

 # She visits that URL - to-dolist is still There

 # She is satisfied

if __name__ == "__main__":
    unittest.main()
