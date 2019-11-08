import random
pos=0
count=0
while(pos<100):
    if(pos==95):                                        #if pos if greater than or equal to 95 this if block will run
        roll=input("roll dice")
        dice=random.randrange(1,7)
        if(dice==6):
            pos=95
            print("you can't move",pos)
        elif(dice==5):
            print(dice)
            pos=100
            print("your current block is :",pos)
        elif(dice==4):
            print(dice)
            pos=99
            print("your current block is :",pos)
        elif(dice==3):
            print(dice)
            pos=98
            print("your current block is :",pos)
        elif(dice==1):
            print(dice)
            pos=97
            print("your current block is :",pos)
        count+=1
    elif(pos==96):
        roll=input("roll dice")
        dice=random.randrange(1,7)
        if(dice==6)or(dice==5):
            pos=96
            print("you can't move",pos)
        elif(dice==4):
            print(dice)
            pos=100
            print("your current block is :",pos)
        elif(dice==3):
            print(dice)
            pos=99
            print("your current block is :",pos)
        elif(dice==2):
            print(dice)
            pos=98
            print("your current block is :",pos)
        elif(dice==1):
            print(dice)
            pos=97
            print("your current block is :",pos)
        count+=1 
    elif(pos==97):
        roll=input("roll dice")
        dice=random.randrange(1,7)
        if(dice==6)or(dice==5)or(dice==4):
            pos=97
            print("you can't move",pos)
        elif(dice==3):
            print(dice)
            pos=100
            print("your current block is :",pos)
        elif(dice==2):
            print(dice)
            pos=99
            print("your current block is :",pos)
        elif(dice==1):
            print(dice)
            pos=98
            print("your current block is :",pos)
        count+=1
    elif(pos==98):
        roll=input("roll dice")
        dice=random.randrange(1,7)
        if(dice==6)or(dice==5)or(dice==4)or(dice==3):
            pos=98
            print("you can't move",pos)
        elif(dice==2):
            print(dice)
            pos=100
            print("your current block is :",pos)
        elif(dice==1):
            print(dice)
            pos=99
            print("your current block is :",pos)
        else:
            print("no moves",pos)
            count+=1
    else:
        roll=input("roll dice")
        dice=random.randrange(1,7)
        count+=1
        print(dice)
        if(pos<=96):
            if(dice==6):                                    #if dice fall 6(and ignore all other condition until another chance is given)
                pos=pos+dice
                print("your current block is :",pos,
                  """ YUP YUPY!
Ignore LADDER or SNAKE wait until next move coz previous dice was 6""")
                if(pos>=95):
                    print("can't roll the dice ")
                else:
                    roll=input("ANOTHER CHANCE TO ROLL DICE")
                    dice=random.randrange(1,7)
                    print(dice)
                    pos=pos+dice
                    print("your current block is :",pos)
            else:                                           #if dice fal 1 to 5
                pos=pos+dice
                print("your current block is :",pos)
        

  
        
    #ladder block

    
    if(pos==7): #ladder1
        pos=11
        print("hurry! you climbed ladder and current block is : ",pos)
    if(pos==20): #ladder2
        pos=38
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==28): #ladder3
        pos=65
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==36): #ladder4
        pos=44
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==42): #ladder5
        pos=63
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==51): #ladder6
        pos=67
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==62): #ladder7
        pos=81
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==86): #ladder8
        pos=97
        print("hurry! you climbed ladder and current block is :",pos)
    if(pos==71): #ladder9
        pos=90
        print("hurry! you climbed ladder and current block is :",pos)
        

      #snakes block
        
    if(pos==25): #snake1 tested (indirect allocating to next pos by subtracting from current pos)
        pos-=22
        print("sad news!snake ate you and your current block : ",pos)
    if(pos==56): #snake2 tested
        pos-=8
        print("sad news!snake ate you and your current block :",pos)
    if(pos==59): #snake3 tested
        pos-=58
        print("sad news!snake ate you and your current block :",pos)
    if(pos==69): #snake4 tested
        pos-=37
        print("sad news!snake ate you and your current block :",pos)
    if(pos==83): #snake5 tested 
        pos=57
        print("sad news!snake ate you and your current block :",pos)
    if(pos==91): #snake6 tested
        pos=73
        print("sad news!snake ate you and your current block :",pos)
    if(pos==94): #snake7 tested
        pos-=68
        print("sad news!snake ate you and your current block :",pos)
    if(pos==99): #snake8 tested
        pos=80
        print("sad news!snake ate you and your current block :",pos)

    if(pos==100):
        print("number of counts:",count)
    
   
      
