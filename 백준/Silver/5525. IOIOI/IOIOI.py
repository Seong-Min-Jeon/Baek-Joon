p=''
for _ in range(int(input())):
    p+='IO'
p+='I'
l=int(input())
s=input()
c=0
for i in range(l):
    if(s[i]=='I' and i+len(p)-1<l):
        t=s[i:i+len(p)]
        if('OO' not in t and 'II' not in t):
            c+=1
print(c)