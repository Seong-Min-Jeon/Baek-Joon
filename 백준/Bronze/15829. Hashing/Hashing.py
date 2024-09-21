s=0
a=int(input())
e=input()
for i in range(a): s+=(ord(e[i])-96)*31**i
print(s%1234567891)