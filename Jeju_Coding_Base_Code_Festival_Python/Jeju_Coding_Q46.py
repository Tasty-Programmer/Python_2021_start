#문제46 : str 자료형의 응용

'''

1부터 100까지의(100을 포함) 모든 숫자를 일렬로 놓고 모든 자릿수의 총 합을 구하세요.

예를 들어 10부터 15까지의 모든 숫자를 일렬로 놓으면 101112131415이고 각 자리의 숫자를 더하면 25입니다.

'''

s = ''
for i in range(101):
    s += str(i)
print(s)
result = 0
for i in s:
    result += int(i)
print(result)