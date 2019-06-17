

# 레퍼런스 복사
import copy

a = 1
b = a


a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = x   # 레퍼런스 복사

print(x)
print(y)
print(x is y)

# swallow copy (얕은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.copy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])


# deep copy (깊은 복사)
a = [1, 2, 3]
b = [4, 5, 6]
x = [a, b, 100]
y = copy.deepcopy(x)
print(x)
print(y)
print(x is y)
print(x[0] is y[0])

# 깊은 복사가 복합객체만을 생성하기 때문에
# 복합객체가 한개만 있는 경우에는
# 얕은 복사, 깊은 복사는 차이는 없다
a = ['hello', 'world']
b = copy.copy(a)
print(a is b)
print(a[0] is b[0])

b = copy.deepcopy(a)
print(a is b)
print(a[0] is b[0])

#
