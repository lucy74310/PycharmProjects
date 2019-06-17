# 클래스 정의
# 클래스: class 문으로 정의하며,  멤버와 메써드를 가지는 객체이다.
# - 클래스 자체도 객체
# - 함수(코드실행) 자체도 객체 : 속성(멤버, 메서드)을 가지고 있음
# - className.memberName -> 자바에서 static 변수


class MyString:
    pass


s = MyString()
print(type(s))
# 부모 알아보기 : 자바랑 비슷함
print(MyString.__bases__)

s2 = str()

print(type(s2))
# 부모 알아보기 : 자바랑 비슷함
print(str.__bases__)

