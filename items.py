import classes

# Moves======================================================================

mv0000 = classes.move(name="Nothing",     #Creates a function for a move to be called upon later, sets name

                      OpponentHPDamage=0,   #Sets damage done to opponent

                      OpponentAPDamage=0,   #Sets damage done to stamina to opponent

                      UserHPDamage=0,       #Sets damage done to user of the move

                      UserAPDamage=0)       #Sets stamina required and used when the move is called upon

mv0001 = classes.move(name="slash",

                      OpponentHPDamage=-10,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-5)

mv0002 = classes.move(name="stab",

                      OpponentHPDamage=-20,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-25)

mv0003 = classes.move(name="bash",

                      OpponentHPDamage=-5,

                      OpponentAPDamage=-20,

                      UserHPDamage=0,

                      UserAPDamage=-10)

mv0004 = classes.move(name="evade",

                      OpponentHPDamage=0,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-18)

mv0005 = classes.move(name="fireball",

                      OpponentHPDamage=-20,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-20)

mv0006 = classes.move(name="frostfall",

                      OpponentHPDamage=-5,

                      OpponentAPDamage=-20,

                      UserHPDamage=0,

                      UserAPDamage=-15)

mv0007 = classes.move(name="heal",

                      OpponentHPDamage=0,

                      OpponentAPDamage=0,

                      UserHPDamage=+30,

                      UserAPDamage=-20)

mv0008 = classes.move(name="Bite",

                      OpponentHPDamage=15,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-10)

mv0009 = classes.move(name="Claw",

                      OpponentHPDamage=10,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-15)

mv0010 = classes.move(name="Starved Strike",

                      OpponentHPDamage=25,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=15)

mv0011 = classes.move(name="Dagger Jab",

                      OpponentHPDamage=-10,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-10)

mv0012 = classes.move(name="Infectious Bite",

                      OpponentHPDamage=-10,

                      OpponentAPDamage=-10,

                      UserHPDamage=0,

                      UserAPDamage=-20)

mv0013 = classes.move(name="Arrow",

                      OpponentHPDamage=-15,

                      OpponentAPDamage=0,

                      UserHPDamage=0,

                      UserAPDamage=-5)

# Effects====================================================================
ef0001 = classes.effect(name='Heal',        #creates ID for effect to be called upon
                        PlayerHPRegen=+20,      #Sets health gain/loss when item is used
                        PlayerAPRegen=0)        #Sets stamina gain/loss when item is used

ef0002 = classes.effect(name='ManaHeal',
                        PlayerHPRegen=0,
                        PlayerAPRegen=+20)
# Armour=======================================================================

ha0001 = classes.heavyArmour(ID='ha0001',       #Creates function for armor to be called upon later
                             name='Iron Armor',     #Specifies name of armor
                             weight=10,     #Sets weight of armor
                             value=100,     #Sets value of armor incase of it being sold
                             desc='A simple set of iron armor',     #Description
                             apparelClass='heavy',  #Weight class of armor, possible debuffs later
                             defense=10,    #Defense, negation of damage
                             effects='none')        #Effects given to use of armor
la0001 = classes.lightArmour(ID='la0001',
                             name='Leather Armor',
                             weight=5,
                             value=100,
                             desc='A simple set of leather armor',
                             apparelClass='light',
                             defense=5,
                             effects='none')

cl0001 = classes.clothing(ID='cl0001',
                          name='Apprentice Robes',
                          weight=1,
                          value=100,
                          desc='A simple set of robes',
                          apparelClass='clothing',
                          defense=0,
                          effects='none')

# Weapons======================================================================

hw0001 = classes.heavyWeapon(ID='hw0001',       #Created ID for weapon

                             name='Iron Sword',     #Specifies name

                             weight=10,     #Sets weight of wepon

                             value=100,     #Sets value of wepon to be possible sold

                             desc='A simple iron sword',    #Description

                             weaponClass='heavy',       #Specifies class of weapon

                             effects='none',        #Specifies if weapon has any special effects

                             move1=mv0001,  #Sets moves that user can do when having the weapon equiped

                             move2=mv0002,

                             move3=mv0003,

                             StrReq=10,     #Sets Strength requirment for use of weapon

                             DexReq=4,      #Sets Dexterity requirment for use of weapon

                             IntReq=0)      #Sets Intelligence requirement for use of weapon

lw0001 = classes.lightWeapon(ID='lw0001',

                             name='Iron Dagger',

                             weight=2,

                             value=100,

                             desc='A simple iron dagger',

                             weaponClass='light',

                             effects='none',

                             move1=mv0001,

                             move2=mv0002,

                             move3=mv0004,

                             StrReq=4,

                             DexReq=10,

                             IntReq=0)

mw0001 = classes.magicWeapon(ID='mw0001',

                             name='wood staff',

                             weight=7,

                             value=100,

                             desc='A simple sorcerer staff',

                             weaponClass='magic',

                             effects='none',

                             move1=mv0005,

                             move2=mv0006,

                             move3=mv0007,

                             StrReq=10,

                             DexReq=4,

                             IntReq=0)

# Accessories==================================================================

ac0001 = classes.accessories(ID='ac0001',   #Creates ID for accessory

                             name='ruby ring',  #Sets name of accessory

                             weight=1,      #Sets weight of accessory

                             value=500,     #Sets value of accessory to possible be sold later

                             desc='a silver ring with a ruby inside',   #Description

                             accClass='ring',   #Sets type of accesssory

                             statEffect='+10 max hp')       #Specifies what effects the accessory gives to user

ac0002 = classes.accessories(ID='ac0002',

                             name='travellers cloak',

                             weight=5,

                             value=50,

                             desc='a brown, dusty cloak',

                             accClass='cloak',

                             statEffect='+2 dexterity')

ac0003 = classes.accessories(ID='ac0003',

                             name='mystic pendant',

                             weight=3,

                             value=500,

                             desc='a mystic pendant with ancient words inscribed on it',

                             accClass='pendant',

                             statEffect='+30 max ap')

# Items========================================================================

it0001 = classes.items(ID='it0001',         #Creates ID

                       name='health potion',        #Sets a name

                       weight=2,        #Sets weight of item

                       value=250,       #Sets value of itme to possible be sold later

                       desc='a weak health potion',     #Description

                       effect=ef0001)       #Specifies what effect item gives user upon use

it0002 = classes.items(ID='it0001',

                       name='mana potion',

                       weight=2,

                       value=300,

                       desc='a weak mana potion',

                       effect=ef0002)

# Currency======================================================================

cu0001 = classes.currency(ID='cu0001',  #Sets ID for currency to be called upon later

                          name='gold',    #Specifies name of the currency

                          weight=0,     #Weight of a single 'gold'

                          value=1,      #Worth of the currency

                          desc='The common currency in the world of Thule.')    #Description

cu0002 = classes.currency(ID='cu0002',

                          name='Diamond',

                          weight=0.5,

                          value=600,

                          desc='The clear reflections in the diamond make it the ultimate jewel for the wealthy.')

cu0003 = classes.currency(ID='cu0003',

                          name='Ruby',

                          weight=0.2,

                          value=350,

                          desc='The shining allure of the Ruby makes it popular with all wealth classes, and into all jewelers shops.')

cu0004 = classes.currency(ID='cu0004',

                          name='Sapphire',

                          weight=0.1,

                          value=250,

                          desc='The blue of the Sapphire reflects the allure of the sky, making it popular in use for jewelry.')

# Npc's=======================================================================
npc0001 = classes.npc(name='Black Knight',      #Specifies name of NPC

                      level=1,     #Sets base level

                      desc='A well trained swordsman fighting for the Black faction.',  #Description

                      essential='no',       #Sets if NPC is essential or not(if it is essetial it can't die)

                      hostile='yes',        #Specifies if NPC is an enemy NPC

                      HP=40,        #Sets base Health stat of NPC

                      AP=20,        #Sets base Stamina stat of NPC

                      move1=mv0001,     #Specifies which moves the NPc cna use in battle

                      move2=mv0003,

                      move3=mv0002)

npc0002 = classes.npc(name='Undead Warrior',

                      level=1,

                      desc='A resurrected swordsman infused with the will to protect something.',

                      essential='no',

                      hostile='yes',

                      HP=30,

                      AP=30,

                      move1=mv0010,

                      move2=mv0009,

                      move3=mv0012)

npc0003 = classes.npc(name='Undead Archer',

                      level=1,

                      desc='A fallen bowman who has resurrected in need to protect something.',

                      essential='no',

                      hostile='yes',

                      HP=15,

                      AP=40,

                      move1=mv0013,

                      move2=mv0011,

                      move3=mv0000)

npc0004 = classes.npc(name='Undead Pilgrim',

                      level=1,

                      desc='A resurrected pilgrim with near to no strength.',

                      essential='no',

                      hostile='yes',

                      HP=10,

                      AP=10,

                      move1=mv0012,

                      move2=mv0008,

                      move3=mv0010)

npc0005 = classes.npc(name='Black Legionnaire',

                      level=1,

                      desc='A well trained sword and shield barrier, of the Black faction.',

                      essential='no',

                      hostile='yes',

                      HP=45,

                      AP=20,

                      move1=mv0002,

                      move2=mv0003,

                      move3=mv0001)

npc0006 = classes.npc(name='Black Rogue',

                      level=1,

                      desc='A well trained soldier trained in the fighting style based upon speed and small weaponry ',

                      essential='no',

                      hostile='yes',

                      HP=15,

                      AP=40,

                      move1=mv0001,

                      move2=mv0011,

                      move3=mv0004)

npc0007 = classes.npc(name='Black Battlemage',

                      level=1,

                      desc='A mage of the Black faction well versed in quick and devastating magic.',

                      essential='no',

                      hostile='yes',

                      HP=20,

                      AP=40,

                      move1=mv0005,

                      move2=mv0006,

                      move3=mv0004)

npc0008 = classes.npc(name='Dungeon Rat',

                      level=1,

                      desc='A rat grown to an unreasonable size from feeding off of the creatures in the dungeon.',

                      essential='no',

                      hostile='yes',

                      HP=15,

                      AP=20,

                      move1=mv0012,

                      move2=mv0008,

                      move3=mv0000)

npc0009 = classes.npc(name='Nested Spider',

                      level=1,

                      desc='An Arachnid grown to large size through making its home in a feeding ground.',

                      essential='no',

                      hostile='yes',

                      HP=25,

                      AP=20,

                      move1=mv0012,

                      move2=mv0008,

                      move3=mv0000)

npc0010 = classes.npc(name='Starving Spider',

                      level=1,

                      desc='An Arachnid starving and in desperation for food',

                      essential='no',

                      hostile='yes',

                      HP=10,

                      AP=15,

                      move1=mv0010,

                      move2=mv0012,

                      move3=mv0000)
# none=========================================================================
none = classes.item(ID='none',
                    name='none',
                    weight=0,
                    value=0,
                    desc='empty slot')
#===============================================================================
# NOTE: if you wanna add quest items and such they'll go here
