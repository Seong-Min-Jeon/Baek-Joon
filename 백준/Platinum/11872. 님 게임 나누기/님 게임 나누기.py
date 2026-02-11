I=input;I();x=0
for e in map(int,I().split()):    
    if(e%4==0): x^=e-1
    elif(e%4==3): x^=e+1
    else: x^=e
print('koosaga' if x else 'cubelover')

# l=[0,1]
# for g in range(2,20):
#     s=set()
#     for i in range(g):
#         s.add(l[i])
#     for i in range(1,g):
#         s.add(l[i]^l[g-i])
#     for n in range(100):
#         if(n not in s):
#             l.append(n)
#             break
# print(l)
# [0, 1, 2, 4, 3, 5, 6, 8, 7, 9, 10, 12, 11, 13, 14, 16, 15, 17, 18, 20]