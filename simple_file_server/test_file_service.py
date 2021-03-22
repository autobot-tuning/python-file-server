import os
import pytest
import shutil

from . import file_service as fs

_test_repository = "test_repository"
_test_filenames = ("test_file1", "test_file2")
_test_contents = ("Some text 1...", "Some text 2...")
_test_data = ((_test_filenames[i], _test_contents[i]) for i in range(2))


def setup_module(module):
    print("\nSetting up module: " + str(module))
    if os.path.isdir(_test_repository):
        shutil.rmtree(_test_repository)
    os.mkdir(_test_repository)


def teardown_module(module):
    print("\nTearing down module: " + str(module))
    pass


@pytest.fixture
def init_service():
    fs.init(_test_repository)


@pytest.fixture
def repository_path(init_service):
    path = fs.make_path(".")
    print("\nCreated fixture: " + path)
    return path


def test1():
    print("\nTest data: " + str(list(_test_data)))


def test2(repository_path):
    print("\nTest repository path: " + repository_path)


# @pytest.mark.parametrize("filename", _test_filenames)
# @pytest.mark.parametrize("content", _test_contents)
@pytest.mark.parametrize(("filename", "content"), _test_data)
def test_create_file(init_service, filename, content):
    print("\nWriting file: ", filename, content)
    fs.write_file(filename, content)
