a,b,c=int(input()),0,0
while a > b:    
    c+=1
    b+=c
a-=b-c
if c%2==0: print(f'{a}/{c+1-a}')
else: print(f'{c+1-a}/{a}')