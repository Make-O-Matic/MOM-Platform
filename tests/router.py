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

import unittest
import platform

class RoutingTests(object):
    """
    Helper class for Routing Tests.

    For use, define:
    routes: Which route to test
    function: Which function should handle the route
    """

    route = "myroute"
    function = "myfunction"

    def url_exists(self):

        routes = []
        for rule in platform.app.url_map.iter_rules():
            routes.append(str(rule))
        return routes

    def test_root_url_exists(self):
        self.assertIn(self.route, self.url_exists())

    def test_index_function_exists(self):
        self.assertIn(self.function, platform.app.view_functions)

    def test_index_endpoint_connection(self):
        self.assertEqual(self.function, platform.app.view_functions[
            self.function].__name__)

class indexRoutingTest(RoutingTests, unittest.TestCase):
    route = "/"
    function = "index"

class loginRoutingTest(RoutingTests, unittest.TestCase):
    route = "/login"
    function = "login"

class logoutRoutingTest(RoutingTests, unittest.TestCase):
    route = "/logout"
    function = "logout"

class registerRoutingTest(RoutingTests, unittest.TestCase):
    route = "/register"
    function = "register"

class usersRoutingTest(RoutingTests, unittest.TestCase):
    route = "/users"
    function = "users"

class AssetRoutingTest(unittest.TestCase):
    """
    Testing asset availability mainly by looking up asset URLs via calling
    the __Bundle__ object.

    Warnings are currently thrown for unclosed files (pending bug in flask
    assets).
    """

    def setUp(self):
        self.app = platform.app.test_client()

    def test_sass_route(self):
        page = self.app.get(platform.sass.urls()[0])
        self.assertEqual(page.status_code, 200)

    def test_bootstrap_route(self):
        page = self.app.get(platform.bootstrap.urls()[0])
        self.assertEqual(page.status_code, 200)

if __name__ == '__main__':
    unittest.main()
