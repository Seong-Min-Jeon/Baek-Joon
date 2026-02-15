input()
r='0'
for e in input().strip():
    if(r[-1]==e): r=r[:-1]; r+=e.upper()*2
    else: r+=e
print(r[1:])