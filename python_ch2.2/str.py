# 한 줄 문자열 정의

s = ''
str1 = 'Hello World'
print(type(s), type(str1))
print(isinstance(s, str))


# 여러줄 문자열
str2 = 'hello world'

'''
주석
'''

# escape
print('Hello\nWorld\n! Say \"Hello World\"')
print('Hello\nWorld\n! Say \"Hello World\"')



#
# 문자열 연산
#
str1 = 'First String'
str2 = 'Second String'

# 1. 인덱싱
print(str1[0], str1[1], str1[2])
print(str1[-1], str1[-2], str1[-3])

# 2. Slicing
# s[start:stop:step]
# 라인으로 생각
str3 = str2[2:5]
print(str3)
# 같은결과
print(str2[2:len(str2)])
print(str2[2:]) # 맨 마지막 까지

s = "Python"
print(s[-1])    # 마지막 문자
print(s[-2:])   # 마지막 2 개 문자
print(s[:-2])   # start 0 이 생략 -> 마지막 2개 문자 제외한 전체 문자

print(s[::-1])      # reverse
print(s[1::-1])     # 역순이니까 1번째, 2번째 문자 문자 s[1:0:-1]
print(s[:-3:-1])    # 마지막 두개 문자 s[0:-3:-1]
print(s[-3::-1])    #


# 연결(+)
print(str1 + ' ' + str2)

# str 객체는 immutable이다
# str1[0] = 'f'

# 서식(formatting) = format 함수
name = "bugwang"
age = 27
print("name:" + name + " , age: " + str(age))
print("name:" + format(name,"s") + " , age: " + format(age, "d"))


# 서식
f = "name:%s , age:%d"
print(f % (name, age))
print(f % ("또치", 20))


# 서식 : 딕셔너리를 사용한 방식
f = "name:%(n)s , age:%(a)d"
print(f % {"n": "둘리", "a": 12})
print(f % {"a": 12, "n": "둘리"})


#
# 객체 함수
#

# 1. 대소문자 관련
s = 'i like Python'
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

# 2. 검색
s = 'I Like Python, I Like Java Also'
print(s.count("Like"))
print(s.find('Like'))   # 시작하는 인덱스
print(s.find('Like', 5))
print(s.find('JavaScript')) # 없을때 -1
print(s.rfind("Like"))     # 오른쪽에서부터 찾는 ?


print(s.index("Like"))
# 발견하지 못하면 예외가 발생한다
# print(s.index("Javascript"))
print(s.startswith("I Like"))   # True or False
print(s.startswith("Like", 5))  # 해당 인덱스부터 Like 이면 True
print(s.endswith("Also"))   # 끝이 해당 글자로 끝나는지
print(s.endswith("Java", 0, 20))    # Java 22~25
print(s.endswith("Java", 0, 26))


# 편집과 치환
s = '   span and ham    '
print('------' + s.strip() + '-------')
print('------' + s.rstrip() + '-------')
print('------' + s.lstrip() + '-------')


s = '<><abc><><defg><><>'
print('------' + s.strip('<>') + '-------')
print('------' + s.strip('><') + '-------')

s = 'Hello Java'

print(s.replace('Java', 'Python'))

# 분리 & 결함

s = 'spam and ham'
l = s.split(' and ')
print(l, type(l))

s2 = ':'.join(l)
print(s2)


s3 = 'one:two:three:four:five'

print(s3.split(":"))
print(s3.split(':', 2))
print(s3.rsplit(":", 2))


lines = '''1stline
2nd line
3rd line
4th line
'''

print(lines.split('\n'))
print(lines.splitlines())

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())


print('abcd'.islower())
print('ABCD'.isupper())

print('    '.isspace())
print('\r\n   '.isspace())
print('\t   '.isspace())

# '0' 채우기 zero fill function
print('20'.zfill(5))
print('1234'.zfill(5))


# 서식 : 객체함수
print('name: {}, age{}'.format('둘리', '10'))     # 인덱스를 안주면 순서대로
print('name: {0}, age{1}'.format('둘리', '10'))
print('name: {1}, age{0}'.format('둘리', '10'))   # 인덱스 대로
print('{:3}의 제곱근은 {:.7}'.format(2, 2**0.5))
print('name: {n}, age:{a}'.format_map({'a':20, 'n':'둘리'}))




