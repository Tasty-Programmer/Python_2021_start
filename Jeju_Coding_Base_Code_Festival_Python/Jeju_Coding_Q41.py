#문제41 : 소수판별

'''
숫자가 주어지면 소수인지 아닌지 판별하는 프로그램을 작성해주세요.
소수이면 YES로, 소수가 아니면 NO로 출력해주세요.
(소수 : 1과 자기 자신만으로 나누어떨어지는 1보다 큰 양의 정수)

>> 입력
11
>> 출력
YES
>> 입력
6
>> 출력
NO
'''


def check_prime(n):
    i = 2
    while i < n:
        if n % i == 0:
            break
        i = i + 1
    if i == n:
        print("YES")
    else:
        print("NO")
check_prime(int(input()))

