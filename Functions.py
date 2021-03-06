#Functions used by game
#=======================================================================================================================
import classes
import items
import random
import time
import pathlib
from threading import Timer
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
                                                    pouch3=items.noneItems,
                                                    pouch4=items.noneItems,
                                                    pouch5=items.noneItems,
                                                    pouch6=items.noneItems,)
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
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch1.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch1.effect.PlayerAPRegen

                        playerEquippedItems.pouch1.count = playerEquippedItems.pouch1.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch1.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch1.count == 0:
                            playerEquippedItems.pouch1 = items.noneItems

                        break
                    elif ItemSelect == '2':
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch2.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch2.effect.PlayerAPRegen

                        playerEquippedItems.pouch2.count = playerEquippedItems.pouch2.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch1.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch2.count == 0:
                            playerEquippedItems.pouch2 = items.noneItems

                        break
                    elif ItemSelect == '3':
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch3.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch3.effect.PlayerAPRegen

                        playerEquippedItems.pouch3.count = playerEquippedItems.pouch3.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch1.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch3.count == 0:
                            playerEquippedItems.pouch3 = items.noneItems

                        break
                    elif ItemSelect == '4':
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch4.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch4.effect.PlayerAPRegen

                        playerEquippedItems.pouch4.count = playerEquippedItems.pouch4.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch4.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch4.count == 0:
                            playerEquippedItems.pouch4 = items.noneItems

                        break
                    elif ItemSelect == '5':
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch5.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch5.effect.PlayerAPRegen

                        playerEquippedItems.pouch5.count = playerEquippedItems.pouch5.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch5.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch5.count == 0:
                            playerEquippedItems.pouch5 = items.noneItems

                        break
                    elif ItemSelect == '6':
                        # Framework for the effect of items on player and enemy HP and AP stats
                        CurrentCombat.enemyHP = CurrentCombat.enemyHP
                        CurrentCombat.enemyAP = CurrentCombat.enemyAP
                        CurrentCombat.playerHP = CurrentCombat.playerHP + playerEquippedItems.pouch6.effect.PlayerHPRegen
                        CurrentCombat.playerAP = CurrentCombat.playerAP + playerEquippedItems.pouch6.effect.PlayerAPRegen

                        playerEquippedItems.pouch6.count = playerEquippedItems.pouch6.count - 1

                        print("")
                        print("You used", playerEquippedItems.pouch6.name + "!")
                        print("")
                        print("Your HP is now", CurrentCombat.playerHP)
                        print("Your AP is now", CurrentCombat.playerAP)

                        if playerEquippedItems.pouch6.count == 0:
                            playerEquippedItems.pouch6 = items.noneItems

                        break
                    else:
                        print("You became confused, gather your thoughts.")  #catches player input errors and offers another try
                        print("")


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


    while True:
        PlayerInitiateCombatInput = input("Will you Fight or flee? >>")
        #player may try to evade the combatant
        if PlayerInitiateCombatInput == 'flee':
            print('You attempt to flee')

            if player.Dex > 5:
                print("You successfully fled and progressed to the next room")
                break
            else:
                print("You are not fast enough, and the enemy blocks your path")
                PlayerInitiateCombatInput = 'fight'
                continue

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
            continue

        time.sleep(.5)
        print("Battle over")
        player.HP = CurrentCombat.playerHP
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
def Puzzle():

    print('1: Precisely one of these statements is untrue\n',

          '2: Precisely two of these statements are untrue\n',

          '3: Precisely three of these statements are untrue\n',

          '4: Precisely four of these statements are untrue\n',

          '5: Precisely five of these statements are untrue\n',

          '6: Precisely six of these statements are untrue\n',

          '7: Precisely seven of these statements are untrue\n',

          '8: Precisely eight of these statements are untrue\n',

          '9: Precisely nine of these statements are untrue\n',

          '10: Precisely ten of these statements are untrue.\n')

    #=================================================================================

    #=================================================================================

    while True:

        timeout = 20

        t = Timer(timeout, print, ['Times up. Try again'])

        t.start()

        rdl_dung = input('Which statement is true?, Answer with the number associated to statement. You have 20 seconds.\n')



        if rdl_dung == '9':

            print('The answer is statement 9, you have answered correctly.')

            break

        elif rdl_dung != '9':

            print('You have answered incorrectly.Try again')

        else:

            t.cancel()

            break
#=======================================================================================================================
#Save==============================================================================================================
def Save():
    print("Saving...")
    SaveFile = open('Save', 'wb')  #opens the save file in 'write' mode
    SaveCatagoryList = [player, playerOwnedWeapons, playerOwnedApperal, playerOwnedAccessories,
                        playerEquippedWeapons, playerEquippedArmour, playerEquippedAccessories, playerEquippedItems]


    SaveListCountStart = 0
    while SaveListCountStart < 8:  #a loop that saves a catagory the returns to beginning, and ending when all categories are saved
        SaveListCount = SaveListCountStart
        pickle.dump(SaveCatagoryList[SaveListCount], SaveFile)  #the categories are saved in a specific order
        print('Saving ', str(SaveCatagoryList[SaveListCount]) + "...")
        SaveListCountStart = SaveListCount + 1
        time.sleep(0.5)


#==================================================================================================
def RecoverSave():  #recovers the data saved on the save file
    global player
    global playerOwnedWeapons
    global playerOwnedApperal
    global playerOwnedAccessories
    global playerEquippedWeapons
    global playerEquippedArmour
    global playerEquippedAccessories
    global playerEquippedItems

    print("Recovering save file... ")

    SaveFile = open('Save', 'rb')

    #reads and assigns the data off of the save file in the correct order
    while True:
        try:
            player = pickle.load(SaveFile)
            playerOwnedWeapons = pickle.load(SaveFile)
            playerOwnedApperal = pickle.load(SaveFile)
            playerOwnedAccessories = pickle.load(SaveFile)
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

        "west",

        None,

        "east",

        "north",

        None,

        "south",

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

        if (0 <= cx < 3) and (0 <= cy <= 5):

            self.arena[py][px] = Game.MARKER_O

            self.arena[cy][cx] = Game.MARKER_X



        else:

            print("Please enter a proper direction.")

            self.curr_pos = self.prev_pos[:]

            self.move_player()

    def play(self):



        print("You are at 0,0")

        while self.flag:

            ctrl = input("Move west, east, north, south, or stop?").lower()

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

                elif self.curr_pos == [0, 1]:

                    while self.flag:

                        CombatSim()


                        print(self.curr_pos)

                        break

                elif self.curr_pos == [1, 1]:

                    while self.flag:

                        print("You walk face first into a wall, and turn back to the center of the room")

                        self.curr_pos = self.prev_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break
                elif self.curr_pos == [1, 2]:

                    while self.flag:

                        if (playerEquippedItems.pouch1 == items.it0003) or (playerEquippedItems.pouch2 == items.it0003) or (playerEquippedItems.pouch3 == items.it0003):
                            print("You use the key you found to open the door")
                            self.curr_pos = self.curr_pos
                        else:
                            print("The door is locked")
                            self.curr_pos = self.prev_pos[:]
                            print(self.curr_pos)

                            break

                        print("You see a room full of treasure")

                        d = Game.CTRLS.index(ctrl)

                        self.prev_pos = self.curr_pos[:]

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

                elif self.curr_pos == [1, 4]:

                    while self.flag:

                        CombatSim()

                        self.curr_pos = self.curr_pos[:]

                        self.move_player()

                        print(self.curr_pos)

                        break

                elif self.curr_pos == [2,4]:
                    while self.flag:
                        print("as you step into the room, you notice the floor is covered in mystic healing scrawls,"
                              "you feel healthier")
                        player.HP = player.HP+50
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










