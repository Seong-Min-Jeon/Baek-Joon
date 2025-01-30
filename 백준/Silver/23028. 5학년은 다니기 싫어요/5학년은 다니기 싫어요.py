n,a,b=map(int,input().split())
for _ in range(8-n):
    x,y=map(int,input().split())
    a+=min(18,x*3)
    b+=min(18,(x+y)*3)
if(a>=66 and b>=130): print('Nice')
else: print('Nae ga wae')