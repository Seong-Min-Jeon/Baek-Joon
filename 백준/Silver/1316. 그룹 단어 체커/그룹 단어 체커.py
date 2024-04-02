a=int(input())
s=[]
c=''
e=0
for _ in range(a):
    b=input()
    for i in range(len(b)):
        d=b[i]        
        if d in s and d!=c:
            e+=1
            break
        elif d!=c:
            s.append(d)
            c=d
    s.clear()
    c=''
print(a-e)