def f():
    l_a = 2
    l_b = '마이콜'
    print(locals())


class MyClass:
    x = 10
    y = 20


g_a = 1
g_b = '둘리'

# print(globals())

f()


# 1. 정의된 함수
f.k = 'hello'
print(f.__dict__)

# 2. 클래스 객체
MyClass.z = 10
# print(MyClass.__dict__)
# 내장 클래스
# TypeError: can't set attributes of built-in/extension type 'str'
# str.z = 10
# 내장 클래스는 심벌 테이블은 있으나 O -> 확장 X
# print(str.__dict__)

# 내장 함수는 심벌 테이블이 X -> 확장 X
# AttributeError: 'builtin_function_or_method' object has no attribute '__dict__'
# print(print.__dict__)

# 내장 클래스로 생성된 객체
# 심벌 테이블 X -> 확장 X
#g_a.z = 10
#print(g_a.__dict__)


# 사용자 정의된 클래스로 생성된 객체
# 심벌 테이블 O -> 확장 O
o = MyClass()
o.x = 100
print(o.__dict__)