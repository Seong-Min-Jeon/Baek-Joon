a=input()
s=set()
for l in range(len(a)):
    for i in range(len(a)-l):
        s.add(a[i:i+l+1])
print(len(s))