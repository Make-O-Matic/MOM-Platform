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

DOC_DIR          = docs

UNITTEST         = python -m unittest
UNITTEST_VERBOSE = python -m unittest -v

ANSIBLE          = cd ansible; ansible-playbook -i production --ask-vault-pass
ANSIBLE_NP       = cd ansible; ansible-playbook -i production

.PHONY: tu
tu:
	$(UNITTEST) tests.router
	$(UNITTEST) tests.views
	$(UNITTEST) tests.models

.PHONY: tuv
tuv:
	$(UNITTEST_VERBOSE) tests.router
	$(UNITTEST_VERBOSE) tests.views
	$(UNITTEST_VERBOSE) tests.models


.PHONY: tf
tf:
	$(UNITTEST) functional_tests.py

.PHONY: tfv
tfv:
	$(UNITTEST_VERBOSE) functional_tests.py

.PHONY: docs
docs:
	sphinx-apidoc -o docs/modules platform/views
	$(MAKE) -C $(DOC_DIR) html

.PHONY: clean-docs
clean-docs:
	$(MAKE) -C $(DOC_DIR) clean

.PHONY: provision
provision:
	$(ANSIBLE) mom.yml

.PHONY: update-nginx
update-nginx:
	$(ANSIBLE) update_nginx.yml

.PHONY: update-platform
update-platform:
	$(ANSIBLE) update_platform.yml

.PHONY: update-notebooks
update-notebooks:
	$(ANSIBLE_NP) update_notebooks.yml
