a,b=input().strip().split()
if(len(a)!=len(b)): print(0)
elif('8' not in a): print(0)
elif('8' not in b): print(0)
else:
    for i in range(len(a)):
        if(a[i]!=b[i]): break
    print(min(a[:i+1].count('8'),b[:i+1].count('8')))