# 문제45 : time함수 사용하기

'''

python의 모듈 중 하나인 time 모듈은 1970년 1월 1일 0시 0분 0초 이후로부터 지금까지 흐른 시간을 초단위로 반환합니다

이를 이용하여 현재 연도(2021)를 출력해보세요

'''

import time
t = time.time()
t = int(t//(3600*24*365))+1970
print(t)