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
        return random.randint(0, self.max_damage)

class Armour:

    def __init__(self, name, max_block):
        '''Create Instance Variables:
        name: String
        max_block: Integer
        '''
        self.name = name
        self.max_block = max_block

    def block(self):
        pass

class Hero:
    
    def __init__(self, name, starting_health=100):
        '''Create Instance Variables:
        name: String
        starting_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health

    def add_ability(self, ability):
        pass
    
    def attack(self):
        pass

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        pass

if __name__=="__main__":
    ability = Ability('Debugging Ability', 20)
    print(ability.name)
    print(ability.attack())

