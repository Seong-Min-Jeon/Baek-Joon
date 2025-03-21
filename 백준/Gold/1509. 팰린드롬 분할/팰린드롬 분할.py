s=input().strip()
l=[i for i in range(len(s)+1)]
for i in range(len(s)):
    for j in range(i+1):
        b=1
        if(l[j]+1>=l[i+1]): continue
        for k in range((i-j+1)//2):
            if(s[i-k]!=s[j+k]): b=0; break
        if(b): l[i+1]=min(l[i]+1,l[j]+1)
print(l[-1])