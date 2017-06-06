#파일에 새로운 내용 추가하기
f=open("새파일.txt",'a')
for i in range(11,20):
    data="%d번째 줄 입니다.\n" %i
    f.write(data)
f.close()

#with문과 함께 사용하기
f=open("foo.txt",'w')
f.write("Life is too short, you need python")
f.close()

with open("foo.txt","w") as f:
    f.write("Life is too short, you need python")

