
# if ~ else
a = 10
if a > 5:
    print('big')
else:
    print('small')


# if ~ elif ~ else
n = -2
if n > 0:
    print('양수')
elif n < 0:
    print('음수')
else:
    print('0')


# tenery operator (삼항연산자)
# in java System.out.println( a > 5 ? 'big' : 'small' );
# value =  true-expr  if  condition   else  false-expr
print('big' if a > 5 else 'small')

count = 1
# 완전히 다 돌아야 ok가 나온다.
# 중간에 브레이크 하면 나오지 않음
while count < 11:
    print(count, end='  ')
    if count == 5:
        break
    count += 1
else:
    print('ok')


# break, continue, else 문 적용
i = 0
while i < 10:
    i += 1

    if i < 5:
        continue
    if i >= 10:
        break
    print(i, end=' ')
else:
    print('ok')

# 무한루프
i = 0
while True:
    i += 1

    print(i, end=' ')

    if i > 5:
        break


else:
    print('else block')

