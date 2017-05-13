#문자열 관련 함수

#문자 개수 세기
a="hobby"
print(a.count('b'))

#위치 알려주기 (find) 찾고자 하는 문자열이 처음 나온 위치를 리턴
a="Python is best choice"
print(a.find('b'))
print(a.find('k'))

#위치 알려주기 (Index)
a="Life is too short"
print(a.index('t'))
#print(a.index('k')) 없는 문자열을 쓴다면 오류 발생

#문자열 삽입(join)
a=","
print(a.join('abcd'))

#소문자를 대문자 & 소문자로 바꾸기
a="hi"
print(a.upper())
a="HI"
print(a.lower())


#문자열 바꾸기
a="Life is too short"
print(a.replace("Life","Your Leg"))


#문자열 나누기
a="Life is too short"
print(a.split())

