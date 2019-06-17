# call by reference 이지만
# 내부에서 변경하더라도 변경되지 않는다 (immutable)


def f(i):
    i = 20
    print(locals())


def f2(seq):
    seq[0] = 0


a = 10
print(globals())
f(a)
print(globals())
print(a)


a = (1, 2, 3)

# 파라미터가 sequence type(immutable) 인 경우
# 내부에서 변경시 오류
# f2(a)


a = [1, 2, 3]
f2(a)
print(a)
