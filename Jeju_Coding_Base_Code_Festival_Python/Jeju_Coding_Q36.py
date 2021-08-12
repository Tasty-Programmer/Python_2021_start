#문제 36 : 구구단 출력하기
'''
1~9 까지의 숫자 중 하나를 입력하면 그 단의 구구단 결과를 한줄에 출력하는 프로그램을 작성하세요.
>> 입력
2
>> 출력
2 4 6 8 10 12 14 16 18

'''

gugu = int(input())

while (gugu < 1 or gugu > 9):
    print('잘못입력')
    gugu = int(input('1~9  재 입력'))

for i in range(1,10):
    print(gugu*i)

