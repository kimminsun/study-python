def sum(a,b):
    return a+b

a=3
b=4
c=sum(a,b)
print(c)

#일반적인 함수의 전형적인 예
def sum(a,b):
    result=a+b
    return result

a=sum(3,4)
print(a)


#입력값이 없는 함수
def say():
    return 'HI'

a=say()
print(a)

#결과값이 없는 함수
def sum1(a,b):
    print("%d,%d의 합은 %d입니다" %(a,b,a+b))

sum1(3,4)


#입력값도 결과값도 없는 함수
def say():
    print('HI')

say()