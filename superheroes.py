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


class Weapon(Ability):

    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)


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
        self.deaths = 0
        self.kills = 0

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

    def add_kill(self, num_kills):
        ''' Update kills with num_kills'''
        self.kills += num_kills

    def add_death(self, num_deaths):
        ''' Update deaths with num_deaths '''
        self.deaths += num_deaths

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
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print(opponent.name + ' won!')
            opponent.add_kill(1)
            self.add_death(1)


class Team:
    def __init__(self, name):
        '''Instatiate instance properties

            name: String
            heroes: List of Hero objects
        '''
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)
        print(self.heroes[len(self.heroes)-1].name)

    def remove_hero(self, hero_name):
        '''Remove hero from heroes list given a name
            If hero isn't found, return 0
        '''
        for hero in self.heroes:
            if len(self.heroes) > 0 and hero.name == hero_name:
                self.heroes.remove(hero)
                return 0
        else:
            return 0

    def view_all_heroes(self):
        if len(self.heroes) > 0:
            for hero in self.heroes:
                print(hero.name)
        else:
            print("There are no heroes on this team yet.")

    def attack(self, other_team):
        index = random.randint(0, len(self.heroes)-1)
        my_hero = self.heroes[index]
        index = random.randint(0, len(other_team.heroes)-1)
        my_opponent = other_team.heroes[index]
        my_hero.fight(my_opponent)

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = health
    
    def stats(self):
        for hero in self.heroes:
            if hero.deaths > 0:
                ratio = hero.kills//hero.deaths
                print(hero.name + ": " + ratio)
            else:
                print(hero.name + ": " + hero.kills)


if __name__ == "__main__":
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    team1 = Team("1")
    team1.add_hero(hero1)
    team1.add_hero(hero2)
    team1.remove_hero(hero2)
    team1.view_all_heroes()
    team1.remove_hero(hero1)
    