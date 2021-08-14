# 문제50 : 버블정렬 구현하기


'''
버블정렬은 두 인접한 원소를 검사하여 정렬하는 방법을 말합니다. 시간 복잡도는 느리지만 코드가 단순하기 때문에 자주 사용됩니다.

아래 코드의 빈 칸을 채워 버블 정렬을 완성해 봅시다.

def bubble(n, data):
	for i in range(n-1):
		for j in range(빈칸을 채워주세요):
			if data[j] > data[j+1]:
				빈칸을 채워주세요
	for i in range(n):
		print(data[i], end = " ")

n = int(input())
data = list(map(int, input().split()))

bubble(n, data)

'''


def bubble(n, data):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    for i in range(n):
        print(data[i], end=" ")


n = int(input())
data = list(map(int, input().split()))

bubble(n, data)
