#bin to dec
def start():
    num=input("the random binary no. you want   ")
    #to restrict to only 0 and 1 
    e=0
    for blah in num:
        if int(num[e]) != 1 and int(num[e]) != 0:
            print("error...you try again or die")
            start()
        e+=1    
        #find length of number
    x=0
    a=int(num)
    while a>1:
        x+=1
        a=a/10
    #calculate binary
    sumx=0
    g=0
    for count in num:
        fn=int(num[g])*(2**x) + int(sumx)
        x-=1
        sumx=fn
        g+=1
    print(fn)
    print("HAHA!!!! I RULE THE WORLD NOW. BOW BEFORE ME")
    return fn    
start() 
