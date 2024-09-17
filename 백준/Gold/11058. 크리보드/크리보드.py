a=int(input())
if(a<7): print(a); exit()
l=[0 for _ in range(a+1)]
for i in range(6):
    l[i]=i
if(a<7):
    print(a); exit()
for i in range(6,a+1):
    l[i]=max(l[i-3]*2,l[i-4]*3,l[i-5]*4)
print(l.pop())