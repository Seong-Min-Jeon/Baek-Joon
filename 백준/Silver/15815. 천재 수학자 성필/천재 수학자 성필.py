l=list(input().strip())
s=[]
for e in l:    
    if(e in ('+','-','*','/')): 
        a,b=s.pop(),s.pop()
        s.append(str(int(eval(b+e+a))))
    else: s.append(e)
print(*s)