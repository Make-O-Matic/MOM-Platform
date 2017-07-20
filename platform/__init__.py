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

from flask import Flask
from flask_assets import Environment, Bundle

app = Flask(__name__)

assets = Environment(app)

sass = Bundle("scss/devices.scss",
              "scss/layout.scss",
              "scss/index.scss",
              "scss/flashes.scss",
              "scss/login.scss",
              "scss/register.scss",
              filters = "pyscss",
              output = "compiled/sass.css")
assets.register("sass", sass)

bootstrap = Bundle("vendor/bootstrap/bootstrap.min.css",
                   "vendor/bootstrap/bootstrap-theme.min.css",
                   output = "compiled/bootstrap.css")
assets.register("bootstrap", bootstrap)

import platform.router
