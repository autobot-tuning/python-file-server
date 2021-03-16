import hashlib
import os
import logging

__logger = logging.getLogger(__name__)
__root_path = ""


def init(root_folder_path):
    """
    Initialize repository with the root folder path.
    @param root_folder_path: String, absolute or relative path
    >>> init("."); print "root_path=", __root_path # @HOW return __root_path?
    ... #doctest:+ELLIPSIS
    root_path=...

    >>> init(".")
    ... print "root_path=" # @WHY this line make no output?

    >>> init("uNrEAl~!!$%-nAmE")
    ... #doctest:+ELLIPSIS
    Traceback (most recent call last):
    ...
    IOError: ...
    """
    global __root_path
    path = os.path.abspath(root_folder_path)
    if not os.path.isdir(path):
        raise IOError("Initial folder %s is incorrect." % path)
    __root_path = path
    __logger.info("File server initialized at %s folder." % path)


def make_path(filename):
    global __root_path
    if __root_path == "":
        raise RuntimeError("Module not initialized. Call init().")
    return os.path.normpath(os.path.join(__root_path, filename))


def write_file(filename, content):
    path = make_path(filename)
    with open(path, "wt") as fh:
        fh.write(content)
    __logger.info("Created file %s." % path)


def read_file(filename):
    path = make_path(filename)
    with open(path, "rt") as fh:
        content = fh.read()
    __logger.info("Read file %s." % path)
    return content




def make_statistics(filename):
    path = make_path(filename)
    f_size = os.path.getsize(path)
    f_date = os.path.getsize(path)
    return "Name: %s, %Size %s, Date: "