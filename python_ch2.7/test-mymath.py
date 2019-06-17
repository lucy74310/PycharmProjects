import sys

# 드라이브 빼도 됨
# \ -> / 로 해도 됨
# sys.path.append('/cafe24/PycharmProjects/python-modules')
# sys.path.append('../python-modules')
# project interperter에 path 에 추가해줌

# 실행시엔 성공
import mymath

print(mymath.pi)
print(mymath.add(10, 20))
print(mymath.area_circle(10))