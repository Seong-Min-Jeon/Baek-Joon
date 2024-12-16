a=input()
if(len(a)==1):
    print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')
    exit()
b=0
b=int(a[0])-int(a[1])
for i in range(2,len(a)):
    if(int(a[i-1])-int(a[i])!=b):
        print('흥칫뿡!! <(￣ ﹌ ￣)>')
        exit()
print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!')