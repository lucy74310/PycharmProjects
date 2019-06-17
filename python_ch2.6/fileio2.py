f = open('test.txt', 'rt', encoding='utf-8')
text = f.read()
print(text)
text = f.read()
print('----', text, '----')

# 안녕하세요
# 파이썬입니다.
# 11글자 -> 33 byte + . 1byte = 34 byte
# 파일크기 36 byte

# position 단위는 byte
pos = f.tell()

print(pos)


# seek 함수
# 1st param : offset
# 2st param : from_what(0: 시작, 1:현재위치, 2: 끝)

# f.seek(10, 2)
#f.seek(10, 0)
# f.seek(16, 2)
# f.seek(16, 0)

# text = f.read()
# print(text)

f = open('123.txt', 'wb')
f.write(b'0123456789')
f.close()

f = open('123.txt', 'rb')
print(f.tell())

f.seek(5, 1)
data = f.read(2)
print(data)


f.seek(0, 2) # 맨 끝으로 이동

f.seek(-5, 1)
data = f.read(3)


# line 단위로 읽기
f2 = open('fileio2.py', 'rt', encoding='utf-8')
linenum = 0
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum += 1
    print('{0}:{1}'.format(linenum, line), end='')


f3 = open('fileio2.py', 'rt', encoding='utf-8')
lines = f3.readlines() # 라인 리스트로 한번에 받음
f3.close()
print(type(lines))
for linenum, line in enumerate(lines):
    print('{0}:{1}'.format(linenum, line), end='')


# with ~ as
with open('fileio2.py', 'rt', encoding='utf-8') as f4:
    for linenum, line in enumerate(f4.readlines()):
        print('{0}:{1}'.format(linenum, line), end='')


# try resource구문
