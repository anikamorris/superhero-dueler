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

class Armour:

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
        for ability in self.abilities:
            print(ability.attack())

    def defend(self, incoming_damage):
        pass

    def take_damage(self, damage):
        pass

    def is_alive(self):
        pass

    def fight(self, opponent):
        pass

if __name__=="__main__":
    ability = Ability('Great Debugging', 50)
    ability2 = Ability('High Jumps', 90)
    my_hero = Hero('Grace Hopper', 200)
    my_hero.add_ability(ability)
    my_hero.add_ability(ability2)
    print(my_hero.attack())

