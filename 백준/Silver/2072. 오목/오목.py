import sys

def win(l:list,x:int,y:int):
    if(not [x-1,y] in l and [x+1,y] in l and [x+2,y] in l and [x+3,y] in l and [x+4,y] in l and not [x+5,y] in l):
        return True    
    elif(not [x-2,y] in l and [x-1,y] in l and [x+1,y] in l and [x+2,y] in l and [x+3,y] in l and not [x+4,y] in l):
        return True
    elif(not [x-3,y] in l and [x-2,y] in l and [x-1,y] in l and [x+1,y] in l and [x+2,y] in l and not [x+3,y] in l):
        return True
    elif(not [x-4,y] in l and [x-3,y] in l and [x-2,y] in l and [x-1,y] in l and [x+1,y] in l and not [x+2,y] in l):
        return True
    elif(not [x-5,y] in l and [x-4,y] in l and [x-3,y] in l and [x-2,y] in l and [x-1,y] in l and not [x+1,y] in l):
        return True
    if(not [x,y-1] in l and [x,y+1] in l and [x,y+2] in l and [x,y+3] in l and [x,y+4] in l and not [x,y+5] in l):
        return True    
    elif(not [x,y-2] in l and [x,y-1] in l and [x,y+1] in l and [x,y+2] in l and [x,y+3] in l and not [x,y+4] in l):
        return True
    elif(not [x,y-3] in l and [x,y-2] in l and [x,y-1] in l and [x,y+1] in l and [x,y+2] in l and not [x,y+3] in l):
        return True
    elif(not [x,y-4] in l and [x,y-3] in l and [x,y-2] in l and [x,y-1] in l and [x,y+1] in l and not [x,y+2] in l):
        return True
    elif(not [x,y-5] in l and [x,y-4] in l and [x,y-3] in l and [x,y-2] in l and [x,y-1] in l and not [x,y+1] in l):
        return True
    if(not [x-1,y-1] in l and [x+1,y+1] in l and [x+2,y+2] in l and [x+3,y+3] in l and [x+4,y+4] in l and not [x+5,y+5] in l):
        return True    
    elif(not [x-2,y-2] in l and [x-1,y-1] in l and [x+1,y+1] in l and [x+2,y+2] in l and [x+3,y+3] in l and not [x+4,y+4] in l):
        return True
    elif(not [x-3,y-3] in l and [x-2,y-2] in l and [x-1,y-1] in l and [x+1,y+1] in l and [x+2,y+2] in l and not [x+3,y+3] in l):
        return True
    elif(not [x-4,y-4] in l and [x-3,y-3] in l and [x-2,y-2] in l and [x-1,y-1] in l and [x+1,y+1] in l and not [x+2,y+2] in l):
        return True
    elif(not [x-5,y-5] in l and [x-4,y-4] in l and [x-3,y-3] in l and [x-2,y-2] in l and [x-1,y-1] in l and not [x+1,y+1] in l):
        return True
    if(not [x+1,y-1] in l and [x-1,y+1] in l and [x-2,y+2] in l and [x-3,y+3] in l and [x-4,y+4] in l and not [x-5,y+5] in l):
        return True    
    elif(not [x+2,y-2] in l and [x+1,y-1] in l and [x-1,y+1] in l and [x-2,y+2] in l and [x-3,y+3] in l and not [x-4,y+4] in l):
        return True
    elif(not [x+3,y-3] in l and [x+2,y-2] in l and [x+1,y-1] in l and [x-1,y+1] in l and [x-2,y+2] in l and not [x-3,y+3] in l):
        return True
    elif(not [x+4,y-4] in l and [x+3,y-3] in l and [x+2,y-2] in l and [x+1,y-1] in l and [x-1,y+1] in l and not [x-2,y+2] in l):
        return True
    elif(not [x+5,y-5] in l and [x+4,y-4] in l and [x+3,y-3] in l and [x+2,y-2] in l and [x+1,y-1] in l and not [x-1,y+1] in l):
        return True
    return False

a=int(sys.stdin.readline())
b=[]
w=[]
for i in range(a):
    x,y=map(int,sys.stdin.readline().split())    
    if(i%2==1):
        b.append([x,y])
        if(win(b,x,y)): 
            print(i+1)
            exit(0)
    else:
        w.append([x,y])
        if(win(w,x,y)):
            print(i+1)
            exit(0)
    if(i==a-1):
        print(-1)