#문제 26 : 행성 문제2
'''
우리 태양계를 이루는 행성은 수성, 금성 , 지구, 화성,  목성, 토성, 천왕성 , 해왕성 이 있습니다.
이ㅅ행성들의 영어 이름은 Mecury, Venus, Earth, Mars, Jupiter, Saturn,Uranus,Neptune 입니다.

행성의 한글 이름을 입력하면 영어 이름을 반환하는 프로그램을 만들어주세요.

>> 입력
지구
>> 출력
Earth
'''
planet = {'지구':'Mercury', '금성':'Venus','지구':'Earth','화성':'Mars',
          '목성':'Jupiter','토성':'Saturn','천왕성':'Uranus','해왕성':'Neptune'}
key = input()
print(planet.get(key))