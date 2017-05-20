#딕셔너리 관련 함수들
a={'name':'pey','phone':'1234455','birth':'1118'}
print(a.keys())

#value 리스트 만들기
print(a.values())

#key, value 쌍 얻기(items(
print(a.items())

#key:value 상 모두 지우기(clear)
a.clear()
print(a)

#key로 value 얻기
a={'name':'pey','phone':'1234455','birth':'1118'}
print(a.get('name'))

print(a.get('phone'))


#해당 key가 딕셔너리 안에 있는지 조사하기(in)
print('name' in a)
print('email' in a)