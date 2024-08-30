c=100
a=input()
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        m=a[i:j]
        b=a.replace(m,'M')        
        c=min(c,len(b)+len(m))
if(c>len(a)):
    c=len(a)
print(c)