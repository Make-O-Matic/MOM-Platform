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
from platform.models.role import Role
from platform.models.status import Status
from platform.models import forms

# Error Handling
from platform import app
from platform.views.errors import ShowErrors
from platform.models.errors import ServerError


class ShowInstall(MethodView):

    methods = ["GET", "POST"]

    def dispatch_request(self):
        form = forms.UserRegistration()
        if form.validate_on_submit():
            self._install(form.username.data, form.password.data)
        return render_template("install.html", form = form)

    def _install(self, username, password):
        db = database.get_db()

        if Status.get_value(db, "installed"):
            flash("Already installed", "error")
            return

        if User.get_by_username(db, username):
            flash("User exists", "error")
            return

        self._install_roles()

        user = User()
        user.username = username
        user.set_password(password)
        user.add_role_by_name(db, "administrator")
        db.create(user)

        Status.set_value(db, "installed", True)

        flash("Installed", "success")

    def _install_roles(self):

        db = database.get_db()
        role_names = [
            "administrator",
            "moderator",
            "user",
        ]

        for role_name in role_names:
            role = Role()
            role.name = role_name
            db.create(role)

    @app.errorhandler(ServerError)
    def handle_invalid_usage(error):
        errorview = ShowErrors()
        return errorview.dispatch_request(error.message)
