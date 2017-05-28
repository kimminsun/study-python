test_list=['one','two','three']
for i in test_list:
    print(i)


#다양한 for문의 사용
a=[(1,2),(3,4),(5,6)]
for(first,last) in a:
    print(first+last)


#for문의 응용
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark>=60:
        print("%d번 학생은 합격입니다."%number)
    else:
        print("%d번 학생은 불합격입니다."%number)


#for문과 continue
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark<60 :continue
    print("%d번 학생 축하합니다. 합격입니다 "%number)

#for와 함께 자주 사용하는 range 함수
a=range(10)
print(a)

a=range(1,11)
print(a)