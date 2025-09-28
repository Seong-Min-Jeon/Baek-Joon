l=[[] for _ in range(8)]
l[0]=[2,3,5,7]
for i in range(1,8):
  for a in l[i-1]:
     for b in (1,3,7,9):
        n=10*a+b
        f=1
        for j in range(2,int(n**0.5)+1):
          if(n%j==0): f=0
        if(f): l[i].append(n)
for e in l[int(input())-1]: print(e)