#int int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴하는 함수

print(int('3'))
print(int(3.4))

print(int('11',2))
print(int('1A',16))

#isinstance 첫 번째 인수로 인스턴스, 두 번째 인수로 클래스 이름을 받는다. 입력받은 인스턴스가 그 클래스의 인스턴스인지 판단하여
#참이면 TRUE 거짓이면 FALSE

class Person:pass

a=Person()
print(isinstance(a,Person))

b=3
print(isinstance(b,Person))


#lambda 함수를 생성할 때 사용하는 예약어, def와 동일한 역할을 한다.
#lambda 인수1,인수2, ... : 인수를 이용한 표현식

sum=lambda a,b:a+b
print(sum(3,4))


