# import sys
# I=sys.stdin.readline
# n=int(I())
# x=0
# for _ in range(n):
#     a,b=map(int,I().split())
#     l=[0]
#     for m in range(1,a+1):
#         g=set()
#         for k in range(10**6):
#             if(m-b**k<0): break
#             g.add(l[m-b**k])
#         for i in range(10**6):
#             if(i not in g):
#                 l.append(i)
#                 break
#     print(l)
#     x^=l[-1]
# print('Alice' if x else 'Bob')

'''
10 3
[0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
7 4
[0, 1, 0, 1, 2, 0, 1, 0]

15 4
[0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0]

홀수면 0101 반복
짝수면 0 1 0 1 ... 자기(2) 가 반복
'''

import sys
I=sys.stdin.readline
x=0
for _ in range(int(I())):
    a,b=map(int,I().split())
    if(b%2):
        if(a%2): x^=1
        else: x^=0
    else:
        a+=1;b+=1
        t=a%b
        if(a%b==0): x^=2
        else:
            if(t%2): x^=0
            else: x^=1
print('Alice' if x else 'Bob')