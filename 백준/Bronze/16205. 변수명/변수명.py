a,b=input().strip().split()
s=[]
q=''
if(a=='2'):
    for e in b:
        if(e=='_'):
            s.append(q)
            q=''
        else:
            q+=e
    s.append(q)
else:
    for e in b:
        if(65<=ord(e)<97):
            s.append(q)
            q=''
            q+=e.lower()
        else:
            q+=e
    s.append(q)
if(s[0]==''): s.pop(0)
a=s.copy()
for i in range(1,len(a)):
    a[i]=a[i][0].upper()+a[i][1:]
print(''.join(a))
b=s.copy()
for i in range(1,len(b)):
    b[i]='_'+b[i]
print(''.join(b))
a[0]=a[0][0].upper()+a[0][1:]
print(''.join(a))