input()
l=list(map(int,input().split()))
j=l.pop(0)
for p in sorted(l):
    if(j>p): j+=p
    else: print('No'); exit()
print('Yes')