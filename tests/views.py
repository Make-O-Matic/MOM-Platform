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

import platform
import unittest

class ViewTests(object):
    """
    Helper class for View Testing

    Expects the following:
    route: What route content to test
    """

    def setUp(self):
        self.app = platform.app.test_client()

class ViewsIndexTest(ViewTests, unittest.TestCase):

    def setUp(self):
        self.app = platform.app.test_client()
        self.page = self.app.get("/")

    def test_proper_mimetype(self):
        self.assertTrue(self.page.mimetype == "text/html")

    def test_starts_with_html(self):
        self.assertTrue(self.page.data.decode().startswith("<!doctype html>"))

    def test_ends_with_html(self):
        self.assertTrue(self.page.data.decode().endswith("</html>"))


class ViewRegisterTest(ViewTests, unittest.TestCase):

    import uuid

    username = str(uuid.uuid4())
    password = str(uuid.uuid4())

    def setUp(self):
        self.app = platform.app.test_client()
        platform.app.config['WTF_CSRF_ENABLED'] = False
        platform.app.config['SECRET_KEY'] = "TESTKEY_SUPERSECRET"


if __name__ == '__main__':
    unittest.main()