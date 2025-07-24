l=[]
for _ in range(int(input())):
  if(len(l)==0): l=list(input().strip()); continue
  s=input().strip()
  for i in range(len(l)):
    if(l[i]!=s[i]): l[i]='?'
print(''.join(l))