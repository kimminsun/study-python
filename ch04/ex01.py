# 예외 처리

#--> 에러발생
#f=open("나없는파일",'r')
try:
    f=open("foo.txt",'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data=f.read()
    f.close()

#--> 에러발생
#print(4/0)
try:
    4/0
except ZeroDivisionError as e:
    print(e)
#-->에러발생
#a=[1,2,3]
#print(a[4])


#오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    def fly(self):
        print("very fast")
eagle=Eagle()
eagle.fly()



