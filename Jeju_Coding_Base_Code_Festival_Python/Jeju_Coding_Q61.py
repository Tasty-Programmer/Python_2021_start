# 문제 61 : 문자열 압축하기

'''

문자열을 입력받고 연속되는 문자열을 압축해서 표현하고싶습니다.


>> 입력
aaabbbbcdddd

>> 출력
a3b4c1d4
'''

import re

input_data = 'aaabbccccccasss'
rule = re.compile('[a-c]+')

one = re.findall('b', input_data)
two = re.findall(rule, input_data)
three = re.findall('(\\w)(\\1*)', input_data)

print(one)
print(two)
print(three)

s = ''
for i, j in three:
    s += str(len(j)+1)+i
print(s)