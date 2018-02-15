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
        global weapons
        global armour
        global itemsd

        print('Creating character...')
        print()
        nameInput = input('Character name ->')
        subclassInput = input('Class type (knight/thief/mage) ->')
        print()

        weapons = "these are your weapons"
        armour = "this is your armour"
        accessories = "these are your accessories"
        itemsd = "these are your items"

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

            playerOwnedWeapons = classes.ownedWeapons(type = weapons,
                                                      weapon1 = items.hw0001,
                                                      weapon2 = 'none',
                                                      weapon3 = 'none')
            playerOwnedApperal = classes.ownedArmour(type = armour,
                                                     armour1 = items.ha0001,
                                                     armour2 = 'none',
                                                     armour3 = 'none')
            playerOwnedAccessories = classes.ownedAccessories(type = accessories,
                                                              acc1 = items.ac0001,
                                                              acc2 = 'none',
                                                              acc3 = 'none')
            playerOwnedItems = classes.ownedItems(type = itemsd,
                                                  item1 = items.it0001,
                                                  item2 = 'none',
                                                  item3 = 'none')
            playerEquippedWeapons = classes.equippedWeapons(type = weapons,
                                                            primary  = items.hw0001)
            playerEquippedArmour = classes.equippedArmour()

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
            player.encodeStats()

            playerOwnedWeapons = classes.ownedWeapons(type = weapons,
                                                      weapon1 = items.lw0001,
                                                      weapon2 = 'none',
                                                      weapon3 = 'none')
            playerOwnedApperal = classes.ownedArmour(type = armour,
                                                     armour1 = items.la0001,
                                                     armour2 = 'none',
                                                     armour3 = 'none')
            playerOwnedAccessories = classes.ownedAccessories(type = accessories,
                                                              acc1 = items.ac0002,
                                                              acc2 = 'none',
                                                              acc3 = 'none')
            playerOwnedItems = classes.ownedItems(type = itemsd,
                                                  item1 = items.it0002,
                                                  item2 = 'none',
                                                  item3 = 'none')

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
            player.encodeStats()
            playerOwnedWeapons = classes.ownedWeapons(type = weapons,
                                                      weapon1 = items.mw0001,
                                                      weapon2 = 'none',
                                                      weapon3 = 'none')
            playerOwnedApperal = classes.ownedArmour(type = armour,
                                                     armour1 = items.cl0001,
                                                     armour2 = 'none',
                                                     armour3 = 'none')
            playerOwnedAccessories = classes.ownedAccessories(type = accessories,
                                                              acc1 = items.ac0003,
                                                              acc2 = 'none',
                                                              acc3 = 'none')
            playerOwnedItems = classes.ownedItems(type = itemsd,
                                                  item1 = items.it0002,
                                                  item2 = 'none',
                                                  item3 = 'none')
            break
        else:
            print('You became confused, gather your thoughts')


# -----------------------------------------------------------------------------------
startGame()
playerCreate()
