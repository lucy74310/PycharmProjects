# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Buit-in

a = 1 # G
b = 300


def f():
    b = 200 # E

    def g():
        # b = 100 # L -> 주석처리하면 EGB 에서 찾아본다
        print(b)
        print(__name__) # B -> 자신이 포함되어 있는 모듈에서 name (모듈이름)
    g()


# 단독으로 실행될 때만 f() 실행
if __name__ == '__main__':
    f()

