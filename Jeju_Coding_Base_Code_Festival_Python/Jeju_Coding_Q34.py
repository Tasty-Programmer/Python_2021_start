# 문제 34 : sort 구현하기
'''
민주는 체육부장으로 체육시간이 되면 반 친구들이 제대로 키 순서대로 모였는지를 확인해야 한다.
그런데 요즘 민주는 그것이 너무 번거롭게 느껴져 한번에 확인하고 싶어한다.

>> 입력
176 156 155 165 166 169
>>출력
No
'''

height = input().split()
height_list = list(height)

if height_list[0] < height_list[2] :
    print('Yes')
else:
    print('No')
