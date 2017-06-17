#open 파일 객체를 리턴하 함수

#f=open("binary_file","rb")


#ord 문자의 아스키 값을 리턴
print(ord('a'))
print(ord('0'))

#pow 제곱한 결과를 리턴
print(pow(2,4))
print(pow(3,3))

#range for문과 함께 자주 사용. 입력받은 숫자에 해당되는 범위의 값을 반복 가능하나 객채로 만들어 리턴
print(list(range(5)))
print(list(range(5,10)))

print(list(range(1,10,2)))
print(list(range(0,-10,-1)))

#sorted 입력값을 정렬한 후 그 결과를 리스트로 리턴
print(sorted([3,1,2]))
print(sorted(['a','b','c']))
print(sorted("zero"))
print(sorted((3,2,1)))

#str 문자열 형태로 객체를 변환하여 리턴
print(str(3))
print(str('hi'))
print(str('hi'.upper()))


#tuple 반복 가능한 자료형으르 입력받아 튜플 형태로 바꾸어 리턴하는 함수
print(tuple("abc"))
print(tuple([1,2,3]))

#type 입력밧의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type([]))
print(type(open("test",'w')))

#zip 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
print(list(zip([1,2,3],[4,5,6])))