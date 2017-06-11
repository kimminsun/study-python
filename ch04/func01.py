#abs 절대값

print(abs(3))
print(abs(-3))
print(abs(-1.2))


#all 모두 참이면 True, 하나라도 거짓이면 False
print(all([1,2,3]))
print(all([1,2,3,0]))


#any 하나라도 참이 있을 경우 True,모두 거짓일 경우에만 False all과 반대경우이다
print(any([1,2,3,0]))
print(any([0,""]))


#chr 아스키코드값을 입력받아 그 코드에 해당하는 문자를 출력
print(chr(97))
print(chr(48))

#dir 객체가 자체적으로 가지고 있는 변수나 함수를 보여 준다
print(dir([1,2,3]))
print(dir({'1':'a'}))

#divmod 2개의 숫자를 입력받고 a를 b로 나눈 몫과 나머지를 튜플 형으로 리턴
print(divmod(7,3))
print(divmod(1.3,0.2))
