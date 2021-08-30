# 문제 82 : 수학괄호 파싱

'''

수학공식이 제대로 입력이 되었는지 판단하는 코드를 작성하려 합니다. 괄호는 소괄호 밖에 없습니다.

입출력 예시


데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 3 + 5
True

데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + 7) * (3 * 5)
False



def math(e):

		<코드를 작성해주세요>

while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break


'''


def sol():
    i = 0
    while i != 2:
        i = int(input("데이터 입력(1), 프로그램 종료(2) :"))
        if i == 2:
            break
        d = list(input("데이터를 입력하세요: "))
        step =0
        for i in d:
            if i =="(":
                step += 1
            elif i==")":
                step -=1

            if step !=0:
                return print(False)
        if step==0:
            return print(True)
sol()
