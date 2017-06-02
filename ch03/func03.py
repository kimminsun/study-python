#입력 인수에 초깃값 미리 설정하기
def say_myself(name,old,man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다")
    else:
        print("여자입니다")

say_myself("박응용",27)
say_myself("박응용",27,True)



#함수 안에서 함수 밖의 변수를 변경하는 방법
#return 이용하기
a=1
def vartest(a):
    a=a+1
    return a

a=vartest(a)
print(a)


#global 명령어 이용하기
a=1
def vartest():
    global a
    a=a+1

vartest()
print(a)