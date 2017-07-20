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

import bcrypt
from py2neo.ogm import GraphObject, Property, RelatedTo

from platform.models.role import Role

class User(GraphObject):

    __primarykey__ = "username"

    username = Property()
    password_hash = Property()

    roles = RelatedTo(Role, "role")


    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(bytes(password, 'utf-8'),
                                           bcrypt.gensalt(12))


    def add_role_by_name(self, graph, role_name):
        role = Role.select(graph, role_name).first()
        if not role:
            return False
        self.roles.add(role)


    def has_role_with_name(self, role_name):
        for role in self.roles:
            if role.name == role_name:
                return True
        return False


    def get_by_login(graph, username, password):
        if not username:
            return None

        user = User.select(graph, username).first()
        if user and bcrypt.checkpw(password.encode('utf-8'),
                                   user.password_hash.encode('utf-8')):
            return user
        return None


    def get_by_username(graph, username):
        if not username:
            return None

        return User.select(graph, username).first()
