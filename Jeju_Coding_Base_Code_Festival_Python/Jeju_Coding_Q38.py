#문제 38 : 호준이의 아르바이트
'''
호준이는 아르바이트로 영어 학원에서 단어 시험지를 채점하는 일을 하고있다. 호준이가 일하ㅐ는 학원은 매번 1위부터 3위까지의 학생에게 상으로
사탕을 준다. 그런데 오늘은 마침 사탕이 다 떨어져서 호준이가 채점을 하고
점수를 보내면, 당신이 아이들의 숫자만큼 사러 가기로했다.

학생들의 점수를 공백으로 구분하여 입력받는다. 1위 ~ 3위 학생은 여러명일 수 있고 1~3위 학생 중
중복되는 학생 까지 포함하여 사탕을 사기로 한다.

>> 입력
97 86 75 66 55 97 85 97 97 95

>> 출력
6
'''


user_input = input()

exam = list(user_input.strip().split())
exam = [int (i) for i in exam]

count = 3


data_sorted = sorted(list(exam))

print(data_sorted)
for i in range(len(exam)-1, 0, -1):
	if data_sorted[-3] == exam[i]:
		count += 1
print(count)