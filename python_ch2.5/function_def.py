
def dummy():
    return '?'


def times(a, b):
    return a*b


def my_function():
    print('Hello World')


def none():
    return


def my_function2(func):
    func()


dummy()
my_function()
times(10, 20)


# 함수도 객체다
print(dummy, type(dummy))
f = my_function
f()
my_function2(f)

print(f, my_function)


# 여러 return 값
def func():
    return 10, 'hello', {1, 2, 3}, (1, 2, 3)


n, s, st, t = func()

print(n, s, st, t)

