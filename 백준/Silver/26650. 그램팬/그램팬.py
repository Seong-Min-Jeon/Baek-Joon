s=input()+'#'
c=0
l=[]
for e in s:
    if(len(l)==0): 
        if(ord(e)==65): l.append(ord(e))
    else:
        if(ord(e)-l[len(l)-1]==1 or ord(e)-l[len(l)-1]==0): 
            l.append(ord(e))
        else: 
            c+=l.count(65)*l.count(90)
            l=[]
            if(ord(e)==65): l.append(ord(e))
print(c)