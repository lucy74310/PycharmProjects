import mymod2
import mymod
# 두개가 import 되어도 문제 없음
# 딱 한번만 import 된다
# 모듈은 한 번 가져오기 하면 메모리에 적재되고 공유된다.

print(mymod.add(10, 20))
print(mymod.subtract(10, 20))
print(mymod.multiply(10, 20))
print(mymod.divide(10, 20))

print(mymod2.power(10, 20))

