input()
f,c,r=0,0,0
for e in input().strip():
    if(f==0 and e=='A'): f=1
    elif(f==1 and e=='A' and c==1): r+=1; c=0
    elif(f==1 and e=='A'): c=0
    elif(f==1 and e=='N'): c+=1
print(r)