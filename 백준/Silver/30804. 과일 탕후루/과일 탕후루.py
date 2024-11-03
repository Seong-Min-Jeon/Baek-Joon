input()
l=input().split()
a,b,c=0,0,0
t={}
t[l[0]]=t.get(l[0],1)
while True:
    if(len(t)<=2): 
        c=max(c,b-a+1)
        b+=1
        if(b>=len(l)): break
        t[l[b]]=t.get(l[b],0)+1       
    else:
        t[l[a]]=t.get(l[a],1)-1
        if(t[l[a]]==0): t.pop(l[a])
        a+=1        
print(c)