import sys
import time
import tkinter as tk
from tkinter import *

from PIL import Image

# silence deprecation warning

root = Tk()
button1 = Button(root, text = "start", command = root.destroy)
button1.pack()
root.mainloop()

print("\nBased somewhat on Dan Brown's 'Angels and Demons' ")

def restart(funcname):
    restart = input("do you want to restart?   ")
    if restart == "yes":
        funcname()
    else:
        sys.exit()
    return 0

def image_resize(filename):
    basewidth = 200
    img = Image.open(filename)
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)    
    img.show(filename)
    time.sleep(2)
    return 0

def checkpoint():
    print("checkpoint")
    time.sleep(1)
    
    # joining up

def joining_up():
    join = input("\n\n<brother 1> do you want to join the illuminati?   ")
    if join == "yes":
        print ("<brother 1> welcome to the illuminati   ")
        time.sleep(2)
    else:
        print ("<brother 1> the secret has been divulged. You will die now.   ")
        time.sleep(2)
        print("you were stabbed in the face.")
        restart(joining_up)
joining_up()


# naming ceremony

name = input("<brother 2> what will you be called in our ranks?   ")
print ("<brother 2>",name,",you seem to be a valuable victi- we mean...asset.")
time.sleep(3.5)
checkpoint()

def first_mission():
    # first mission
    # giving items

    print ("<brother 3> ok",name,", we have got a mission for you.   ")
    accept = input ("<brother 3> do you want to accept it?   ")
    if accept != "yes":
        print (name,"was burned to death   ")
        restart(first_mission)
    else:
        print ("<brother 3> nice. good for you that you accepted this mission.\n<brother 3> you will need this.")
first_mission()
    

time.sleep(2.5)

image_resize('../data/walktalk.jpeg')         # walkie-talkie

image_resize('../data/rope.jpeg')             # rope

image_resize('../data/torch.jpeg')            # torch

image_resize('../data/coffee.jpeg')           # coffee

image_resize('../data/phone.jpeg')            # phone

image_resize('../data/mac.jpeg')              # mac

image_resize('../data/backpack.jpeg')         # backpack
time.sleep(1)

backpack = ["walkie-talkie","rope","torch","coffee","phone","mac"]

print("<brother 1> go on,",name,"accept these items (close the windows)")
time.sleep(12)

# the actual mission

print("<brother 2> so, your mission is to break into one of the minor vaults of our arch enemy 'The Church'.")
print("<brother 2> configure your mac so that we can send the location to you.\n\n")
    
class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
 
    def createWidgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "to configure mac\n"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.QUIT = tk.Button(self, text="quit", fg="red",
                                             command=root.destroy)
        self.QUIT.pack(side="bottom")

    def say_hi(self):
        print("""            -------------------------------------------
            |                                         |
            |                                         |
            |                   Welcome !             |
            |                                         |
            |                     To                  |
            |            Set up your password         |
            |                 press quit              |
            |               and click here            |
            |            ____________________         |
            |                                         |
            -------------------------------------------""")
root = tk.Tk()
app = Application(master=root)
app.mainloop()

password = input("<macbook> Set up your password   ")
print ("password has been set to '",password,"'.remember this.")
time.sleep(1)
print ("loading...")
time.sleep(3)
print("<siri> The location of the vault is - 'The halli bank' in Evera, Portugal")
time.sleep(5)
print("<brother 2> Go now. and may the all seeing eye be with you.")
time.sleep(2.5)
checkpoint()

image_resize("../data/timecard(eternity).jpg")

def on_the_way():
    #on your way

    time.sleep(2.5)

    print("<siri> you are currently 500 metres from the Louvre in Paris, France")
    louvre = input("<siri> do you want me to redirect you to the Louvre?   ")
    if louvre == "yes":
        print("<siri> ok. redirecting you to the Louvre. ")
    else:
        print(name,"was terminated by siri.")
        restart(on_the_way)
on_the_way()

# entering weapon's bunker 

time.sleep(2)
print("In front of the Louvre pyramid, you find a number pad with the Eye of Providence engraved on it.")
time.sleep(4)
passcode = int(input("what is the passcode?(3 numbers)   "))

while passcode != 522:
    passcode = int(input("access denied. try again.   "))

if passcode == 522:
    print("access granted.")
time.sleep(2)

print("*stone and metal grinding noises*")
time.sleep(1.5)
print("*secret doors open*")
time.sleep(1.2)
print("<brother 3>",name,"! there are people around you. why are you opening our weapon's bunker?")
time.sleep(3)

# choosing the weapons


while True:
    print("""<siri> your options are to:
    (E)liminate every watching person
    (I)nvisibility shield
    (L)eave the site""")
    weapon_door = input("what do you do?")
    copstat = 0
    if weapon_door.upper() == "E":
        print("everyone was terminated by siri")
        copstat += 1
        time.sleep(1)
        print("<siri> the cops have been alerted. you are now wanted for mass murder. beware,if you get 5 stars, you will die.")
        time.sleep(3.5)
        print("cop status:",copstat * "✯")
        break
    elif weapon_door.upper() == "I":
        print("<siri> invisibility shield has been activated. you can enter safely.")
        break
    else:
        print(name ,"was shot by a Louvre guard")

time.sleep(2.5)
print("inside the weapon's bunker, you find an arsenal of weapons. ")
time.sleep(2)


while True:

    weapons = input("""what do you choose (write them all at once with spaces):
    Weapons:                            
        1. Melee;                       durability : 7                   
            •(K)nife                        
            •(S)cythe                      
            •(H)ammer               
        2.ranged(light);                durability : 5
            •(D)esert eagle                   
            •(G)lock 45                       
            •(W)ebley MK IV                   
        3.ranged(heavy)                 durability : 3
            •(B)eretta AS70/90                
            •(H)eckler & Koch MG5             
            •(M)auser 45                      
            
            :""")

    # sorting

    if len(weapons) > 5 or len(weapons) < 5:
        print("you choose only 1 from each category")
        
    elif len(weapons) == 5:
        weapons_list = weapons.split()

        if weapons_list[0].upper() == "K":
            melee = "Knife"
            mdur = 7
        elif weapons_list[0].upper() == "S":
            melee = "Scythe"
            mdur = 7
        elif weapons_list[0].upper() == "H":
            melee = "Hammer"
            mdur = 7

        if weapons_list[1].upper() == "D":
            light = "Desert eagle"
            ldur = 5
        elif weapons_list[1].upper() == "G":
            light = "Glock 45"
            ldur = 5
        elif weapons_list[1].upper() == "W":
            light = "Webley MK IV"
            ldur = 5

        if weapons_list[2].upper() == "B":
            heavy = "Beretta AS70/90"
            hdur = 3
            break
        elif weapons_list[2].upper() == "H":
            heavy = "Heckler and Koch MG5"
            hdur = 3
            break
        elif weapons_list[2].upper() == "M":
            heavy = "Mauser 45"
            hdur = 3
            break

        else:
            print("try again")
            

print("you have chosen",melee,",",light,"and",heavy)
# going inside the Louvre

if copstat > 0:
    print("the louvre guard is about to shoot you for mass murder.")
    guard_kill = input(f"""what do you do?
    use the {melee}
    use the {light}
    use the {heavy}
    
    use the """)
    if guard_kill.title() == melee:
        print("the guard was violently killed by using the",melee)
        mdur -= 1
    elif guard_kill.title() == light:
        print("the guard was shot using",light)
        ldur -= 1
    elif guard_kill.title() == heavy:
        print("the guard is peppered with bullets from the",heavy)
        hdur -= 1
    else:
        print("instead of",guard_kill,"you punch him and he faints.")
        time.sleep(2)
        print("you have entered the louvre")
else:
    time.sleep(2)
    print("you have entered the louvre")

# inside the louvre

print("<brother 1>",name,""", good, you have successfully entered the louvre.
 Now, I want you to go and steal one of these items.
 You will find something to speed you to Evera.""")
time.sleep(4)
checkpoint()

# stealing fromt the louvre

def stealing():
    steal_item = input("""what do you want to steal?
    (T)he Mona lisa
    (M)arcus Aurelius's bust
    (B)ust of Socrates
    (R)aft of Medusa""")

    if steal_item.upper() == "T":
        print("behind the Mona Lisa, you find a wooden box")
        print("and inside the wooden box, you find…")
    elif steal_item.upper() == "M":
        print("behind the bust of Marcus Aurelius, you find a golden eggcup")
        print("and inside the eggcup, you find…")
    elif steal_item.upper() == "B":
        print("inside the bust of Socrates, you find a gold silk cover")
        print("and inside the cover, you find…")
    elif steal_item.upper() == "R":
        print("behind the painting, you find…")
    else:
        print(name,"was killed by the spirit of Bernini")
        restart(stealing)
stealing()

time.sleep(2)
print("a small metalltic device")

root = Tk()
button2 = Button(root, text = "teleport", command = root.destroy)
button2.pack()
root.mainloop()

# in Evera

print("<siri> you have been teleported to 'the halli bank' in Evera, Portugal")
time.sleep(2)
print("<clerk> hello sir, i see you want to create an account in our bank.")
bank_pass = input("<clerk> enter your password sir")

while True:
    if bank_pass != password:
        print("that does not seem to be your password sir. try again.")
    elif bank_pass == password:
        print("ok sir. you have successfully made an account with us. thank you.")
        break

print("<brother 1> hmm… good. now is the perfect opprtunity for you to steal from them")
time.sleep(3)
print("<brother 2> there is a back door to the bank. use that.")
time.sleep(2)
print("inside the room you find a cardboard door marked 'not the money vault'.")
time.sleep(3)
print("<brother 3> that has to be the money vault.")

    
sys.exit()
