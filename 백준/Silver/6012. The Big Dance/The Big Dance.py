def f(t):
    global r
    if(len(t)==2): r+=t[0]*t[1]
    elif(len(t)==1): return
    else:
        c=len(t)//2
        if(len(t)%2!=0): c+=1
        f(t[:c])
        f(t[c:])
l=[i for i in range(1,int(input())+1)]
r=0
f(l)
print(r)