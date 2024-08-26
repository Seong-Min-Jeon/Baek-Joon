a=int(input())
# l=[0]*101
# for i in range(4):
#     l[4**i]=1
# for i in range(2, 101):
#     for j in range(4):
#         if(i>4**j and l[i-4**j]!=1): l[i]=1
# print(l)
if(a==1): print('SK')
else:
    v=(a-1)%5
    if(v==2 or v==3 or v==0): print('SK')
    else: print('CY')

#1 1 / S
#2 1 1 / C
#3 1 2 / S
#4 1 3 / 4 / S
#5 1 4 / 4 1 / C
#6 1 5 / 4 2 / S

'''
[0, 1, 
0, 1, 1, 0, 1, 
0, 1, 1, 0, 1, 
0, 1, 1, 0, 1, 
0, 1, 1, 0, 1, 
0, 1, 1, 0, 1, 
0, 1, 1, 0, 1,
'''