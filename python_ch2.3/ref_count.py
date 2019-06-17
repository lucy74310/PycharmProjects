import sys

x = object()
print(type(x))
print(sys.getrefcount(x))


y = x
print(sys.getrefcount(x))

# 레퍼런스 값 줄이기
# del은 심볼 테이블에서 이름을 삭제한다
del x
test = 1234
print(sys.getrefcount(y)) # x 날려서 y 로 접근
print(globals())

