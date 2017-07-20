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

from flask import render_template, flash
from flask.views import MethodView

from platform import database
from platform.models.user import User

from platform.models import forms

# Error Handling
from platform import app
from platform.views.errors import ShowErrors
from platform.models.errors import ServerError


class ShowRegister(MethodView):

    methods = ["GET", "POST"]

    def dispatch_request(self):

        form = forms.UserRegistration()

        if form.validate_on_submit():
            db = database.get_db()

            if User.get_by_username(db, form.username.data):
                flash("User exists", "error")
            else:
                user = User()
                user.username = form.username.data
                user.set_password(form.password.data)
                user.add_role_by_name(db, "user")
                db.create(user)

                flash("User created", "success")

        return render_template("register.html", form=form)

    @app.errorhandler(ServerError)
    def handle_invalid_usage(error):
        errorview = ShowErrors()
        return errorview.dispatch_request(error.message)
