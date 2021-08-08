# 문제 16 : 로꾸거

'''
문장이 입력되는 거꾸로 출력하는 프로그램을 만들어 봅시다.

>> 입력
거꾸로

>> 출력

로꾸거


'''

yourWord = input("")
newWord = ""


for s in  yourWord:
    newWord = s+ newWord


print(newWord)


# yourWord2 = input("")
# print(yourWord2[::-1])
# 이런 방식으로도 가능하다! print (바꿀변수[::-1])