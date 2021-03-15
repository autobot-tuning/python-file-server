import os
import logging

__root_path = ""
__logger = logging.getLogger(__name__)


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
        raise IOError ("Initial folder %s is incorrect." % path)
    __root_path = path
    __logger.debug("File server initialized")


def make_path(filename):
    global __root_path
    if __root_path == "":
        raise RuntimeError("Module not initialized. Call init().")
    return os.path.normpath(os.path.join(__root_path, filename))


def create_file(filename, content):
    path = make_path(filename)
