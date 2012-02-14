from time import sleep

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from splinter.browser import Browser
from tests.base import BaseBrowserTests
from fake_webapp import EXAMPLE_APP

class ZombieTest(BaseBrowserTests, unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser('zombie')
        sleep(0.5)

    def setUp(self):
        self.browser.visit(EXAMPLE_APP)
