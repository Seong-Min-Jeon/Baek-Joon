def f1(x):
    if(x=='.'): return
    print(x,end='')
    f1(t[x][0])
    f1(t[x][1])

def f2(x):
    if(x=='.'): return    
    f2(t[x][0])
    print(x,end='')
    f2(t[x][1])

def f3(x):
    if(x=='.'): return    
    f3(t[x][0])
    f3(t[x][1])
    print(x,end='')

t={}
for i in range(int(input())):
    x,y,z=input().split()
    t[x]=[y,z]
f1('A')
print()
f2('A')
print()
f3('A')