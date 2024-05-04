x,y,w,h=map(int,input().split())
l=[]
l.append(w-x)
l.append(h-y)
l.append(x-0)
l.append(y-0)
l.sort()
print(l[0])