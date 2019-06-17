import sys

i1 = 10
i2 = 10
print(hex(id(i1)), hex(id(i2)))

i0 = 10
i1 = 11
i2 = i0 + 1

print(hex(id(i1)), hex(id(i2)))


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)), hex(id(l2)))

s1 = 'hello'
s2 = 'hello'

print(hex(id(s1)), hex(id(s2)))

print(i1 is i2)
print(l1 is l2)
print(s1 is s2)


# ?
t1 = (1, 2, 3)
t2 = (1, 2, 3)
print(sys.getrefcount(t1), sys.getrefcount(t2))
print(t1 is t2)


# literal 과 tuple생성자로 만든 객체는 다르다
t3 = tuple(range(1, 4))
print(sys.getrefcount(t3))
print(t1 is t3)


# slicing한 객체는..? 역시 다르다. 오로지 리터럴만 같다.
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)



