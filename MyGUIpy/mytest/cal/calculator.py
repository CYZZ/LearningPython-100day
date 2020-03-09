def add(a, b):
    return a + b


def reduce(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


class car():
    name = "abcd"

    def __init__(self):
        print('car 已经开始初始化了')

    def __del__(self):
        print('car 类已经销毁了')
    def sayHello(self):
        print('car say hello')
