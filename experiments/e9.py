import random
dice1 = 0
dice2 = 0
comb = ()

def dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    print(dice1, dice2)
    return dice1, dice2
dice()
    
    
