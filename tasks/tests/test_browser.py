from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class SeleniumTest(StaticLiveServerTestCase):
    """
    Test View class
    """
    browser = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--window-size=1420,1080')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    # Browser Integration testing with Selenium
    def test_homepage_title(self):
        """
        Simple test to check the correct loading of home page
        """
        self.browser.get('%s%s' % (self.live_server_url, '/'))
        self.assertIn('TDD', self.browser.title)

    def test_create_task(self):
        """
        Simple test to check the correct constructing of new tasks
        """
        self.browser.get('%s%s' % (self.live_server_url, '/'))
        add_button = self.browser.find_element_by_link_text('add_task')
        add_button.click()

        # store the number of tasks
        carts = self.browser.find_elements_by_class_name('card-body in-list')
        old_num = len(carts)

        # enter title
        title_input = self.browser.find_element_by_name('task_title')
        title_input.send_keys('test title from selenium')

        # enter description
        desc_input = self.browser.find_element_by_name('task_description')
        desc_input.send_keys('test description from selenium')

        # click on create task button
        create_btn = self.browser.find_element_by_tag_name('button[type="submit"]')
        create_btn.click()

        carts = self.browser.find_elements_by_class_name('card-body')
        new_num = len(carts)

        self.assertEqual(new_num, old_num + 1)
