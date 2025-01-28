a,b,c=map(int,input().split())
r=(a-11)*1440+(b-11)*60+(c-11)
if(r<0): print(-1)
else: print(r)