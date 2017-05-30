a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)

print(result)


result=[num*3 for num in a]
print(result)


#[표현식 for 항목 in 반복 가능 객체 if 조건]

result=[x*y for x in range(2,10)
        for y in range(1,10)
        ]
print(result)