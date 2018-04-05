#Functions used by game
#=======================================================================================================================
import classes
import items
import random
import time
import pathlib
import _pickle as pickle
#=======================================================================================================================
#StartGame==============================================================================================================
def startGame():
    while True:
        startGameInput = input('Begin your quest, adventurer? (y/n)')
        if startGameInput == 'y':
            print("_________                   _        _______ \n"
                  "\__   __/|\     /||\     /|( \      (  ____ \ \n"
                  "   ) (   | )   ( || )   ( || (      | (    \/ \n"
                  "   | |   | (___) || |   | || |      | (__ \n"
                  "   | |   |  ___  || |   | || |      |  __) \n"
                  "   | |   | (   ) || |   | || |      | ( \n"
                  "   | |   | )   ( || (___) || (____/\| (____/\ \n"
                  "   )_(   |/     \|(_______)(_______/(_______/ \n")
            break
        elif startGameInput == 'n':
            print('Another day perhaps you will decide you are ready')
        else:
            print('You became confused, gather your thoughts')  #catches player input errors and offers another try
#=======================================================================================================================
#PlayerCreate===========================================================================================================
def playerCreate():
    while True:
        global player
        global playerOwnedWeapons
        global playerOwnedApperal
        global playerOwnedAccessories
        global playerOwnedItems
        global playerEquippedWeapons
        global playerEquippedArmour
        global playerEquippedAccessories
        global playerEquippedItems

        print('Creating character...')
        print()
        nameInput = input('Character name ->')
        subclassInput = input('Class type (knight/thief/mage) ->')
        print()


        if subclassInput == 'knight':  #assigns the player's starting equipment/stats based on class selection
            player = classes.pc(name=nameInput,
                                subclass='knight',
                                level=1,
                                HP=150,
                                AP=100,
                                Str=15,
                                Dex=5,
                                Int=2,
                                essential='n',
                                location=(0, 0))

            playerOwnedWeapons = classes.ownedWeapons(type = 'Weapons',
                                                      weapon1 = items.hw0001,
                                                      weapon2 = items.none,
                                                      weapon3 = items.none)

            playerOwnedApperal = classes.ownedArmour(type = 'armour',
                                                     armour1 = items.ha0001,
                                                     armour2 = items.none,
                                                     armour3 = items.none)
            playerOwnedAccessories = classes.ownedAccessories(type = 'accessories',
                                                              acc1 = items.ac0001,
                                                              acc2 = items.none,
                                                              acc3 = items.none)
            playerOwnedItems = classes.ownedItems(type = 'itemsd',
                                                  item1 = items.it0001,
                                                  item2 = items.none,
                                                  item3 = items.none)
            playerEquippedWeapons = classes.equippedWeapons(type = 'Weapons',
                                                            primary = items.hw0001)
            playerEquippedArmour = classes.equippedArmour(type = 'armour',
                                                          armour = items.ha0001)
            playerEquippedAccessories = classes.equippedAccessories(type = 'accessories',
                                                                    acc1 = items.ac0001,
                                                                    acc2 = items.none,
                                                                    acc3 = items.none,
                                                                    acc4 = items.none)
            playerEquippedItems = classes.beltItems(type = 'items',
                                                    pouch1 = items.it0001,
                                                    pouch2 = items.none,
                                                    pouch3=items.none,
                                                    pouch4=items.none,
                                                    pouch5=items.none,
                                                    pouch6=items.none)
            break
        elif subclassInput == 'thief':  #assigns the player's starting equipment/stats based on class selection
            player = classes.pc(name=nameInput,
                                subclass='thief',
                                level=1,
                                HP=100,
                                AP=150,
                                Str=5,
                                Dex=15,
                                Int=4,
                                essential='n',
                                location=(0, 0))

            playerOwnedWeapons = classes.ownedWeapons(type = 'Weapons',
                                                      weapon1 = items.lw0001,
                                                      weapon2 = items.none,
                                                      weapon3 = items.none)
            playerOwnedApperal = classes.ownedArmour(type = 'armour',
                                                     armour1 = items.la0001,
                                                     armour2 = items.none,
                                                     armour3 = items.none)
            playerOwnedAccessories = classes.ownedAccessories(type = 'accessories',
                                                              acc1 = items.ac0002,
                                                              acc2 = items.none,
                                                              acc3 = items.none)
            playerOwnedItems = classes.ownedItems(type = 'itemsd',
                                                  item1 = items.it0002,
                                                  item2 = items.none,
                                                  item3 = items.none)
            playerEquippedWeapons = classes.equippedWeapons(type = 'Weapons',
                                                            primary = items.lw0001)
            playerEquippedArmour = classes.equippedArmour(type = 'armour',
                                                          armour = items.la0001)
            playerEquippedAccessories = classes.equippedAccessories(type = 'accessories',
                                                                    acc1 = items.ac0002,
                                                                    acc2 = items.none,
                                                                    acc3 = items.none,
                                                                    acc4 = items.none)
            playerEquippedItems = classes.beltItems(type = 'items',
                                                    pouch1 = items.it0002,
                                                    pouch2 = items.none,
                                                    pouch3=items.none,
                                                    pouch4=items.none,
                                                    pouch5=items.none,
                                                    pouch6=items.none,)
            break
        elif subclassInput == 'mage':  #assigns the player's starting equipment/stats based on class selection
            player = classes.pc(name=nameInput,
                                subclass='mage',
                                level=1,
                                HP=100,
                                AP=100,
                                Str=5,
                                Dex=5,
                                Int=15,
                                essential='n',
                                location=(0, 0))
            playerOwnedWeapons = classes.ownedWeapons(type = 'Weapons',
                                                      weapon1 = items.mw0001,
                                                      weapon2 = items.none,
                                                      weapon3 = items.none)
            playerOwnedApperal = classes.ownedArmour(type = 'armour',
                                                     armour1 = items.cl0001,
                                                     armour2 = items.none,
                                                     armour3 = items.none)
            playerOwnedAccessories = classes.ownedAccessories(type = 'accessories',
                                                              acc1 = items.ac0003,
                                                              acc2 = items.none,
                                                              acc3 = items.none)
            playerOwnedItems = classes.ownedItems(type = 'itemsd',
                                                  item1 = items.it0002,
                                                  item2 = items.none,
                                                  item3 = items.none)
            playerEquippedWeapons = classes.equippedWeapons(type = 'Weapons',
                                                            primary = items.mw0001)

            playerEquippedArmour = classes.equippedArmour(type = 'armour',
                                                          armour = items.cl0001)
            playerEquippedAccessories = classes.equippedAccessories(type = 'accessories',
                                                                    acc1 = items.ac0003,
                                                                    acc2 = items.none,
                                                                    acc3 = items.none,
                                                                    acc4 = items.none)
            playerEquippedItems = classes.beltItems(type = 'items',
                                                    pouch1 = items.it0002,
                                                    pouch2 = items.none,
                                                    pouch3=items.none,
                                                    pouch4=items.none,
                                                    pouch5=items.none,
                                                    pouch6=items.none,)
            break
        else:
            print('You became confused, gather your thoughts')  #catches player input errors and offers another try
#=======================================================================================================================
#Combat=================================================================================================================
def CombatSim():
    PlayerHP = player.HP
    PlayerAP = player.AP
    EnemyHP = items.npc0001.HP
    EnemyAP = items.npc0001.AP

    CurrentCombat = classes.combat(playerHP = PlayerHP,
                                   playerAP = PlayerAP,
                                   enemyHP = EnemyHP,
                                   enemyAP = EnemyAP,)
#===========================================================================================
    #defines the player turn
    def PlayerTurn():
        while True:
            global PlayerSelectedMove
            ActionSelect = input("Engage or use item? >>")
            if ActionSelect == 'item':

                while True:
                    ItemSelect = input('please select an item: '
                                                      + " " + playerEquippedItems.pouch1.name
                                                      + " " + playerEquippedItems.pouch2.name
                                                      + " " + playerEquippedItems.pouch3.name
                                                      + " " + playerEquippedItems.pouch4.name
                                                      + " " + playerEquippedItems.pouch5.name
                                                      + " " + playerEquippedItems.pouch3.name
                                                      + " (1, 2, 3, 4, 5, or 6)")

                    # assigns an item to a variable based on player input
                    if ItemSelect == '1':
                        PlayerSelectedItem = playerEquippedItems.pouch1
                        break
                    elif ItemSelect == '2':
                        PlayerSelectedItem = playerEquippedItems.pouch2
                        break
                    elif ItemSelect == '3':
                        PlayerSelectedItem = playerEquippedItems.pouch3
                        break
                    elif ItemSelect == '4':
                        PlayerSelectedItem = playerEquippedItems.pouch4
                        break
                    elif ItemSelect == '5':
                        PlayerSelectedItem = playerEquippedItems.pouch5
                        break
                    elif ItemSelect == '6':
                        PlayerSelectedItem = playerEquippedItems.pouch6
                        break
                    else:
                        print("You became confused, gather your thoughts.")  #catches player input errors and offers another try
                        print("")

                # Framework for the effect of items on player and enemy HP and AP stats
                CurrentCombat.enemyHP = CurrentCombat.enemyHP
                CurrentCombat.enemyAP = CurrentCombat.enemyAP
                CurrentCombat.playerHP = CurrentCombat.playerHP + PlayerSelectedItem.effect.PlayerHPRegen
                CurrentCombat.playerAP = CurrentCombat.playerAP + PlayerSelectedItem.effect.PlayerAPRegen

                print("")
                print("You used", PlayerSelectedItem.name + "!")
                print("")
                print("Your HP is now", CurrentCombat.playerHP)
                print("Your AP is now", CurrentCombat.playerAP)
                break

            elif ActionSelect == 'engage':

                while True:
                    PlayerTurn.MoveSelect = input('please select a move: '
                                                  + " " + playerEquippedWeapons.primary.move1.name
                                                  + " " + playerEquippedWeapons.primary.move2.name
                                                  + " " + playerEquippedWeapons.primary.move3.name
                                                  + " (1, 2, or 3)>>")

                    # assigns an weapon's move to a variable based on player input
                    if PlayerTurn.MoveSelect == '1':
                        PlayerSelectedMove = playerEquippedWeapons.primary.move1
                        break
                    elif PlayerTurn.MoveSelect == '2':
                        PlayerSelectedMove = playerEquippedWeapons.primary.move2
                        break
                    elif PlayerTurn.MoveSelect == '3':
                        PlayerSelectedMove = playerEquippedWeapons.primary.move3
                        break
                    else:
                        print("You became confused, gather your thoughts.")  #catches player input errors and offers another try
                        print("")

            else:
                print("You became confused, gather your thoughts.")  #catches player input errors and offers another try
                print("")
                continue

            # Framework for the effect of a weapons move on player and enemy HP and AP stats
            CurrentCombat.enemyHP = CurrentCombat.enemyHP + PlayerSelectedMove.OpponentHPDamage
            CurrentCombat.enemyAP = CurrentCombat.enemyAP + PlayerSelectedMove.OpponentAPDamage
            CurrentCombat.playerHP = CurrentCombat.playerHP + PlayerSelectedMove.UserHPDamage
            CurrentCombat.playerAP = CurrentCombat.playerAP + PlayerSelectedMove.UserAPDamage
            print("You used", PlayerSelectedMove.name)
            time.sleep(.5)
            if CurrentCombat.enemyHP >= 0:
                print("The", EnemySelect.name + "'s health falls to", str(CurrentCombat.enemyHP) + "!")
                print("")
            elif CurrentCombat.enemyHP < 0:
                print("The", EnemySelect.name + "'s health falls below 0!")
                print("")
            break
#================================================================================================
    #defines enemy turn (which is essentially the same, with choices being determined randomly)
    def EnemyTurn():
        while True:
            global EnemySelectedMove

            EnemyTurn.MoveSelect = random.choice([EnemySelect.move1, EnemySelect.move2, EnemySelect.move3])

            if EnemyTurn.MoveSelect == EnemySelect.move1:
                EnemySelectedMove = EnemySelect.move1

            elif EnemyTurn.MoveSelect == EnemySelect.move2:
                EnemySelectedMove = EnemySelect.move2

            else:
                EnemySelectedMove = EnemySelect.move3

            break
        else:
            print("You became confused, gather your thoughts.")
            print("")

        CurrentCombat.enemyHP = CurrentCombat.enemyHP + EnemySelectedMove.UserHPDamage
        CurrentCombat.enemyAP = CurrentCombat.enemyAP + EnemySelectedMove.UserAPDamage
        CurrentCombat.playerHP = CurrentCombat.playerHP + EnemySelectedMove.OpponentHPDamage
        CurrentCombat.playerAP = CurrentCombat.playerAP + EnemySelectedMove.OpponentHPDamage

        print("Enemy used", EnemySelectedMove.name)
        time.sleep(.5)
        if CurrentCombat.playerHP >= 0:
            print("Your health falls to", str(CurrentCombat.playerHP) + "!")
            print("")
        elif CurrentCombat.playerHP < 0:
            print("Your health falls below 0!")
            print("")
#---------------------------------------------------------------------------------------
    #framework that utilizes and calls the actor turns to create the combat sim
    global PlayerInitiateCombatInput
    global EnemySelect
    EnemySelect = items.npc0001
    print("A ", EnemySelect.name, "appears!\n")
    PlayerInitiateCombatInput = input("Will you Fight or flee? >>")

    while True:
        #player may try to evade the combatant
        if PlayerInitiateCombatInput == 'flee':
            print('You attempt to flee')

            if player.Dex > 5:
                print("You successfully fled and progressed to the next room")
                break
            else:
                print("You are not fast enough, and the enemy blocks your path")
                PlayerInitiateCombatInput = 'fight'

        elif PlayerInitiateCombatInput == 'fight':
            playerAPReset = CurrentCombat.playerAP
            enemyAPReset = CurrentCombat.enemyAP
            while True:
                CurrentCombat.playerAP = playerAPReset
                CurrentCombat.enemyAP = enemyAPReset
                if CurrentCombat.playerHP <= 0:
                    print("You are dead.")
                    break
                elif CurrentCombat.playerAP <= 0 <= CurrentCombat.playerHP:
                    print("You do not have enough stamina to fight")
                elif CurrentCombat.enemyHP <= 0:
                    break
                else:
                    PlayerTurn()

                if CurrentCombat.enemyAP <= 0 <= CurrentCombat.playerHP:
                    print('The enemy is exhausted')
                    print("")
                    continue

                elif CurrentCombat.enemyHP <= 0:
                    print('The enemy is Dead...')
                    break

                else:
                    EnemyTurn()
        else:
            print("You became confused, gather your thoughts")

        time.sleep(.5)
        print("Battle over")
        break


#=======================================================================================================================
#Journal================================================================================================================
def ValidateJournal():
    while True:
        Journal = pathlib.Path("JournalFile.txt")
        if Journal.exists():  #Validates that JournalFile.txt exists
            break

        else:
            print("Setting up Journal...")
            Journal = open("JournalFile.txt", "w")  #Create Journal
            Journal.write("QUESTS:\nNOTES:\nSETTINGS:\n")  #Create Categories in journal
            Journal.close()
            time.sleep(1)
            print("Journal is set up.")
#=============================================================================================
def ReadJournal():
    while True:
        print("Please select journal section...")
        JournalSelection = int(input("Quests, Notes, Settings (1, 2, 3)~ "))
        print("")

        JournalFile = open("JournalFile.txt", "r")
        JournalSections = ["QUESTS:\n", "NOTES:\n", "SETTINGS:\n"]  #List that contains category titles
        JournalFileLines = JournalFile.readlines()  #Creates a list that has each line in file as an item
        DiscoveredLineStart = JournalFileLines.index(JournalSections[JournalSelection - 1])  #Finds the index of title of catagory requested
        DiscoveredLineEnd = JournalFileLines.index(JournalSections[JournalSelection])  #Finds the index of the next title

        #Print Contents of section selected
        Next = DiscoveredLineStart
        while Next < DiscoveredLineEnd:  #A loop that runs until the index of the next catagory
            LineToDisplay = Next
            print(JournalFileLines[LineToDisplay].strip())  #Prints lines of Requested category
            Next = LineToDisplay + 1
        break

    JournalFile.close()


#================================================================================================
def WriteToJournal():
    JournalFile = open("JournalFile.txt", "r")
    JournalFileLines = JournalFile.readlines()  #Creates a list that has each line in file as an item
    print("Select Section to append:")
    JournalSelection = int(input("Quests, Notes, Settings (1, 2, 3)~ "))
    JournalFile.close()
    print("")

    JournalSections = ["QUESTS:\n", "NOTES:\n", "SETTINGS:\n"]  #List that contains category titles
    JournalSectionDiscover = JournalFileLines.index(JournalSections[JournalSelection - 1])   #Finds the index of title of catagory requested

    NewContentInput = input("Enter new line ~")
    JournalFileLines.insert(JournalSectionDiscover + 1, "-" + NewContentInput+"\n")  #Inserts new item into list of lines, creating a new line
    JournalUpdatedContent = "".join([str(i) for i in JournalFileLines])  #Turns lines list back into a string so  that it can be written to file

    JournalFile = open("JournalFile.txt", "w")
    JournalFile.write(JournalUpdatedContent)  #Overwrites old file with updated file containing new addition

    JournalFile.close()

#=======================================================================================================================
#Save==============================================================================================================
def Save():
    print("Saving...")
    SaveFile = open('Save', 'wb')
    SaveCatagoryList = [player, playerOwnedWeapons, playerOwnedApperal, playerOwnedAccessories, playerOwnedItems,
                             playerEquippedWeapons, playerEquippedArmour, playerEquippedAccessories, playerEquippedItems]


    SaveListCountStart = 0
    while SaveListCountStart < 9:
        SaveListCount = SaveListCountStart
        pickle.dump(SaveCatagoryList[SaveListCount], SaveFile)
        print('Saving ', str(SaveCatagoryList[SaveListCount]) + "...")
        SaveListCountStart = SaveListCount + 1
        time.sleep(0.5)


#==================================================================================================
def RecoverSave():
    global player
    global playerOwnedWeapons
    global playerOwnedApperal
    global playerOwnedAccessories
    global playerOwnedItems
    global playerEquippedWeapons
    global playerEquippedArmour
    global playerEquippedAccessories
    global playerEquippedItems

    print("Recovering save file... ")

    SaveFile = open('Save', 'rb')
    while True:
        try:
            player = pickle.load(SaveFile)
            playerOwnedWeapons = pickle.load(SaveFile)
            playerOwnedApperal = pickle.load(SaveFile)
            playerOwnedAccessories = pickle.load(SaveFile)
            playerOwnedItems = pickle.load(SaveFile)
            playerEquippedWeapons = pickle.load(SaveFile)
            playerEquippedArmour = pickle.load(SaveFile)
            playerEquippedAccessories = pickle.load(SaveFile)
            playerEquippedItems = pickle.load(SaveFile)

        except EOFError:
            break
    time.sleep(1)
    print("Okay.")



#=======================================================================================================================
class Board(list):



    def __str__(self):

        return "\n".join(" ".join(row) for row in self)





class Game(object):



    MARKER_X = "X"

    MARKER_O = "O"

    CTRLS = [

        "left",

        None,

        "right",

        "up",

        None,

        "down",

    ]

    EXIT = "stop"

    START = [0, 0]

    DEFAULT = [["O"] * 6 for _ in range(6)]



    def __init__(self):

        self.flag = True

        self.arena = Board(Game.DEFAULT)

        self.curr_pos = Game.START[:]

        self.prev_pos = Game.START[:]

        self.move_player()



    def move_player(self):

        px, py = self.prev_pos

        cx, cy = self.curr_pos

        if (0 <= cx <= 3) and (0 <= cy <= 5):

            self.arena[py][px] = Game.MARKER_O

            self.arena[cy][cx] = Game.MARKER_X



        else:

            print("Please enter a proper direction.")

            self.curr_pos = self.prev_pos[:]

            self.move_player()

    def play(self):



        print("You are at 0,0")

        while self.flag:

            ctrl = input("Move left, right, up, down, or stop?").lower()

            if ctrl in Game.CTRLS:

                d = Game.CTRLS.index(ctrl)

                self.prev_pos = self.curr_pos[:]

                self.curr_pos[d > 2] += d - (1 if d < 3 else 4)

                self.move_player()

                print(self.curr_pos)

                if self.curr_pos == [1, 0]:

                  while self.flag:

                    print("You walk face first into a wall, and turn back to the center of the room")

                    self.curr_pos = self.prev_pos[:]

                    self.move_player()

                    print(self.curr_pos)

                    break

                #elif self.curr_pos == [0,1]:

                  #while self.flag:

                    #CombatSim()

                    #self.curr_pos = self.prev_pos[:]

                    #self.move_player()

                    #print(self.curr_pos)

                    #break

                elif self.curr_pos == [1, 1]:

                    while self.flag:

                        print("You walk face first into a wall, and turn back to the center of the room")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

                elif self.curr_pos == [0, 2]:

                    while self.flag:

                        print("as you walk into the room, you note a large door on one end, a pit on the other and"

                              "a staircase in front of you")

                        break

                elif self.curr_pos == [2, 2]:

                    while self.flag:

                        print("Congratulations! You made it out of the dungeon!,"

                              "Get Ready for the full product, THULE, coming soon!")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        self.flag = False



                        break

                elif self.curr_pos == [3, 1]:

                    while self.flag:

                        print("You walk face first into a wall, and turn back to the center of the room")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

                elif self.curr_pos == [3, 2]:

                    while self.flag:

                        print("You almost slip and fall into a chasm,"

                              "You catch yourself and return to the center of the room")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

                elif self.curr_pos == [1, 5]:

                    while self.flag:

                        print("Wishing to be one with the waterfall,"

                              "you almost walk off the edge of the platform,"

                              "you regain your senses and return to the center of the room")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

                elif self.curr_pos == [0, 5]:

                    while self.flag:

                        print("Amazed by the gorgeous waterfall,"

                              "you almost walk off the platform you were standing on,"

                              "you catch yourself and return to the center of the room ")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

            elif ctrl == Game.EXIT:

                self.flag = False

            else:

                print("Please enter a proper direction.")



my_game = Game()










