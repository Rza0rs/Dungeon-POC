#===========================================================================================
#Inventory==================================================================================
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

    def encodeownedWeapons(self):
            global weaponString
            weaponStats = [self.weapon1, self.weapon2, self.weapon3]
            weaponString = " ".join([str(i) for i in weaponStats])

class ownedArmour(inventory):
    def __init__(self, type, armour1, armour2, armour3):
        self.armour1 = armour1
        self.armour2 = armour2
        self.armour3 = armour3
        super().__init__(type)

    def encodeownedArmour(self):
        global armourString
        armourStats = [self.armour1, self.armour2, self.armour3]
        armourString = " ".join([str(i) for i in armourStats])

class ownedItems(inventory):
    def __init__(self, type, item1, item2, item3):
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        super().__init__(type)

    def encodeownedItems(self):
        global itemString
        itemStats = [[self.item1, self.item2, self.item3]]
        itemString = " ".join([str(i) for i in itemStats])

class ownedAccessories(inventory):
    def __init__(self, type, acc1, acc2, acc3):
        self.acc1 = acc1
        self.acc2 = acc2
        self.acc3 = acc3
        super().__init__(type)

    def encodeownedAccessories(self):
        global accessoryString
        accessoryStats = [[self.acc1, self.acc2, self.acc3]]
        accessoryString = " ".join([str(i) for i in accessoryStats])

class equippedWeapons(inventory):
    def __init__(self, type, primary):
        self.primary = primary
        super().__init__(type)

    def encodeequippedWeapons(self):
        global eweaponString
        eweaponStats = [self.primary]
        eweaponString = " ".join([str(i) for i in eweaponStats])

class equippedArmour(inventory):
    def __init__(self, type, helm, chest, arms, boots):
        self.helm = helm
        self.chest = chest
        self.arms = arms
        self. boots = boots
        super().__init__(type)

    def encodeequippedArmour(self):
        global earmourString
        earmourStats = [self.helm, self.chest, self.arms, self.boots]
        earmourString = " ".join([str(i) for i in earmourStats])

class equippedAccessories(inventory):
    def __init__(self, type, ring1, ring2, ring3, ring4):
        self.ring1 = ring1
        self.ring2 = ring2
        self.ring3 = ring3
        self.ring4 = ring4
        super().__init__(type)

    def encodeequippedAccessories(self):
        global accString
        accStats = [self.ring1, self.ring2, self.ring3, self.ring4]
        accString = " ".join([str(i) for i in accStats])

class beltItems(inventory):
    def __init__(self, type, pouch1, pouch2, pouch3, pouch4, pouch5, pouch6):
        self.pouch1 = pouch1
        self.pouch2 = pouch2
        self.pouch3 = pouch3
        self.pouch4 = pouch4
        self.pouch5 = pouch5
        self.pouch6 = pouch6
        super().__init__(type)

    def encodebeltItems(self):
        global beltString
        beltStats = [self.pouch1, self.pouch2, self.pouch3, self.pouch4, self.pouch5, self.pouch6]
        beltString = " ".join([str(i) for i in beltStats])
#=============================================================================================
#item classes=================================================================================
class item():
    'objects that can be held by player characters or npcs'
    def __init__(self, ID, name, weight, value, desc):
        self.ID = ID
        self.name = name
        self.weight = weight
        self.value = value 
        self.desc = desc
            
#weapon classes--------------------------------------------------------------------------------
class weapon(item):
    'weapons'
    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq):
        self.weaponClass = weaponClass
        self.effects = effects
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.StrReq = StrReq
        self.DexReq = DexReq
        self.IntReq = IntReq
        super().__init__( ID, name, weight, value, desc)
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
    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq):
        super().__init__( ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq)
class lightWeapon(weapon):
    'light weapons'
    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq):
        super().__init__( ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq)
class magicWeapon(weapon):
    'magic weapons'
    def __init__(self, ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq):
        super().__init__( ID, name, weight, value, desc, weaponClass, effects, move1, move2, move3, StrReq, DexReq, IntReq)
#apparel classes---------------------------------------------------------------------------------
class apparel(item):
    'apparel'
    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        self.apparelClass = apparelClass
        self.defense = defense
        self.effects = effects
        super().__init__( ID, name, weight, value, desc)
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
        super().__init__( ID, name, weight, value, desc, apparelClass, defense, effects)
        
class lightArmour(apparel):
    'light armour'
    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):  
        super().__init__( ID, name, weight, value, desc, apparelClass, defense, effects)
        
class clothing(apparel):
    'clothes'
    def __init__(self, ID, name, weight, value, desc, apparelClass, defense, effects):
        super().__init__( ID, name, weight, value, desc, apparelClass, defense, effects)
        
#=============================================================================================
#Accessories==================================================================================
class accessories(item):
    'accessories'
    def __init__(self, ID, name, weight, value, desc, accClass, statEffect):
        self.accClass = accClass
        self.statEffect = statEffect
        super().__init__( ID, name, weight, value, desc)
    def accessoryStats(self):
        print('Name -', self.name)
        print('Weight -', self.weight)
        print('Value -', self.value)
        print('Descripton -', self.desc)
        print('Class -', self.accClass)
        print('Defense -', self.statEffect)

#=============================================================================================
#Items========================================================================================
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

#=============================================================================================
#actor classes================================================================================
class actor():
    'actors'
    def __init__(self, name, level, essential, HP, AP):
        self.name = name
        self.level = level      
        self.essential = essential
        self.HP = HP
        self.AP = AP
#----------------------------------------------------------------------------------------------
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
    def encodeStats(self):
        global statsString
        stats  = [self.name, self.subclass, self.level, self.HP, self.AP, self.Str, self.Dex, self.Int, self.essential, self.location]
        statsString = " ".join([str(i) for i in stats])
        saveFile = open("saveFile.txt", "w")
        saveFile.write (statsString)
        saveFile.close()
#-----------------------------------------------------------------------------------------------
class npc(actor):
    'non-player characters'
    def __init__(self, name, level, desc, essential, hostile, HP, AP, loot):
        self.hostile = hostile
        self.loot = loot
        self.desc = desc
        super().__init__(name, level, essential, HP, AP)
    def npcStats(self):
        print(self.name)
        print(self.level)
        print(self.desc)
        print('essential? -', self.essential)
        print('hostile? -', self.hostile)
        print(self.HP)
        print(self.AP)
        print('Drops -', self.loot)
#=================================================================================================

