#enumerate 열거하다
for i,name in enumerate(['body','foo','bar']):
    print(i,name)

#eval 실행가능한 문자열을 입력으로 받아 문자열을 실행한 결과값을 리턴
print(eval('1+2'))
print(eval("('hi'+'a')"))
print(eval('divmod(4,3)'))



#filter 걸러낸다. 첫 번째 인수로 함수 이름은 ,두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 자료형을 받는다
def positive(numberList):
    result=[]
    for num in numberList:
        if num>0:
            result.append(num)
    return result

print(positive([1,-3,2,0,5,6]))



def positive(x):
    return x>0

print(list(filter(positive,[1,-3,2,0,-5,6])))



#hex 정수값을 입력받아 16진수로 변환하여 리턴하는 함수
print(hex(234))
print(hex(3))


#id 객체를 입력받아 객체의 고유 주소값을 리턴하는 함수
a=3
print(id(3))
print(id(a))
b=a
print(id(b))

print(id(4))


#input 사용자 입력을 받는 함수이다
a=input()
print(a)

b=input("Enter : ")
print(b)




