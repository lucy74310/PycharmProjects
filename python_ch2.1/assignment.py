# 치환문
# 연산 방향은 오른쪽에서 왼쪽

a = 1
b = a+1

print(a, b)

# sep 지정 가능
print(a, b, sep=' : ')

# 세미콜론으로 치환문을 구분 할 수 있다.
e = 3.5;  f = 5.3
print(e, f)

# 여러 개를 한번에 치환하기
e, f = 3.5, 5.3
print(e, f)


# 같은 값을 여러 변수에 대입
x = y = z = 10
# c 스타일은 지원 x
# x = (y = 10)

print(x, y, z)


# 동적 타이핑
# 변수에 새로운 값이 할당되면 값을 버리고
# 새로운 값으로 치환된다.
a = 1
print(a, type(a))

a = 'hello'
print(a, type(a))

# 확장 치환문
a = 10
a += 10  # a = a + 10
print(a)











