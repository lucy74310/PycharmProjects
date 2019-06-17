# dictionary => map

# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

# 접근 - 연관배열 : [문제] 없는 키로 접근하면 에러남
print(d['basketball'])

# 반복(*), 연결(+) 지원하지 않는다. (sequence형이 아니기 때문에)

# 변경가능
d['valleyball'] = 6
print(d)

# 길이
print(len(d))

# in, not in 가능 : 키만 가능
print('soccer' in d)
print('valleyball' in d)


#
# 다양한 dict 객체 생성 방법
#

# 1. literal
d = {}
print(d, type(d))

# 2. dict() 사용하는 방법1
d = dict()
print(d)

# 3. dict() 사용하는 방법2
d = dict(one=1, two=2, three=3)
print(d)

# 4. dict() 사용하는 방법3
d = dict([('one', 1), ('two', 2), ('three', 3)])
print(d)

# 5. dict() 사용하는 방법4 - zip을 사용하는 방법
# list set tuple 을 dict로 만드는 방법
# keys = {'one', 'two', 'three'}
keys = ('one', 'two', 'three')
# print(keys, type(keys))
# values = {1, 2, 3}
values = (1, 2, 3)
# sequence 있는 애로 해야 함 순서 섞임
d = dict(zip(keys, values))
print(d)

# 다양한 key 타입 (immutable 타입만 가능하다 )
# dict 에서 key는 immutable, value는 mutable
d = {}

d[True] = 'true'
d[10] = '10'
d['twenty'] = 20
d[(1, 2, 3)] = 6
# d[[1, 2, 3]] = 6 # immutable이 아니라서 에러
print(d)

# keys 객체
keys = d.keys()
print(keys, type(keys))
for key in keys:
    print("{0}:{1}".format(key, d[key]))

# values 객체
values = d.values()
print(values, type(values))

# items 객체
# [(key1, value1), (key2, value2), ...]
items = d.items()   # 복합 자료형
print(items, type(items))


phone = {
    '둘리': '000-0000-0000',
    '마이콜': '111-1111-1111',
    '또치': '222-2222-2222',
}

p = phone
print(p)
print(phone)

# phone -> s 를 가리키고 있었다면
# p = phone 은
# p -> s 를 가리키게 만드는 것

# p['도우넛'] = '333-3333-3334'
print(p)
print(phone)


p = phone.copy()
print(p)
print(phone)
p['누구있찌또'] = '444-4444-4444'
print(p)
print(phone)


# get() 함수
# get을 사용하는 이유는 해당 키값에 대한 객체 값이 존재하지 않는 경우
# None을 받기 위해서
# print(phone['도우넛'])
print(phone.get('도우넛'))

# setDefault
print(phone.setdefault('도우넛', '333-3333-3333'))
print(phone)


# 업데이트
phone.update({
    '도우넛': '333-3333-3333',
    '또치': '444-4444-4444'
})

print(phone)

# 모두 삭제하기
phone.clear()

print(phone)

