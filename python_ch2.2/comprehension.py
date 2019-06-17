results = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    result = n * n
    results.append(result)

print(results)

# 문자열 리스트에서 길이가 2 이하인 문자열 리스트
strings = ['a', 'as', 'bar', 'car', 'as', 'dove', 'python']
string = [s for s in strings if len(s) <= 2] # as 중복 들어감
print(string)
string = {s for s in strings if len(s) <= 2} # as 중복 안들어감
print(string)


evens = [n for n in range(1, 101) if n % 2 == 0]
print(evens)


# dict comprehension
strings = ['a', 'bar', 'car', 'as', 'dove', 'python']
d = {s: len(s) for s in strings}
print(d)


#
# 369
#

for t in[(n,'짝'* (str(n).count('3') + str(n).count('6') + str(n).count('9')))
          for n in range(1, 1000) if '3' in str(n) or '6' in str(n) or '9' in str(n)]:
    print('%s: %s' % t)







