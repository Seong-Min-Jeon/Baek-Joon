s=input()
k,y='KOREA','YONSEI'
a,b=k,y
for e in s:
    if(e==k[0]): k=k[1:]
    if(e==y[0]): y=y[1:]
    if(k==''): print(a); break
    if(y==''): print(b); break