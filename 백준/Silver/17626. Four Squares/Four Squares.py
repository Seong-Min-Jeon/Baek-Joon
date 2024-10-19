a=int(input())
b=0
for i in range(224):
    for j in range(224):
        for k in range(224):
            if(i**2+j**2+k**2==a):
                c=0
                if(i!=0): 
                    c+=1
                if(j!=0): 
                    c+=1
                if(k!=0): 
                    c+=1
                print(c)
                exit()
print(4)                