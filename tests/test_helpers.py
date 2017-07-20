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

class TestHelpers(object):
    """
    Get all the information
    Currently stub for lookup reasons
    """

    def get_all_test_client_names(self, page):

        print("accept_ranges: ", page.accept_ranges)
        print("add_etag: ", page.add_etag)
        print("age: ", page.age)
        print("allow: ", page.allow)
        print("autocorrect_location_header: ", page.autocorrect_location_header)
        print("automatically_set_content_length: ", page.automatically_set_content_length)
        print("calculate_content_length: ", page.calculate_content_length)
        print("call_on_close: ", page.call_on_close)
        print("charset: ", page.charset)
        print("close: ", page.close)
        print("content_encoding: ", page.content_encoding)
        print("content_language: ", page.content_language)
        print("content_length: ", page.content_length)
        print("content_location: ", page.content_location)
        print("content_md5: ", page.content_md5)
        print("content_range: ", page.content_range)
        print("content_type: ", page.content_type)
        print("data: ", page.data)
        print("date: ", page.date)
        print("content_md5: ", page.content_md5)
        print("default_mimetype: ", page.default_mimetype)
        print("default_status: ", page.default_status)
        print("expires: ", page.expires)
        print("force_type: ", page.force_type)
        print("freeze: ", page.freeze)
        print("from_app: ", page.from_app)
        print("get_app_iter: ", page.get_app_iter)
        print("get_data: ", page.get_data)
        print("get_etag: ", page.get_etag)
        print("get_wsgi_headers: ", page.get_wsgi_headers)
        print("get_wsgi_response: ", page.get_wsgi_response)
        print("headers: ", page.headers)
        print("implicit_sequence_conversion: ", page.implicit_sequence_conversion)
        print("is_sequence: ", page.is_sequence)
        print("is_streamed: ", page.is_streamed)
        print("iter_encoded: ", page.iter_encoded)
        print("last_modified: ", page.last_modified)
        print("location: ", page.location)
        print("make_conditional: ", page.make_conditional)
        print("make_sequence: ", page.make_sequence)
        print("mimetype: ", page.mimetype)
        print("mimetype_params: ", page.mimetype_params)
        print("response: ", page.response)
        print("retry_after: ", page.retry_after)
        print("set_cookie: ", page.set_cookie)
        print("set_data: ", page.set_data)
        print("set_etag: ", page.set_etag)
        print("status: ", page.status)
        print("status_code: ", page.status_code)
        print("stream: ", page.stream)
        print("vary: ", page.vary)
        print("www_authenticate: ", page.www_authenticate)

if __name__ == '__main__':
    unittest.main()
