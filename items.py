import classes
#Moves======================================================================
mv0001 = classes.move(name="slash",
                      OpponentHPDamage=-10,
                      OpponentAPDamage=0,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-5)
mv0002 = classes.move(name="stab",
                      OpponentHPDamage=-20,
                      OpponentAPDamage=0,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-25)
mv0003 = classes.move(name="bash",
                      OpponentHPDamage=-5,
                      OpponentAPDamage=-20,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-10)
mv0004 = classes.move(name="evade",
                      OpponentHPDamage=0,
                      OpponentAPDamage=0,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-18)
mv0005 = classes.move(name="fireball",
                      OpponentHPDamage=-20,
                      OpponentAPDamage=0,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-20)
mv0006 = classes.move(name="frostfall",
                      OpponentHPDamage=-5,
                      OpponentAPDamage=-20,
                      PlayerHPDamage=0,
                      PlayerAPDamage=-15)
mv0007 = classes.move(name="heal",
                      OpponentHPDamage=0,
                      OpponentAPDamage=0,
                      PlayerHPDamage=+30,
                      PlayerAPDamage=-20)

import classes

#Armour=======================================================================

ha0001 = classes.heavyArmour(ID = 'ha0001',
                             name = 'Iron Armor',
                             weight = 10,
                             value = 100,
                             desc = 'A simple set of iron armor',
                             apparelClass = 'heavy',
                             defense = 10,
                             effects = 'none')
la0001 = classes.lightArmour(ID = 'la0001',
                             name = 'Leather Armor',
                             weight = 5,
                             value = 100,
                             desc = 'A simple set of leather armor',
                             apparelClass = 'light',
                             defense = 5,
                             effects = 'none')

cl0001 = classes.clothing(ID = 'cl0001',
                          name = 'Apprentice Robes',
                          weight = 1,
                          value = 100,
                          desc = 'A simple set of robes',
                          apparelClass = 'clothing',
                          defense = 0,
                          effects = 'none')

#Weapons======================================================================

hw0001 = classes.heavyWeapon(ID = 'hw0001',

                             name = 'Iron Sword',

                             weight = 10,

                             value = 100,

                             desc = 'A simple iron sword',

                             weaponClass = 'heavy',

                             effects = 'none',

                             move1 = 'slash',

                             move2 = 'stab',

                             move3 = 'bash',

                             StrReq = 10,

                             DexReq = 4,

                             IntReq = 0)

lw0001 = classes.lightWeapon(ID = 'lw0001',

                             name = 'Iron Dagger',

                             weight = 2,

                             value = 100,

                             desc = 'A simple iron dagger',

                             weaponClass = 'light',

                             effects = 'none',

                             move1 = 'slash',

                             move2 = 'stab',

                             move3 = 'evade',

                             StrReq = 4,

                             DexReq = 10,

                             IntReq = 0)

mw0001 = classes.magicWeapon(ID = 'mw0001',

                             name = 'wood staff',

                             weight = 7,

                             value = 100,

                             desc = 'A simple sorcerer staff',

                             weaponClass = 'magic',

                             effects = 'none',

                             move1 = 'fireball',

                             move2 = 'frostfall',

                             move3 = 'magicshield',

                             StrReq = 10,

                             DexReq = 4,

                             IntReq = 0)

#Accessories==================================================================

ac0001 = classes.accessories(ID = 'ac0001',

                             name = 'ruby ring',

                             weight = 1,

                             value = 500,

                             desc = 'a silver ring with a ruby inside',

                             accClass = 'ring',

                             statEffect = '+10 max hp')

ac0002 = classes.accessories(ID = 'ac0002',

                             name = 'travellers cloak',

                             weight = 5,

                             value = 50,

                             desc = 'a brown, dusty cloak',

                             accClass = 'cloak',

                             statEffect = '+2 dexterity')

ac0003 = classes.accessories(ID = 'ac0003',

                             name = 'mystic pendant',

                             weight = 3,

                             value = 500,

                             desc = 'a mystic pendant with ancient words inscribed on it',

                             accClass = 'pendant',

                             statEffect = '+30 max ap')

#Items========================================================================

it0001 = classes.items(ID = 'it0001',

                             name = 'health potion',

                             weight = 2,

                             value = 250,

                             desc = 'a weak health potion',

                             effect = '+30 hp')

it0002 = classes.items(ID = 'it0001',

                             name = 'mana potion',

                             weight = 2,

                             value = 300,

                             desc = 'a weak mana potion',

                             effect = '+40 ap')

#Currency======================================================================

cu0001 = classes.currency(ID = 'cu0001',

                          name ='gold',

                          weight = 0,

                          value = 1,

                          desc = 'The common currency in the world of Thule.')

cu0002 = classes.currency(ID = 'cu0002',

                          name='Diamond',

                          weight=0.5,

                          value=600,

                          desc='The clear reflections in the diamond make it the ultimate jewel for the wealthy.')

cu0003 = classes.currency(ID = 'cu0003',

                          name='Ruby',

                          weight=0.2,

                          value=350,

                          desc='The shining allure of the Ruby makes it popular with all wealth classes, and into all jewelers shops.')

cu0004 = classes.currency(ID = 'cu0004',

                          name='Sapphire',

                          weight=0.1,

                          value=250,

                          desc='The blue of the Sapphire reflects the allure of the sky, making it popular in use for jewelry.')


#Npc's=======================================================================
npc0001 = classes.npc(name = '',

                      level = ,

                      desc = ,

                      essential = '',

                      hostile = '',

                      HP = ,

                      AP = ,)

#NOTE: if you wanna add quest items and such they'll go here




