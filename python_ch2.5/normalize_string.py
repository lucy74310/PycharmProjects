# 문자열 데이터를 분석하기 전에 처리함수 만들기
# 1. 공백제거
# 2. 필요 없는 문자 보호 제거
# 3. 대소문자 정리(Capitalize)
import re

states = ['Alabama', ' Georgia!', 'Georgia ', 'georgia',
          'FlOrIda', 'south #carolina   ', 'West virginia?']


def clean_string(strings):
    for string in strings:
        string = string.strip()
        string = re.sub('[!#?]', '', string)
        string = string.title()

        results.append(string)
    print(states)
    return results


results = []
print(clean_string(states))


def clean_string(strings, *funcs):
    results = []
    for string in strings:
        for func in funcs:
            string = func(string)

        results.append(string)
    return results


def remove_special(s):
    return re.sub('[!#?]', '', s)


# lambda 여러줄 지원 안한다. (JAVA 는 지원함)
states = clean_string(states, str.strip, str.title, lambda s: re.sub('[!#?]', '', s))

print(states)

ex1 = " abc  ".strip()
ex2 = str.strip(" abc ")
print('---', ex1, '---', sep='')
print('---', ex2, '---', sep='')










