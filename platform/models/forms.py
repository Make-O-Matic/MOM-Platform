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

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms import validators


class UserRegistration(FlaskForm):

    username = StringField(
        "Username",
        validators = [
            validators.Length(min = 3),
            validators.DataRequired(),
        ],
        render_kw = {"placeholder": "Enter your username"}
    )

    password = PasswordField(
        "Password",
        validators = [
            validators.DataRequired(),
            validators.Length(min = 8),
        ],
        render_kw = {"placeholder": "Enter your passphrase"}
    )

    confirm = PasswordField(
        "Repeat Password",
        validators = [
            validators.DataRequired(),
            validators.EqualTo("password", message = "Passwords don't match"),
        ],
        render_kw = {"placeholder": "Repeat your passphrase"}
    )


class UserLogin(FlaskForm):

    username = StringField(
        "Username",
        validators = [
            validators.DataRequired(),
        ],
        render_kw = {"placeholder": "Enter your username"}
    )

    password = PasswordField(
        "Password",
        validators = [
            validators.DataRequired(),
        ],
        render_kw = {"placeholder": "Enter your passphrase"}
    )
