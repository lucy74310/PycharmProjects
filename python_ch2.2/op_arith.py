# 사칙연산

print(2 * 3)
print(2 / 3)
print(2 + 3)
print(2 - 3)
print(2 / 3)
print(2 / 3.0)
print(2.0 / 3.0)

print()

# //(몫) **(지수승), %(나머지)
result, last = divmod(2, 3)
print(result, last)

t = divmod(2, 3)
print(t, type(t))

# 연산자 우선순위
print(2 + 3 * 4)
print(-2 + 3 * 4)
# 부호가 가장 우선순위 높다
print(-(2 + 3) * 4)

print(4 / 2 * 2)

# 우선순위 같을 때 순서 오른쪽-> 왼쪽 결합
print(2 ** 3 ** 4)
print(2 ** (3 ** 4))


