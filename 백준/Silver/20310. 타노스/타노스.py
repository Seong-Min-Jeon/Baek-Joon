s=input().strip()
a,b=s.count('0')//2,s.count('1')//2
t=''
for e in s[::-1]:
    if(e=='0' and a>0): a-=1
    else: t+=e
t=t[::-1]
r=''
for e in t:
    if(e=='1' and b>0): b-=1
    else: r+=e
print(r)