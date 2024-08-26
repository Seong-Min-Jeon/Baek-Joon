a=int(input())
if(a==1 or a==3 or a==4): print('SK')
elif(a==2): print('CY')
else:
    v=(a-4)%7
    if(v==1 or v==2 or v==4 or v==6 or v==0): print('SK')
    else: print('CY')