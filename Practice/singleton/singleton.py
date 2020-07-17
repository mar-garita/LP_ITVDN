import unittest


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance


@singleton
class User:
    def __init__(self, username):
        self.username = username


class UserTestCase(unittest.TestCase):

    def test_User(self):
        u1 = User('User1')
        u2 = User('User2')
        self.assertIs(u1, u2)