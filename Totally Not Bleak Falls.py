import classes
import items


# ==========================================================================
# ==============================================================================
def startGame():
    while True:
        startGameInput = input('Begin your quest, adventurer? (y/n)')
        if startGameInput == 'y':
            break
        elif startGameInput == 'n':
            print('Another day perhaps you will decide you are ready')
        else:
            print('You became confused, gather your thoughts')


# -------------------------------------------------------------------------------
def playerCreate():
    while True:
        global player
        global playerApparel
        global playerWeapon
        print('Creating character...')
        print()
        nameInput = input('Character name ->')
        subclassInput = input('Class type (knight/thief/mage) ->')
        print()
        if subclassInput == 'knight':
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
            player.encodeStats()

            playerOwnedWeapons = classes.ownedWeapons(weapon1 = items.hw0001)
            playerOwnedApperal = classes.ownedArmour(armour = items.ha0001)
            playerOwnedAccessories = classes
            playerOwnedItemsd
            break
        elif subclassInput == 'thief':
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

            playerApparel = items.la0001
            playerWeapon = items.lw0001

            break
        elif subclassInput == 'mage':
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

            playerApparel = items.cl0001
            playerWeapon = items.mw0001

            break
        else:
            print('You became confused, gather your thoughts')


# -----------------------------------------------------------------------------------
startGame()
playerCreate()
