import os
import logging

_log = logging.getLogger(__name__)
_root_path = ""


def init(root_folder_path):
    """
    Initialize repository with the root folder path.
    @param root_folder_path: String, absolute or relative path
    >>> init("."); print("root_path=", _root_path) # @HOW return correct _root_path with init() effect?
    root_path=...

    >>> init(".")
    ... print("root_path=", make_path(""))
    ... #doctest:+ELLIPSIS
    root_path= ...

    >>> init(".")
    ... print("root_path=") # @WHY this line make no output?

    >>> init("uNrEAl~!!$%-nAmE")
    ... #doctest:+ELLIPSIS
    Traceback (most recent call last):
    ...
    OSError: ...
    """
    global _root_path
    path = os.path.abspath(root_folder_path)
    if not os.path.isdir(path):
        raise IOError("Initial folder %s is incorrect." % path)
    _root_path = path
    _log.info("File server initialized at %s folder." % path)


def make_path(filename: str):
    if _root_path == "":
        raise RuntimeError("Module not initialized. Call init().")
    path = os.path.normpath(os.path.join(_root_path, filename.lstrip("\\/")))
    _log.debug("Current path: '%s'." % path)
    return path


def write_file(filename, content):
    path = make_path(filename)
    with open(path, "wt") as fh:
        fh.write(content)
    _log.info("Created file %s." % path)


def read_file(filename):
    path = make_path(filename)
    with open(path, "rt") as fh:
        content = fh.read()
    _log.info("Read file %s." % path)
    return content


def make_statistics(filename):
    path = make_path(filename)
    f_size = os.path.getsize(path)
    f_date = os.path.getsize(path)
    return "Name: %s, %Size %s, Date: "


def get_file_list(folder):
    path = make_path(folder)
    if not os.path.isdir(path):
        raise IOError("Incorrect folder '%s'." % folder)
    files = os.listdir(path)
    _log.debug("List files %s:\n%s" % (path, files))
    return files


def check_and_create_file(folder):
    path = make_path(folder)
    if not os.path.isdir(path):
        os.mkdir(path)


def delete_file(full_path):
    path = make_path(full_path)
    if not os.path.isfile(path):
        raise IOError("Incorrect file '%s'." % full_path)
    os.remove(path)
