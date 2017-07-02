import re
p=re.compile('[a-x]+')

#match
m=p.match("python")
print(m)

m=p.match("3 python")
print(m)


#search
m=p.search("python")
print(m)

m=p.search("3 python")
print(m)

