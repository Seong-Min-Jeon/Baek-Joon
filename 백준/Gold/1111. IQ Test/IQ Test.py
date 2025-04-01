n=int(input())
l=list(map(int,input().split()))
if(len(l)<2): print('A'); exit()
if(len(set(l))==1): print(l[0]); exit()
x,y=l[0],l[1]
o=[]
for a in range(-200,201):
    b=y-x*a
    o.append((a,b))
for a,b in o.copy():
    for i in range(1,n-1):
        if(l[i]*a+b!=l[i+1]):
            o.remove((a,b))
            break
if(len(o)==0): print('B')
elif(len(o)>1): print('A')
else: print(l[-1]*o[0][0]+o[0][1])