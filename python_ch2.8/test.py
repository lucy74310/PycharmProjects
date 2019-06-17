global_a = 1
global_b = 'global'

def foo():
    local_a = 2
    local_b = 'local'
    print(locals())

class MyClass:
    x = 10
    y = 20


# 1. global symbol table 확인
print(globals())    # 'global_a': 1, 'global_b': 'global', 'foo': <function foo at 0x00000228D8A05268>, 'MyClass': <class '__main__.MyClass'>}

# 2. local symbol table 확인
foo()   # {'local_b': 'local', 'local_a': 2}

# 3. 정의된 함수 객체 확인
# symbol table이 있다는 것은 확장이 가능함을 의미한다.
# 그리고 __dict__를 통해 접근이 가능하다.
foo.c = 'hello'
foo.d = 'world'
print(foo.__dict__)         # {'c': 'hello'}

# 4. MyClass 객체
print(MyClass.__dict__)     # {'x': 10, 'y': 20, '__dict__': <attribute '__dict__' of 'MyClass' objects>,}