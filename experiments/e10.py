count = 1
judge = 0

# function even or odd 

def even_or_odd(num):
    if num %2 == 0:
        print(num, "is even and")
    elif num%2 == 1:
        print(num, "is odd and")
    else:
        print("invalid")
    return num

# function prime or not

def prime(count, judge):
    while count <= num1:
        if num1 % count == 0:
            judge += 1
            count += 1
        else:
            count += 1
    if judge == 2:
        print("prime")
    else:
        print("composite")
    return judge 

# main program

num1 = int(input('enter your no.   '))

even_or_odd(num1)

prime(count, judge)