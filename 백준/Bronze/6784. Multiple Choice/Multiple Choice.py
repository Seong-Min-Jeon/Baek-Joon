I=input;n=int(I())
a,b=[I() for _ in range(n)],[I() for _ in range(n)]
print(sum([a[i]==b[i] for i in range(n)]))