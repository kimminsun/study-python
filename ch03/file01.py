#파일 읽고 쓰기
f=open("새파일.txt",'w')
f.close()


#파일을 쓰기 모드로 열어 출력값 적기
f=open("새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄 입니다.\n" %i
    f.write(data)
f.close()


#프로그램의 외부에 저장된 파일을 읽는 여러 가지 방법

#readline 함수 이용하기
f=open("새파일.txt",'r')
while True:
    line=f.readline()
    if not line:break
    print(line)
f.close()


#readlines() 함수 이용하기
f=open("새파일.txt",'r')
lines=f.readlines()
for line in lines:
    print(line)
f.close()



