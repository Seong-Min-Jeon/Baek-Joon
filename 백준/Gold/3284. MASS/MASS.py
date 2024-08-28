s=list(input())
i=0
while i < len(s):
    if(s[i]=='('):
        a=0
        for j in range(i+1, len(s)):            
            if(s[j]==')' and a==0):
                s[i]='#'
                s[j]='#'                
                if(j+1<len(s) and s[j+1].isdigit()):
                    v=int(s[j+1])
                    s[j+1]='#'
                    for k in range(v-1):
                        for l in range(j-1, i, -1):                            
                            s.insert(j, s[l])                
                break
            if(s[j]=='('):
                a+=1
            elif(s[j]==')'):
                a-=1
    if(s[i].isdigit() and s[i-1].isalpha()):
        v=int(s[i])
        s[i]='#'
        for j in range(v-1):  
            s.insert(i, s[i-1])
    i+=1
v=0
for i in s:
    if(i=='H'): v+=1
    if(i=='C'): v+=12
    if(i=='O'): v+=16
print(v)