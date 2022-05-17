from subprocess import check_output

import requests


def print_contents_of_cwd():
    return check_output(["ls"]).split()


def get_google():
    r = requests.get("https://www.google.com/")

    return r.json()


class Wrench(object):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def wrencher(self) -> int:
        return self.x + self.y


def wrench_out():
    return Wrench(5, 10).wrencher()
