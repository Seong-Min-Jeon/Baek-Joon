i=input()
l=[-2]*26
for a in range(26):
    if(chr(a+97) in i and l[a]==-2): l[a]=i.find(chr(a+97))
    else: l[a]=-1
print(*l)