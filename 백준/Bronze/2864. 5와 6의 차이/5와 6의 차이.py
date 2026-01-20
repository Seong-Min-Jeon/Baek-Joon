a,b=input().strip().split()
x,y=a.replace('6','5'),b.replace('6','5')
n,m=a.replace('5','6'),b.replace('5','6')
print(int(x)+int(y),int(n)+int(m))