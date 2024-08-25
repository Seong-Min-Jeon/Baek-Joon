a,b=map(int,input().split()); s=''; c,m=0,32
d='BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB'
for _ in range(a):
    s+=input()
for i in range(b-7):
    for j in range(a-7):
        for k in range(64):
            e=i+b*(j+k//8)+k-8*(k//8)
            if(s[e]!=d[k]): c+=1
        if(c>32): c=64-c
        if(m>c): m=c
        c=0
print(m)