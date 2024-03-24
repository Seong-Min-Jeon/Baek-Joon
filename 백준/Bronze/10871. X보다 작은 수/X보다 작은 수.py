a=int(input().split()[1])
l=''
for i in map(int,input().split()):
    if i<a: l+=str(i)+' '
print(l)