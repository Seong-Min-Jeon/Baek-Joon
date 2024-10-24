s=input()
l=['+']
for e in s:
   if(e=='+' or e=='-'): l.append(e); continue
   l[len(l)-1]+=e
for i in range(len(l)):
    if(l[i][0]=='-'):        
        a=int(l[i])*-1
        for j in range(i+1,len(l)):            
            if(l[j][0]=='+'):
                a+=int(l[j])
                l[j]='0'
            else: break
        l[i]=str(a*-1)
r=0
for e in l:
    r+=int(e)
print(r)