#문제 31 : 파이썬 자료형의 복잡도

'''
다음 리스트의 내장함수의 시간복잡도가 O(1)이 아닌것은?

1) l[i]
2) l.append(5)
3)l[a:b]
4)l.pop()
5)l.clear()
'''

#1번은 index O(1), 2번은 append로 역시 O(1), 3번은 slice 로  O(b-a) 로 정답은 3번! 4번 clear 와 pop 또한 O(1)입니다.