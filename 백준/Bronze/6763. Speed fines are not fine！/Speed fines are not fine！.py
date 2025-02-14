a=(int(input())-int(input()))*-1
s='You are speeding and your fine is $'
if(a<1): print('Congratulations, you are within the speed limit!')
elif(a<21): print(s+'100.')
elif(a<31): print(s+'270.')
else: print(s+'500.')