# 문제81 : 지뢰찾기

'''
지뢰를 찾는 문제입니다.
다음 그림처럼 깃발 주위에는 지뢰가 사방으로 있습니다.
깃발의 위치를 입력받아 지뢰와 함께 출력해주는 프로그램 을 만드세요.

- 아래 Case 외 예외 사항은 고려하지 않습니다.
(예를 들어 깃발이 붙어 있을 경우는 고려하지 않습니다.)
실력이 되시는 분들은 깃발이 붙어있을 상황까지 고려해주세요


데이터
flag = [] #지뢰 없이 깃발만 있는 리스트
minesweeper = [] #지뢰를 찾은 리스트
for i in range(5):
    flag.append(input('깃발 값과 함께 입력하세요 :').split(' '))

pass
print(flag)
print(minesweeper)

>> 입력
0 1 0 0 0
0 0 0 0 0
0 0 0 1 0
0 0 1 0 0
0 0 0 0 0

>> 출력
* f * 0 0
0 * 0 * 0
0 0 * f *
0 * f * 0
0 0 * 0 0

'''


value ='''0 1 0 0 0
    0 0 0 0 0
    0 0 0 1 0
    0 0 1 0 0
    0 0 0 0 0'''
    print(value.split('\n'))
    sp = value.split('\n')
    count = 0
    for i in sp:
        sp[count] = i.replace('1', 'f').split(' ')
        count += 1
    print(sp)
    count = 0
    search = 0
    for s in sp:
        for i in s:
            if i == 'f':
                search = s.index(i)
                if search > 0:
                    s[search-1] = '*'
                if search < 4:
                    s[search+1] = '*'
                if count > 0:
                    sp[count-1][search] = '*'
                if count < 4:
                    sp[count+1][search] = '*'
        count += 1
    for i in sp:
        print(i)
