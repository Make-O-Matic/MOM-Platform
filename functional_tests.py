# Copyright (c) 2016-2017 Enproduktion GmbH & Laber's Lab e.U. (FN 394440i, Austria)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import unittest

class IndexTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get('http://localhost:5000/')

    def tearDown(self):
        self.browser.quit()

    def test_index_page_logged_out_nothing_selected(self):
        """
         Functional Test for index page when logged out.
        """

        """
        Little Tommi looks up the new kid on the block, Make-o-Matic
        """
        self.assertIn('Make-o-Matic', self.browser.title)

        """
        LT (Little Tommi) does not look at the browser's tab title,
        notices the page's title anyways
        """

        self.assertIn('Make-o-Matic', self.browser \
            .find_element_by_class_name('site-header__title').text)

        """
        LT recognises the navigation items
        """
        site_header__navigation = self.browser \
            .find_element_by_class_name('site-header__navigation')
        site_header__navigation__a = site_header__navigation \
            .find_elements_by_tag_name('a')
        self.assertTrue(
            any(element.text == 'Home'
                for element in site_header__navigation__a)
        )
        self.assertTrue(
            any(element.text == 'Register'
                for element in site_header__navigation__a)
        )
        self.assertTrue(
            any(element.text == 'Login'
                for element in site_header__navigation__a)
        )
        self.assertTrue(
            any(element.text == 'Users'
                for element in site_header__navigation__a)
        )

        """
        LT recognises he is on the home page
        """
        self.assertIn('The Home Page', self.browser \
            .find_element_by_class_name('site-index__title').text)


class RegisterTest(unittest.TestCase):

    import uuid

    username = str(uuid.uuid4())
    password = str(uuid.uuid4())

    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.get('http://localhost:5000/register')

    def tearDown(self):
        self.browser.quit()

    def delete_test_user(self):
        import config
        from py2neo import Graph
        graph = Graph(host=config.neo4j_database)
        graph.run("MATCH (n:User) WHERE (n.username={username}) DELETE n",
                  username = self.username)

    def register(self):
        self.browser.find_element_by_id('username').send_keys(self.username)
        self.browser.find_element_by_id('password').send_keys(self.password)
        self.browser.find_element_by_id('confirm').send_keys(self.password)
        self.browser.find_element_by_id('confirm').send_keys(Keys.ENTER)

    def test_register_elements(self):

        # LT would like to register on the page
        self.assertIn('Register', self.browser \
            .find_element_by_class_name('register__title').text)

        self.assertEqual(
            self.browser.find_element_by_name('username').get_attribute(
                'placeholder'), "Enter your username")

        self.assertEqual(
            self.browser.find_element_by_name('password').get_attribute(
                'placeholder'), "Enter your passphrase")

        self.assertEqual(
            self.browser.find_element_by_name('confirm').get_attribute(
                'placeholder'), "Repeat your passphrase")

        self.assertTrue(
            self.browser.find_element_by_id('csrf_token'))

    def test_01_register_new_user(self):
        self.register()

        self.assertIn('User created', self.browser \
            .find_element_by_class_name('flashes').text)

    def test_02_user_exists(self):
        self.register()

        self.assertIn('User exists', self.browser \
            .find_element_by_class_name('flashes').text)

    def test_03_remove_user(self):
        self.delete_test_user()



if __name__ == "__main__":
    unittest.main(warnings="ignore")
