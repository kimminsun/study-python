#x in s,x not in s

print (1 in [1,2,3])
print(1 not in[1,2,3])


pocket=['paper','cellphone','money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")



#다양한 조건을 판단하는 elif

pocket=['paper','cellphone']
card=1
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")

if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")