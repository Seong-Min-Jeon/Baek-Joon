a=b=c=2; d=e=f=3; g=h=i=4; j=k=l=5; m=n=o=6; p=q=r=s=7; t=u=v=8; w=x=y=z=9
st=input().lower()
to=0
for ch in st:
    to+=globals()[ch]
print(to+len(st))