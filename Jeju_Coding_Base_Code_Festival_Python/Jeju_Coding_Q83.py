# 문제 83 : 수학 괄호 파싱 2
'''


수학공식이 제대로 입력이 되었는지 판단하는 코드를 작성하려 합니다.
괄호는 소괄호와 중괄호가 있습니다.

입출력 예시


데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + 7 * {(3 * 5)}
True
데이터 입력(1), 프로그램 종료(2) : 1
데이터를 입력하세요: 5 + 7){ * (3 * 5)
False
데이터 입력(1), 프로그램 종료(2) : 2



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


def math(e):
    m = {
        ')': '(',
        '}': '{',
    }
    stack = []
    for i in e:
        if i in '({':
            stack.append(i)
        elif i in m:
            if len(stack) == 0:
                return False
            else:
                t = m[i]
                if t != stack.pop():
                    return False
    return len(stack) == 0


while 1:
    order = input('데이터 입력(1), 프로그램 종료(2) :')
    if order == '1':
        ex = input('데이터를 입력하세요 :')
        print(math(ex))
    else:
        break
