# 문제65 : 변형된 리스트

'''

a = [1,2,3,4]
b = [a,b,c,d]
이런 리스트가 있을 때 [[1,a],[b,2],[3,c],[d,4]] 이런식으로 a,b리스트가 번갈아가면서 출력되게 해주세요.

'''

a = input().split(' ')
b = input().split(' ')

c = []
count = 0

for i, j in zip(a, b):
    if count % 2 == 0:
        c.append([i, j])
    else:
        c.append([j, i])
    count += 1

print(c)
