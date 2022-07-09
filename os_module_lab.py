import os
import shutil
from os import path
import pytest

cwd = os.getcwd()


@pytest.fixture()
def setup_dirs():
    os.chdir("/home/david/PycharmProjects/entry-level-course")
    dirs = ["./tree/c/other_courses/cpp",
            "./tree/c/other_courses/python",
            "./tree/cpp/other_courses/c",
            "./tree/cpp/other_courses/python",
            "./tree/python/other_courses/c",
            "./tree/python/other_courses/cpp"]
    for d in dirs:
        if not path.exists(d):
            os.makedirs(d)

    return True


@pytest.fixture()
def teardown_dirs():
    yield True
    os.chdir("/home/david/PycharmProjects/entry-level-course")
    shutil.rmtree("./tree")

found = []

def find_dirs(start_path, find_this):
    cwd = os.getcwd()
    os.chdir(start_path)
    for d in os.listdir():
        if d == find_this:
            # print(os.getcwd() + "/" + d)
            found.append(os.getcwd() + "/" + d)
        find_dirs(d, find_this)
    os.chdir(cwd)


def test_find_dirs(setup_dirs, teardown_dirs):
    start_path = "./tree"
    dir_to_find = "python"
    print(f"Searching recursively for \'{dir_to_find}\' under \'{start_path}\'")

    start_dir = os.getcwd()
    should_find = ["/home/david/PycharmProjects/entry-level-course/tree/python",
                   "/home/david/PycharmProjects/entry-level-course/tree/c/other_courses/python",
                   "/home/david/PycharmProjects/entry-level-course/tree/cpp/other_courses/python"]
    find_dirs(start_path, dir_to_find)

    assert sorted(found) == sorted(should_find)
    assert start_dir == os.getcwd()
