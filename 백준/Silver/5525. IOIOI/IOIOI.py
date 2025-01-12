a=''.join(['IO' for _ in range(int(input()))])+'I'
p=[i for i in range(len(a)-1)]
p.insert(0,0)
l=int(input())
s=input()
c,i,j=0,0,0
while j<len(s):
    if(a[i]==s[j]):
        i+=1
        j+=1
        if(i==len(a)):
            c+=1
            i=p[i-1]
    else:
        if(i!=0): i=p[i-1]
        else: j+=1
print(c)