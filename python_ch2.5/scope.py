# LGB 규칙 !
# Local Global Built-in (이름공간3가지)
# 이름공간에 저장된 이름을 통해 객체를 참조하게 된다.
# 지역변수에 없으면 글로벌스콥에서 찾는다
# 동일한 이름이 이 세 가지 Scope에 존재하면 LGB 순서로 찾는다.


def func1(a):
    x = 3
    return a + x


def func2(a):
    return a + x


def func3(a):
    global g
    g = 3
    return a + g

# 실행된 시점에 x 가 없으므로 NameError: name 'x' is not defined
# print(func(2))


x = 1
g = 10

# (L)GB
print(func1(5))

# L(G)B
print(func2(2))
print(g)
print(func3(4)) # 이때 g 변함
print(g)

# LG(B)
print(dir(__builtins__))



