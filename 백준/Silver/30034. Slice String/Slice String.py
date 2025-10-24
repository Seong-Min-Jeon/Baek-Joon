I=input
I();l=list(I().strip())
I();l+=list(I().strip())
I()
s=set(l)
for e in list(I().strip()):
    if(e in s): s.remove(e)
s.add(' ')
I()
t=[]
q=''
for e in I().strip():
    if(e in s): 
        if(q!=''): t.append(q); q=''
    else: q+=e
if(q!=''): t.append(q)
for e in t:
    print(e)