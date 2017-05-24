#리스트 관련 함수들

a=[1,2,3]
a.append(4)
print(a)

a.append([5,6])
print(a)

#리스트 정렬(sort)
a=[1,4,3,2]
a.sort();
print(a)

#알파벳순서도 정렬가능
a=['a','c','b']
a.sort()
print(a)

#리스트뒤집기
a=['a','c','b']
a.reverse()
print(a)

#위치반환
a=[1,2,3]
print(a.index(3))

#리스트 요소 삽입
a=[1,2,3]
a.insert(0,4)
print(a)

a.insert(3,5)
print(a)

#리스트 요소 제거(remove)
a.remove(3)
print(a)

#리스트 요소 끄집어내기
a.pop()
print(a)

#pop(x)는 리스트의 x번째 요소를 돌려주고 요소는 삭제한다
a=[1,2,3]
a.pop(1)
print(a)


#리스트에 포함된 요소 x의 개수 세기(count)
a=[1,2,3]
print(a.count(1))


#리스트 확장
a=[1,2,3]
a.extend([4,5])
print(a)


