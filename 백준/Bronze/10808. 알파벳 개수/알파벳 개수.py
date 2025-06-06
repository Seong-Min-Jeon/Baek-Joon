l=[0 for _ in range(26)]
for c in input(): l[ord(c)-97]+=1
print(*l)