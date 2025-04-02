s=input().strip()
r=set()
for c in s:
    if(c in r): r.remove(c)
    else: r.add(c)
print(len(r)-1 if len(r)>0 else 0)