#문자열 포매팅

print("I eat %d apples."%3)

print("I eat %s apples." %"five")


number=3

print("I eat %d apples."%number)

number=10
day="three"

print("I ate %d aples. so I was sick for %s days."%(number,day))

#문자열 포매팅은 다양한 것들을 대입시킬 수 있다
#부동소수,8,16진수,Literal 등등

print("Error is %d%%." %98)



#포맷 코드와 숫자 함께 사용하기

print("%10s"%"hi")
print("%-10sjane."%'hi')
