from __future__ import absolute_import
from __future__ import unicode_literals
from . import file_service as fs

_test_filename = "test_file"
_test_content = "Some text..."


def create_file_test():
    fs.write_file(_test_filename, _test_content)
