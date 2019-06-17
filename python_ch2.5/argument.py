# 기본 인수값


def incr(a, step=1):
    return a + step


# a 가 기본 인수값을 가진 인자 뒤로 갈 수 x
# 기본 인수 뒤에 인자 오는것도 X 기본인수면 O
def decr(a, step=1):
    return a - step


print(incr(10))
print(incr(10, step=2))
print(incr(10, 4))


# 키워드 인수
def area(width, height):
    return width * height


print(area(10, 20))
print(area(height=20, width=10))
print(area(width=10, height=20))


#  오류
# area(20, width=10)
# TypeError: area() got multiple values for argument 'width'


# 가변 인수
def varg(a, *arg):
    print(a, arg)


varg(10)
varg(10, 1)
varg(10, 1, 3, 4, 5, 7)


# 정의되지 않은 키워드 인수는 모두 dict로 받을 수 있다.
def _print(*args, end='newline'):
    print(args, end)


_print(10, 20, 30)
_print(10, end='tab')
_print(10, 'tab')


# c의 print흉내내기
def printf(format, *args):
    print(format % args)


printf("%s이 %d원짜리 %s를 입고, %s를 차고 노래를한다,", "타잔", 100, '팬티', '?')


# 정의되지 않은 키워드 인수 처리하기
def f(width, height, **kw):
    print(width, height)
    print(kw)


f(10, 20)
f(10, 20, depth=10)
f(10, 20, depth=10, dimension=3)
# 키워드 x 에러
# f(10, 20, depth=30, 40)


def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)


g(10, 20)
g(10, 20, 30)
g(10, 20, c=60)
g(10, 20, 30, 'sleep', depth=40, dimension=5)


# 튜플/ 사전 파라미터
def h(name, age, height):
    print(name, age, height)


h('둘리', 10, 150)
print('-------------')
t = ('둘리', 10, 50)
h(*t)


d = {'name': '둘리', 'age': 10, 'height': 50}
h(**d)

