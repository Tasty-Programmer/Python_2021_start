# 문제 37 : count 사용하기

'''
새 학기를 맞아 은비네 반은 반장 선거를 하기로 했습니다. 그런데 표를 하나씩 개표하는 과정이 너무
번거롭게 느껴진 당신은 학생들이 뽑은 후보들을 입력받으면 뽑힌 학생의 이름과 받은 표 수를 출력하는
프로그램을 작성하기로 하였습니다.

>> 입력
첫 줄에 학생들이 뽑은 후보들이 입력됩니다.
원영 원영 은비 은비 은비 은비 채연 채연
>> 출력
출력은 "은비가 총 4표로 반장이 되었습니다." 와 같습니다.
은비(이)가 총 4표로 반장이 되었습니다.
'''

lists = input().strip().split()
count = {}

for i in lists:
    try:
        count[i] += 1
    except:
        count[i] = 1

max_key = max(count)
max_val = max(count.values())

print("{0}(이)가 총 {1}표로 반장이 되었습니다.".format(max_key, max_val))

data = list(map(str, input().split()))
count = 0
for i in range(len(data)):
    if data.count(data[i - 1]) < data.count(data[i]):
        count = i
print("{}(이)가 총 {}표로 반장이 되었습니다.".format(data[count], data.count(data[count])))
