#여러 개의 입력값을 받는 함수 만들기

def sum_many(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum

result=sum_many(1,2,3)
print(result)

result=sum_many(1,2,3,4,5,6,7,8,9,10)
print(result)


def sum_mul(choice,*args):
    if choice=="sum":
        result=0
        for i in args:
            result=result+i
    elif choice=="mul":
        result=1
        for i in args:
            result=result*i
        return result

result=sum_mul("sum",1,2,3,4,5)
print(result)

result=sum_mul("mul",1,2,3,4,5)
print(result)

