l=list(map(int,input().split()))
r=0
y=0
b=0
t=0
y+=int(input())
t=int(input())
y+=t/2
b+=t/2
b+=int(input())
t=int(input())
r+=t/2
b+=t/2
r+=int(input())
t=int(input())
r+=t/2
y+=t/2
r-=l[0]
y-=l[1]
b-=l[2]
if(r<0): r=0
if(y<0): y=0
if(b<0): b=0
if(int(r)!=r): r=(r*10)/10
else: r=int(r)
if(int(y)!=y): y=(y*10)/10
else: y=int(y)
if(int(b)!=b): b=(b*10)/10
else: b=int(b)
print(f'{r} {y} {b}')