from django.test import TestCase

# Create your unit tests here.import - augmented version of unittest.TestCase
# with some Django-specific features

class Smoketest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 3)
