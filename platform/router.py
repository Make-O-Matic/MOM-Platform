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

from platform import app

from platform.views import (index, register, login, logout, users, status,
                            errors, install, profile)

app.add_url_rule('/', view_func =
    index.ShowIndex.as_view('index', template_name='index.html'))

app.add_url_rule('/register', view_func =
    register.ShowRegister.as_view("register"))

app.add_url_rule('/login', view_func =
    login.ShowLogin.as_view("login"))

app.add_url_rule('/logout', view_func =
    logout.ShowLogout.as_view("logout"))

app.add_url_rule('/users', view_func =
    users.ShowUsers.as_view("users"))

app.add_url_rule('/status', view_func =
    status.ShowStatus.as_view("status"))

app.add_url_rule('/errors', view_func =
    errors.ShowErrors.as_view("errors"))

app.add_url_rule('/install', view_func =
    install.ShowInstall.as_view("install"))

app.add_url_rule('/profile/<username>', view_func =
    profile.ShowProfile.as_view("profile"))
