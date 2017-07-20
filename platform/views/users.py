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

from flask import render_template, redirect, url_for
from flask.views import View
from platform.models.user import User
from platform import database
from platform.models.permission import Permission

# Error Handling
from platform import app
from platform.views.errors import ShowErrors
from platform.models.errors import ServerError

class ShowUsers(View):

    def dispatch_request(self):
        db = database.get_db()

        if not Permission(db).has_role("administrator"):
            return redirect(url_for("index"))

        users = list(User.select(db))
        return render_template("users.html", users = users)

    @app.errorhandler(ServerError)
    def handle_invalid_usage(error):
        errorview = ShowErrors()
        return errorview.dispatch_request(error.message)
