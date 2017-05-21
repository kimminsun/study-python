#자료형의 값을 저장하는 공간,변수
a=1
b="python"
c=[1,2,3]

#변수명= 변수에 저장할 값
#c언어나 java 처럼 변수의 자료형을 함께 쓸 필요는 없다.


a=3
b=3
print(a is b)


#변수를 만드는 여러가지 방법
a,b=('python','life')

(a,b)='python','life'

[a,b]=['python','life']

a=b='python'

#파이썬에서는 두 변수의 값을 아주 간단히 바꿀 수 있다
a=3
b=5
a,b=b,a
print(a)
print(b)

