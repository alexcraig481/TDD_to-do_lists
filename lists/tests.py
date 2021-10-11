# Create your unit tests here.import - augmented version of unittest.TestCase
# with some Django-specific features

from django.urls import resolve
from django.test import TestCase
from lists.views import home_page



class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        # Resolve is function Dj uses internally to resolve URLs with the right
        # view function via mapping
        #
        # Can we resolve the URL for the root of the site to a particular
        # view function we've made?
        found = resolve('/')
        self.assertEqual(found.func, home_page)
