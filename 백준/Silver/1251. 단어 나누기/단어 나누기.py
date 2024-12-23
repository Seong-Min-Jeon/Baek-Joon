s=input()
r='ㅇ'
for i in range(len(s)-1):
    for j in range(len(s)-1):
        if(i==j or i>j): continue
        a,b,c=s[:i+1],s[i+1:j+1],s[j+1:]
        a,b,c=a[::-1],b[::-1],c[::-1]        
        r=min(r,a+b+c)        
print(r)