#len 입력값이 길이를 리턴
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

#list 반복 가능한 자료형 s을 입력받아 리스트로 만들어 리턴하는 함수
print(list("python"))
print(list((1,2,3)))

a=[1,2,3]
b=list(a)
print(b)


#map 반복 가능한 자료형으르 입력으로 받는다. map은 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴
def two_times(numberList):
    result=[]
    for number in numberList:
        result.append(number*2)
    return result

result=two_times([1,2,3,4])
print(result)

#위에 코드를 map을 사용해 바꾼 코드
def two_times(x):return x*2

print(list(map(two_times,[1,2,3,4])))

#lambda 사용
print(list(map(lambda a:a*2,[1,2,3,4])))

#max 인수로 반복 가능한 자료형을 입력받아 그 최대값을 리턴
print(max([1,2,3]))
print(max("python"))


#min max함수와 반대로, 그 최소값을 리턴
print(min([1,2,3]))
print(min("python"))

#oct 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴
print(oct(34))
print(oct(12345))