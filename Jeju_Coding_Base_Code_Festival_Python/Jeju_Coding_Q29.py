#문제 29 : 대문자만 지나가세요

'''
진구는 영어 학원 아르바이트를 하고 있습니다. 반 아이들은 알파벳을 공부하는 학생들인데 오늘은 대문자 쓰기 시험을 봤습니다.

알파벳 하나만을 입력하고 그 알파벳이 대문자이면 YES 를 아니면 NO 를 출력하는 프로그램을 만들어주세요

>> 입력
A
>> 출력
YES
>> 입력
d
>> 출력
NO
'''


ALP = input()
if ALP.isupper() == True:
    print('Yes')
else:
    print('No')
