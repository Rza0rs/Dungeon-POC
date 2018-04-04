# ===========================================================================================
# Inventory==================================================================================

class inventory():
    'the organization of items held by the player'

    def __init__(self, type):
        self.type = type


class ownedWeapons(inventory):

    def __init__(self, type, weapon1, weapon2, weapon3):

        self.weapon1 = weapon1

        self.weapon2 = weapon2

        self.weapon3 = weapon3

        super().__init__(type)



class ownedArmour(inventory):

    def __init__(self, type, armour1, armour2, armour3):

        self.armour1 = armour1

        self.armour2 = armour2

        self.armour3 = armour3

        super().__init__(type)


class ownedItems(inventory):

    def __init__(self, type, item1, item2, item3):

        self.item1 = item1

        self.item2 = item2

        self.item3 = item3

        super().__init__(type)


class ownedAccessories(inventory):

    def __init__(self, type, acc1, acc2, acc3):

        self.acc1 = acc1

        self.acc2 = acc2

        self.acc3 = acc3

        super().__init__(type)


class equippedWeapons(inventory):

    def __init__(self, type, primary):

        self.primary = primary

        super().__init__(type)



class equippedArmour(inventory):

    def __init__(self, type, armour):

        self.armour = armour

        super().__init__(type)


class equippedAccessories(inventory):

    def __init__(self, type, acc1, acc2, acc3, acc4):

        self.acc1 = acc1

        self.acc2 = acc2

        self.acc3 = acc3

        self.acc4 = acc4

        super().__init__(type)



class beltItems(inventory):

    def __init__(self, type, pouch1, pouch2, pouch3, pouch4, pouch5, pouch6):

        self.pouch1 = pouch1

        self.pouch2 = pouch2

        self.pouch3 = pouch3

        self.pouch4 = pouch4

        self.pouch5 = pouch5

        self.pouch6 = pouch6

        super().__init__(type)

#===================================================================
# item classes=================================================================================

class item():
    'objects that can be held by player characters or npcs'

    def __init__(self, ID, name, weight, value, desc):
        self.ID = ID

        self.name = name

        self.weight = weight

        self.value = value

        self.desc = desc

# ==============================================================================================

class currency(item):
    'The currency in the world of Thule.'

    def __init__(self, ID, name, weight, value, desc):
        super().__init__(ID, name, weight, value, desc)

    def currencyDescription(self):
        print('Name -', self.name)

        print('Value -', self.value)

        print('Descripton -', self.desc)


# weapon classes--------------------------------------------------------------------------------

class weapon(item):
    """weapons"""

    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                 IntReq):
        self.weaponClass = weaponClass

        self.effects = effects

        self.move1 = move1

        self.move2 = move2

        self.move3 = move3

        self.StrReq = StrReq

        self.DexReq = DexReq

        self.IntReq = IntReq

        super().__init__(ID, name, weight, value, desc)

    def weaponStats(self):
        print('Name -', self.name)

        print('Weight -', self.weight)

        print('Value -', self.value)

        print('Descripton -', self.desc)

        print('Class -', self.weaponClass)

        print('Effects -', self.effects)

        print('Move 1 -', self.move1)

        print('Move 2 -', self.move2)

        print('Move 3 -', self.move3)

        print('Str requirement -', self.StrReq)

        print('Dex requirement -', self.DexReq)

        print('Int requirement -', self.IntReq)


class heavyWeapon(weapon):
    'heavy weapons'

    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                 IntReq):
        super().__init__(ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                         IntReq)


class lightWeapon(weapon):
    'light weapons'

    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                 IntReq):
        super().__init__(ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                         IntReq)


class magicWeapon(weapon):
    'magic weapons'

    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                 IntReq):
        super().__init__(ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq,
                         IntReq)


# apparel classes---------------------------------------------------------------------------------

class apparel(item):
    'apparel'

    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        self.apparelClass = apparelClass

        self.defense = defense

        self.effects = effects

        super().__init__(ID, name, weight, value, desc)

    def apparelStats(self):
        print('Name -', self.name)

        print('Weight -', self.weight)

        print('Value -', self.value)

        print('Descripton -', self.desc)

        print('Class -', self.apparelClass)

        print('Defense -', self.defense)

        print('Effects -', self.effects)


class heavyArmour(apparel):
    'heavy armour'

    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        super().__init__(ID, name, weight, value, desc, apparelClass, defense, effects)


class lightArmour(apparel):
    'light armour'

    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        super().__init__(ID, name, weight, value, desc, apparelClass, defense, effects)


class clothing(apparel):
    'clothes'

    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        super().__init__(ID, name, weight, value, desc, apparelClass, defense, effects)


# =============================================================================================

# Accessories==================================================================================

class accessories(item):
    'accessories'

    def __init__(self, ID, name, weight, value, desc, accClass, statEffect):
        self.accClass = accClass

        self.statEffect = statEffect

        super().__init__(ID, name, weight, value, desc)

    def accessoryStats(self):
        print('Name -', self.name)

        print('Weight -', self.weight)

        print('Value -', self.value)

        print('Descripton -', self.desc)

        print('Class -', self.accClass)

        print('Defense -', self.statEffect)


# =============================================================================================

# Items========================================================================================

class items(item):
    'items'

    def __init__(self, ID, name, weight, value, desc, effect):
        self.effect = effect

        super().__init__(ID, name, weight, value, desc)

    def itemStats(self):
        print('Name -', self.name)

        print('Weight -', self.weight)

        print('Value -', self.value)

        print('Descripton -', self.desc)

        print('Class -', self.effect)


# =============================================================================================

# actor classes================================================================================

class actor():
    'actors'

    def __init__(self, name, level, essential, HP, AP):
        self.name = name

        self.level = level

        self.essential = essential

        self.HP = HP

        self.AP = AP


# ----------------------------------------------------------------------------------------------

class pc(actor):
    'the player character'

    def __init__(self, name, subclass, level, HP, AP, Str, Dex, Int, essential, location):
        self.location = location

        self.subclass = subclass

        self.Str = Str

        self.Dex = Dex

        self.Int = Int

        super().__init__(name, level, essential, HP, AP)

    def pcStats(self):
        print('Name -', self.name)

        print('Class -', self.subclass)

        print('Level -', self.level)

        print('Health -', self.HP)

        print('Action points -', self.AP)

        print('Strength -', self.Str)

        print('Dexterity -', self.Dex)

        print('Intelligence -', self.Int)

# -----------------------------------------------------------------------------------------------

class npc(actor):
    'non-player characters'

    def __init__(self, name, level, desc, essential, hostile, HP, AP, move1, move2, move3):
        self.hostile = hostile
        self.desc = desc
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        super().__init__(name, level, essential, HP, AP)
    def npcStats(self):
        print(self.name)
        print(self.level)
        print(self.desc)
        print('essential? -', self.essential)
        print('hostile? -', self.hostile)
        print(self.HP)
        print(self.AP)



# =================================================================================================
#=================================================================================================
#Moves classes====================================================================================
class move():
    """moves"""
    def __init__(self, name, OpponentHPDamage, OpponentAPDamage, UserHPDamage, UserAPDamage):
        self.name = name
        self.OpponentHPDamage = OpponentHPDamage
        self.OpponentAPDamage = OpponentAPDamage
        self.UserHPDamage = UserHPDamage
        self.UserAPDamage = UserAPDamage
#=============================================================================================
#Effects Classes==============================================================================
class effect():
    """effets"""
    def __init__(self, name, PlayerHPRegen, PlayerAPRegen):
        self.name = name
        self.PlayerHPRegen = PlayerHPRegen
        self.PlayerAPRegen = PlayerAPRegen
#============================================================`=================================
class combat():
    """combat"""
    def __init__(self, playerHP, playerAP, enemyHP, enemyAP,
                 PTplayerCurrentHP, PTplayerCurrentAP, PTenemyCurrentHP, PTenemyCurrentAP,
                 ETplayerCurrentHP, ETplayerCurrentAP, ETenemyCurrentHP, ETenemyCurrentAP,
                 playerCanFightHP, playerCanFightAP, enemyCanFightHP, enemyCanFightAP):

        self.playerHP = playerHP
        self.playerAP = playerAP
        self.enemyHP = enemyHP
        self.enemyAP = enemyAP

        self.PTplayerCurrentHP = PTplayerCurrentHP
        self.PTplayerCurrentAP = PTplayerCurrentAP
        self.PTenemyCurrentHP = PTenemyCurrentHP
        self.PTenemyCurrentAP = PTenemyCurrentAP

        self.ETplayerCurrentHP = ETplayerCurrentHP
        self.ETplayerCurrentAP = ETplayerCurrentAP
        self.ETenemyCurrentHP = ETenemyCurrentHP
        self.ETenemyCurrentAP = ETenemyCurrentAP

        self.playerCanFightHP = playerCanFightHP
        self.playerCanFightAP = playerCanFightAP
        self.enemyCanFightHP = enemyCanFightHP
        self.enemyCanFightAP = enemyCanFightAP

