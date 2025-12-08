I=input
F=lambda:map(float,I().split())
n=int(I())
a,b,c=[*F()],[*F()],[*F()]
s=0
for i in range(n):
    if(c[i]>1):
        t=a[i]*c[i]+0.000001
        s+=int(t)-b[i]
    else:
        t=b[i]*c[i]+0.000001
        s+=a[i]-int(t)
print(int(s))