import operator
a=input().lower()
m=dict()
for i in range(len(a)):
    if(a[i] in m):
        m[a[i]]=m.get(a[i])+1
    else:
        m[a[i]]=1
d=sorted(m.items(),key=operator.itemgetter(1),reverse=True)
if(len(d)==1):
    print(d[0][0].upper())
    exit()
if(d[0][1]!=d[1][1]):
    print(d[0][0].upper())
else: print('?')