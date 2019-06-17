# 객체의 대소의 비교

print(1 >= 3)
print(2 >= 4)

print(6 == 9)
print(6 != 9)


# 복합관계

a = 6

print(0 < a and a < 10)
print(0 < a < 10)

# 수치형 이외의 객체 비교
print('abcd' > 'abd')
print((1, 2, 4) < (1, 3, 1))
print([1, 3, 2] < [1, 2, 0])

# print([1, 3, 2] < (1, 2, 0)) 에러남
print([1, 3, 2] < list((1, 2, 0)))


# 동질성 비교 동일성 비교
a = 10
b = 20
c = 1
print( a == b)
print( a is b)
print(a is c)


# 논리의 계산 순서

print('ok')

s = 'hello world'
# none 이 아니면 실행
s and print(s)


def f(msg=None):
    msg and print(msg)


f()
f('hello world~')

# def f():
#     print('execution!')
#
#
# if 1 + 2 < 10:
#     f();
#
#
# 1 + 2 > 10 and f()


