"""
    Unit Test file for views
"""
from django.test import TestCase

from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from pyvirtualdisplay import Display

from pydjango_ci_integration.settings import SITE_URL


class TaskListViewTest(TestCase):
    """
    Test View class
    """
    # Browser Integration testing with Selenium
    def test_chrome_site_homepage(self):
        # display = Display(visible=0, size=(800, 800))
        # display.start()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(chrome_options=chrome_options)
        
        # browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

        browser.get(SITE_URL)
        self.assertIn('Semaphore', browser.title)
        browser.close()
