a=list(map(int,input().split()))
y=(a[2]*a[3]-a[0]*a[5])/(a[1]*a[3]-a[0]*a[4])
if(a[0]==0): x=(a[5]-a[4]*y)/a[3]
else: x=(a[2]-a[1]*y)/a[0]
print(int(x),int(y))