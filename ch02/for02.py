#range 함수 예시 살펴보기
sum=0
for i in range(1,11):
    sum+=i
    print(sum)

marks=[90,25,67,45,80]
for number in range(len(marks)):
    if marks[number]<60: continue
    print("%d번 학생 축하합니다. 합격입니다" %(number+1))

for i in range(2,10):
    for j in range(1,10):
        print(i*j,end=" ")
        print('')