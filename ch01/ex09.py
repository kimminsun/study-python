#딕셔너리 쌍 추가,삭제하기

a={1:'a'}
a[2]='b'
print(a)

a['name']='pey'
print(a)

a[3]=[1,2,3]
print(a)

#딕셔너리 요소 삭제하기
del a[1]
print(a)

#딕셔너리에서 Key 사용해 Vlaue 얻기
grade={'pey':10,'jullet':99}
print(grade['pey'])
print(grade['jullet'])
