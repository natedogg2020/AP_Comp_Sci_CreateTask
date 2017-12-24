import sys
import os
import time
from random import randint
superSayan = {'weapon: ': 150, 'health: ' : 600}
dragon = {'weapon: ': 200, 'health: ' : 300}
haybale = {'moves: ': 0}
stranger = {'talked: ': 0}
player = {'weapon: ': 10, 'health: ': 100, 'money: ': 0, }
honeyBadger = {'weapon: ': 50, 'health: ' : 30}
ghost = {'weapon: ': 70, 'health: ' : 150}
robber = {'weapon: ': 150, 'health: ' : 300}
def End_Menu():
            p = raw_input('Would you like to play again? Yes(Y) or No(N)?')
            if p == 'Y' or p=='y' or p=='Yes' or p=='yes':
                    superSayan['weapon: '] = 150 
                    superSayan['health: ']=600
                    dragon ['weapon: ']=200 
                    dragon['health: ']=300
                    haybale['moves: ']= 0
                    stranger['talked: ']=0
                    player['weapon: ']= 10 
                    player['health: ']= 100
                    player['money: ']= 0
                    honeyBadger['weapon: ']=50 
                    honeyBadger['health: ']=30
                    ghost['weapon: ']= 70 
                    ghost['health: ']=150
                    robber['weapon: ']=150 
                    robber['health: ']=300
                    print(superSayan,'\n', dragon, '\n', haybale,'\n', stranger, '\n',  player,'\n', honeyBadger,'\n', ghost, '\n',robber)
                    Main_Menu()
            else:
                sys.exit() 
def Stranger():
    if stranger['talked: '] ==0:
            t=raw_input("Hello fellow traveler, I have one simple question, and you will be rewarded.\nDo you prefer paper(1) or plastic(2)?")
            if t=='1':
                player['money: '] += 100
                print("Congratulations, you chose correctly! Paper is recyclable.\nYou recieved 100 coins")
            
                stranger['talked: '] +=1
                Town_Square()
            elif t=='2':
                player['money: '] += 50
                print("Wrong answer, but I like your efforts.\nHere is 50 coins anyways.")
                stranger['talked: '] +=1
                Town_Square()
                    
    else:  
        print("You've already talked to the stranger")
        Town_Square()
def See_Merchant():
    print(player)
    t=raw_input("Good Day, Traveler! Welcome to my store,\nYou can buy A Snack(1)-20 health:10 coins  A Cup of Fruit(2)-50 health:25 coins  A Gallon of Milk(3)-75 health:40 coins  go back(4)\n")
    
    if t=='1':
        if player['money: '] <10:
            print("You don't have enough money for this item")
            See_Merchant()
        else:
            print("You have consumed A Snack! +20 Health")
            player['money: '] += -10
            player['health: '] += 20
            See_Merchant()     
    elif t=='2':
        if player['money: '] <50:
            print("You don't have enough money for this item")
            See_Merchant()
        else:
            print("You have consumed A Cup of Fruit! +50 Health")
            player['money: '] += -25
            player['health: '] += 50
            See_Merchant()
    elif t=='3':
        if player['money: '] <40:
            print("You don't have enough money for this item")
            See_Merchant()
        else:
            print("You have consumed A Gallon of Milk! +75 Health")
            player['money: '] += -40
            player['health: '] += 75
            See_Merchant()
    elif t=='4':
            Town_Square()
def Visit_Weaponsmith():
    print(player)
    t=raw_input("Salutations, Traveler! I am the weaponsmith,\nYou can buy A Dangerous Sword(1)150 attack:150 coins  A Scary Yo-yo(2)200 attack:200 coins  A Gallon of Napalm(3)250 attack:250 coins  go back(4)\n")
    
    if t=='1':
        if player['weapon: '] >= 150:
            print("Your weapon is already better, no need to downgrade...")
            Visit_Weaponsmith()
        else:
            if player['money: '] <100:
                print("You don't have enough money for this item")
                Visit_Weaponsmith()
            else:
                print("You have acquired A Dangerous Sword!")
                player['money: '] += -100
                player['weapon: '] = 150
                Visit_Weaponsmith()     
    elif t=='2':
        if player['weapon: '] >= 200:
            print("Your weapon is already better, no need to downgrade...")
            Visit_Weaponsmith()
        else:
            if player['money: '] <200:
                print("You don't have enough money for this item")
                Visit_Weaponsmith()
            else:
                print("You have acquired A Scary Yo-yo!")
                player['money: '] += -200
                player['weapon: '] = 200
                Visit_Weaponsmith()
    elif t=='3':
        if player['weapon: '] >= 250:
            print("Your weapon is already better, no need to downgrade...")
            Visit_Weaponsmith()
        else:
            if player['money: '] <250:
                print("You don't have enough money for this item")
                Visit_Weaponsmith()
            else:
                print("You have acquired A Gallon of Napalm!")
                player['money: '] += -250
                player['weapon: '] = 250
                Visit_Weaponsmith()
    elif t=='4':
            Town_Square()    
def Healer():
    print(player)
    t=raw_input("Good day, Traveler! I am the healer,\nYou can buy A Bandaid(1)+50 health:30 coins  Coughsyrup(2)+100 health:50 coins  A Health Potion(3)+200 health:80 coins  go back(4)\n")
    
    if t=='1':
        if player['money: '] <30:
            print("You don't have enough money for this item")
            Healer()
        else:
            print("You have put on A Bandaid! +50 Health")
            player['money: '] += -30
            player['health: '] += 50
            Healer()     
    elif t=='2':
        if player['money: '] <50:
            print("You don't have enough money for this item")
            Healer()
        else:
            print("You have consumed Coughsyrup! +100 Health")
            player['money: '] += -50
            player['health: '] += 100
            Healer()
    elif t=='3':
        if player['money: '] <100:
            print("You don't have enough money for this item")
            Healer()
        else:
            print("You have consumed A Health Potion! +250 Health")
            player['money: '] += -100
            player['health: '] += 250
            Healer()
    elif t=='4':
            Town_Square()             
def Town_Square():
    ts=raw_input("You have arrived at the picturesque townsquare of Engsdale!\nWhat would you like to do first? \nTalk to stranger(1)  See Merchant(2)  Visit WeaponSmith(3)  See Healer(4) Leave Townsquare(5)\n")               
    if ts=='1':
        Stranger()
    elif ts=='2':
        See_Merchant()
    elif ts=='3':
        Visit_Weaponsmith()
    elif ts=='4':
        Healer()
    elif ts=='5':
        print("AAAHHH LEAVING")
        Engsdale_District_Menu()
    elif ts == 'end' or ts == 'quit' or ts == 'q':
	       sys.exit() # This quits the game
def Dark_Alleyway():
    print(player)
    x=raw_input("You are very brave to go down such a dark alleyway!\nYOU SEE A DANGEROUS ROBBER(150 attack, 300 health), WHAT WILL YOU DO?\nRUN AWAY(1) FIGHT TO THE DEATH(2)\n")
    if x=='1':
        Engsdale_District_Menu()
    elif x=='2':
        player['health: '] += - robber['weapon: ']
        robber['health: '] += - player['weapon: ']
        print ("You're health is: ", player['health: '])
        print ("The robber's health is: ", robber['health: '], '\n\n\n')
        if player['health: '] <= 0:
            print('you died...')
            time.sleep(0)
            End_Menu()
        if robber['health: '] <= 0:
            print("You killed the robber! You're safe now.. \n\nand you found 500 gold!!!\n\n+500 gold\n\n\n")
            player['money: '] += 500
            time.sleep(0)
            Engsdale_District_Menu()
        else:
            print('You wounded the robber!')
            time.sleep(0)
            Dark_Alleyway()
        Engsdale_District_Menu()
    elif x == 'end' or x == 'quit' or x == 'q':
	       sys.exit() # This quits the game
    else:
        print("Incorrect input")
        Dark_Alleyway()
def Help_Woman():
    print(player)
    h=raw_input("Nice to meet you, traveler. Would you be willing to help me for some money? Yes(1) No(2)")
    x= randint(0,150)
    haybale = {'moves: ': 0}
    if h=='1':
        while haybale['moves: '] < 5:
            hm=raw_input("Great! I need you to move 5 haybales around my farm. Move haybale(1)  Give up(2)")
            if hm=='1':
                haybale['moves: '] += 1
                print(haybale)
            elif hm=='2':
                Help_Woman()
        print "Nice work! Here are "+str(x)+" coins! good luck on your travels!"
        player['money: '] += x
        Help_Woman()
    
        print(player)
    elif h=='2':
        Engsdale_District_Menu()
    elif h == 'end' or h == 'quit' or h == 'q':
	       sys.exit() # This quits the game
    else:
        print("that is not a command, please try again")
        Help_Woman()
def Brown_Woods():
    if dragon['health: '] <= 0:
        print('AMAZING! You are a true fighter. \nUse the code (1918) to get back to this point\nJust in case you need it...')
        print('You now feel a presence of a greater being!')
        time.sleep(2)
        print('A SUPERSAYAN SPRINTS TOWARDS YOU!!!\n\n\n')
        time.sleep(1)
        player['health: '] += - superSayan['weapon: ']
        superSayan['health: '] += - player['weapon: ']
        print ('youre health is: ', player['health: '])
        print ("the supersayan's health is: ", superSayan['health: '], "\n\n\n\n\n")
        if player['health: '] <= 0:
                print('you died...')
                time.sleep(1)
                End_Menu()
                sys.exit()
        if superSayan['health: '] <= 0:                             #GHOST
                print('you killed the supersayan! youre safe now. \n\n\n\n\ncongrats! you actually finished the game!')
                time.sleep(0)
                print(player)
                End_Menu()
        Brown_Woods()
    else:
        print('you see a dragon!!!\n\nOh no! its coming right for you!!!\n\nits begun to attack you\n\n')  #BEAR
        time.sleep(1)
        player['health: '] += - dragon['weapon: ']
        dragon['health: '] += - player['weapon: ']
        print ('youre health is: ', player['health: '])
        print ('the dragons health is: ', dragon['health: '], '\n\n\n')
        if player['health: '] <= 0:
                print('you died...')
                time.sleep(2)
                Engsdale_District_Menu()
        if dragon['health: '] <= 0:
                print('you killed the dragon! youre safe now.. \n\nand you found 5000 gold!!!\n\n+5000 gold\n\n\n')
                player['money: '] = 5000
                time.sleep(2)
                Engsdale_District_Menu()
        else:
                print('you wounded the dragon!')
                time.sleep(1)
                Engsdale_District_Menu()
def Engsdale_District_Menu():
    x=raw_input("Hello again, traveler! Now that you have made it through the woods,\nyou have arrived in Engsdale district! Where will you go first?\nTown Square(1)  Dark Alleyway(2)  Help Woman(3)  BrownWoods(4)\n")
    if x =='1':
        Town_Square()
    elif x =='2':
        Dark_Alleyway()
    elif x =='3':
        Help_Woman()
    elif x =='4':
        Brown_Woods()
    elif x == 'end' or x == 'quit' or x == 'q':
	       sys.exit() # This quits the game
    else:
        print("Incorrect input, traveler, please select a location(1-4)")
def Intermission():
    o=raw_input("HAHA! You thought you beat the game, didn't you! \nThere are more challenges ahead, BE PREPARED \nIf you're ready to go on, press any button to continue\n")
    if o == 'q':
        print("Let's do this!")
        Engsdale_District_Menu()
    elif o == 'end' or o == 'quit' or o == 'q':
	       sys.exit() # This quits the game
    else:
        print("Let's do this!")
        Engsdale_District_Menu()
            
def Town_Menu(): #TOWN MENU
            print(player)
            f =raw_input('what do you want to buy?\nbandage+100 health:30coins(1)    weapon-100attack:60 coins(2)    go back(3)\n')
            
            if f == 'bandage' or f=='1':
                if player['money: '] < 30:
                    print('you dont have enough money...')
                    Town_Menu()
                else:
                    print('bandage was bought!\n\n+100 health\n')
                    player['health: '] += 100
                    player['money: '] += -30
                    Town_Menu()
            elif f == 'weapon' or f=='2':
                if player['money: '] < 60:
                    print('you dont have enough money...')
                    Town_Menu()
                else:
                    print(' i have a new sniper you can buy! it will cost you 60 gold!')
                    player['weapon: '] = 100
                    player['money: '] += -60
                    print('you bought the sniper!\n\nweapon = 100\n')
                    Town_Menu()
            elif f == 'go back' or f=='3':
                Main_Menu()
            elif f == 'end' or f == 'quit' or f == 'q':
	       sys.exit() # This quits the game
            else:
                print('i dont know what you mean..')
                Town_Menu()
                
def Main_Menu(): #FIRST LEVEL
    x =raw_input('Hello traveler! Where do you wish to go?\nWhat will you do?\ninn(1)---50 coins     GreenWoods(2)     Old Barn(3)     Town(4)\nsee stats(5)    secret(password)\n')
    if x== '1918':
        player['health: '] += 100
        Engsdale_District_Menu()
    elif x == 'inn' or x== '1':                                   #INN
        if player['money: '] < 50:
            print('you dont have enough gold\n\n\n\n\n')
            Main_Menu()
        else:
            player['money: '] += -50
            player['health: '] += 50
            print('...\n...\n...')
            time.sleep(0)
            print('you feel well rested')
            print (' your health is: ', player['health: '], '\n\n\n')
            print(' you now have', player['money: '], 'gold\n\n')
            time.sleep(2)
            Main_Menu()
    elif x == "woods" or x == '2':                          #WOODS
        if honeyBadger['health: '] <= 0:
            print('you feel a presence...')
            time.sleep(1)
            print(' a ghost flies towards you!!!\n')
            time.sleep(1)
            player['health: '] += - ghost['weapon: ']
            ghost['health: '] += - player['weapon: ']
            print ('youre health is: ', player['health: '])
            print ('the ghosts health is: ', ghost['health: '], '\n\n\n\n\n')
            if player['health: '] <= 0:
                print('you died...')
                time.sleep(1)
                End_Menu()
                sys.exit()
            if ghost['health: '] <= 0:                             #GHOST
                print('you killed the ghost! youre safe now. \n\n\n\n\ncongrats! you finished the game!')
                time.sleep(0)
                Intermission()
            Main_Menu()
        else:
            print('you see a wild honeybadger!!!\n\noh no! its coming right for you!!!\n\nits begun to attack you\n')  #BEAR
            time.sleep(3)
            player['health: '] += - honeyBadger['weapon: ']
            honeyBadger['health: '] += - player['weapon: ']
            print ('youre health is: ', player['health: '])
            print ('the bears health is: ', honeyBadger['health: '], '\n\n\n')
            if player['health: '] <= 0:
                print('you died...')
                time.sleep(2)
                End_Menu()
            if honeyBadger['health: '] <= 0:
                print('you killed the honeybadger! youre safe now.. \n\nand you found 50 gold!!!\n\n+50 gold\n')
                player['money: '] = 50
                time.sleep(3)
                Main_Menu()
            else:
                print('you wounded the honeybadger!')
                time.sleep(3)
                Main_Menu()
    elif x == 'old barn' or x== '3':                                    #OLD BARN
        if player['weapon: '] >= 70:
            print('theres nothing here\n')
            Main_Menu()
        else:
            player['weapon: '] = 70
            print('you found an old shotgun!\n\nweapon = 70\n')
            Main_Menu()
    elif x == 'see stats' or x =='5':
        print(player)
        Main_Menu()
    
    elif x == 'town' or x=='4':                                         #TOWN
        print(' youre walking to the town when you find 10 gold!!')
        player['money: '] += 10
        time.sleep(3)
        print(' you come across a shop and you walk in...\n\n\nWelcome to my shop!\n')
        Town_Menu()
    elif x=='4141':
        player['money: '] += 1000
        Main_Menu()
    elif x == "end" or x == "quit" or x == "q":
	    sys.exit() # This quits the game
    elif player['health: '] <= 0:
                print('you died...')
                sys.exit()
    else:
        print('thats no place to go!\n')
        time.sleep(1)
        Main_Menu()
        
Main_Menu()