s=input()
c=0
for i in range(len(s)-3):
    if(s[i:i+4]=='kick'): c+=1
print(c)