f=list(map(int,input().split()))
s=list(map(int,input().split()))
if(f[0]==f[2] and s[0]==s[2]):
    if(f[0]!=s[0]): print(0); exit()
    if(min(s[1],s[3]) <= f[1] and f[1] <= max(s[1],s[3])): print(1); exit()
    elif(min(s[1],s[3]) <= f[3] and f[3] <= max(s[1],s[3])): print(1); exit()
    elif(min(f[1],f[3]) <= s[1] and s[1] <= max(f[1],f[3])): print(1); exit()
    elif(min(f[1],f[3]) <= s[3] and s[3] <= max(f[1],f[3])): print(1); exit()
    else: print(0); exit()
if(f[0]==f[2]):
    a2=(s[1]-s[3])/(s[0]-s[2])
    b2=s[1]-a2*s[0]
    y=a2*f[0]+b2
    if(min(s[0],s[2]) <= f[0] and f[0] <= max(s[0],s[2]) and min(f[1],f[3])-y <= 10**-8 and -1*10**-8 <= max(f[1],f[3])-y): print(1); exit()
    else: print(0); exit()
if(s[0]==s[2]):
    a1=(f[1]-f[3])/(f[0]-f[2])
    b1=f[1]-a1*f[0]
    y=a1*s[0]+b1
    if(min(f[0],f[2]) <= s[0] and s[0] <= max(f[0],f[2]) and min(s[1],s[3])-y <= 10**-8 and -1*10**-8 <= max(s[1],s[3])-y): print(1); exit()
    else: print(0); exit()
a1=(f[1]-f[3])/(f[0]-f[2])
b1=f[1]-a1*f[0]
a2=(s[1]-s[3])/(s[0]-s[2])
b2=s[1]-a2*s[0]
if(a1-a2<=10**-8 and -1*10**-8<=a1-a2):
    if(b1-b2<=10**-8 and -1*10**-8<=b1-b2): 
        if(min(f[0],f[2]) <= s[0] and s[0] <= max(f[0],f[2]) and min(f[1],f[3]) <= s[1] and s[1] <= max(f[1],f[3])):
            print(1); exit()
        elif(min(f[0],f[2]) <= s[2] and s[2] <= max(f[0],f[2]) and min(f[1],f[3]) <= s[3] and s[3] <= max(f[1],f[3])):
            print(1); exit()      
        elif(min(s[0],s[2]) <= f[0] and f[0] <= max(s[0],s[2]) and min(s[1],s[3]) <= f[1] and f[1] <= max(s[1],s[3])):
            print(1); exit()
        elif(min(s[0],s[2]) <= f[2] and f[2] <= max(s[0],s[2]) and min(s[1],s[3]) <= f[3] and f[3] <= max(s[1],s[3])):
            print(1); exit()
        else:
            print(0); exit()
    else: print(0); exit()
x=(b2-b1)/(a1-a2)
y=a1*x+b1
if(min(f[0],f[2])-x <= 10**-8 and -1*10**-8 <= max(f[0],f[2])-x and min(f[1],f[3])-y <= 10**-8 and -1*10**-8 <= max(f[1],f[3])-y and
   min(s[0],s[2])-x <= 10**-8 and -1*10**-8 <= max(s[0],s[2])-x and min(s[1],s[3])-y <= 10**-8 and -1*10**-8 <= max(s[1],s[3])-y):
    print(1)
else:
    print(0)