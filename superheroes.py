import random

class Ability:

    def __init__(self, name, max_damage):
        '''Create Instance Variables:
        name: String
        max_damage: Integer
        '''
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        ''' Return a random value between 0 and 
        the initialized max_damage strength. ''' 
        return random.randint(0, self.max_damage)

class Armor:

    def __init__(self, name, max_block):
        ''' Create Instance Variables:
        name: String
        max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        ''' Return a random value between 0 and 
        the initialized max_block strength. ''' 
        return random.randint(0, self.max_block)

class Hero:
    
    def __init__(self, name, starting_health=100):
        '''Create Instance Variables:
        name: String
        starting_health: Integer

        Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.abilities = []
        self.armors = []
        self.current_health = self.starting_health

    def add_ability(self, ability):
        self.abilities.append(ability)
    
    def attack(self):
        '''Calculate the total damage from all ability attacks.
          return: total: Integer
        '''
        damage = 0
        for ability in self.abilities:
            damage += ability.attack()
        return damage

    def add_armor(self, armor):
        '''Add armor to self.armors
            armor: Armor object
        '''
        self.armors.append(armor)

    def defend(self):
        ''' Runs 'block' method on each armor
            Returns sum of all blocks 
        '''
        sum = 0
        for armor in self.armors:
            sum += armor.block()
        return sum

    def take_damage(self, damage):
        '''Updates self.current_health to reflect damage minus defense'''
        defense = self.defend()
        damage = damage - defense
        self.current_health -= damage

    def is_alive(self):
        return self.current_health > 0

    def fight(self, opponent):
        while self.is_alive() and opponent.is_alive():
            if not self.abilities and not opponent.abilities:
                print("Draw")
            else:
                damage = self.attack()
                print(damage)
                opponent.take_damage(damage)
                damage = opponent.attack()
                print(damage)
                self.take_damage(damage)

        if self.is_alive():
            print(self.name + ' won!')
        else:
            print(opponent.name + ' won!')
            
if __name__=="__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
