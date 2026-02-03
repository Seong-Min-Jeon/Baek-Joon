I=input;I()
l=[*map(int,I().split())]
if(len(set(l))==1 and l[0]==1):
    print('cubelover' if len(l)%2==1 else 'koosaga')
    exit()
x=0
for e in l: x^=e
print('cubelover' if x==0 else 'koosaga')