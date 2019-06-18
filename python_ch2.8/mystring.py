class MyString:

    def __init__(self, s):
        self.s = s

    def __str__(self):
        return self.s

    def __truediv__(self, other):
        return self.s.split(other)

    def __add__(self, other):
        print('__add__')
        # str 타입 리턴
        # return self.s + other.s
        # MyString 타입 리턴
        return MyString(self.s+other.s)

    def __radd__(self, other):
        print('__radd__')
        return other + self.s

    def __mul__(self, other):
        print('__mul__')
        return self.s * other

    def __rmul__(self, other):
        print('__rmul__')
        return other * self.s

    def __neg__(self):
        return self.s[::-1]

s = MyString('Python Programmer is Good')
t = s / ' '
print(type(t))
print(t)

print(s + MyString(' Job'))

print(MyString('Python ') * 3)
print(3 * MyString('Python ') * 3)

print(MyString('Hello') + MyString('  ') + MyString('World'))


print('hello' + MyString(' world'))