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
    
    def add_weapon(self, weapon):
        self.abilities.append(weapon)

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
                return
            else:
                damage = self.attack()
                print(self.name + ': ' + str(damage))
                opponent.take_damage(damage)
                damage = opponent.attack()
                print(opponent.name + ': ' + str(damage))
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
        '''Add hero to heroes list'''
        self.heroes.append(hero)

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

    def show_surviving_heroes(self):
        for hero in self.heroes:
            if hero.is_alive():
                print(hero.name)

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

class Arena:
    def __init__(self):
        '''Instantiate properties
            team_one: None
            team_two: None
        '''
        self.team_one = None
        self.team_two = None

    def create_ability(self):
        ''' Prompt user for Ability information
            return Ability with values from user input'''
        name = input('Name of ability: ')
        max_damage = input('Maximum damage: ')
        ability = Ability(name, int(max_damage))
        return ability
        
    def create_weapon(self):
        ''' Prompt user for Weapon information
            return Weapon with values from user input'''
        name = input('Name of weapon: ')
        max_damage = input('Maximum damage: ')
        weapon = Weapon(name, int(max_damage))
        return weapon
    
    def create_armor(self):
        ''' Prompt user for Armor information
            return Armor with values from user input'''
        name = input('Name of armor: ')
        max_block = input('Maximum block: ')
        armor = Armor(name, int(max_block))
        return armor

    def create_hero(self):
        name = input("Name your hero: ")
        hero = Hero(name)
        menu_option = 0
        while menu_option != '4':
            menu_option = input("Enter 1 to add an ability\nEnter 2 to add a weapon\nEnter 3 to add armor\nEnter 4 when you're done\n")
            if menu_option == '1':
                ability = self.create_ability()
                hero.add_ability(ability)
            elif menu_option == '2':
                weapon = self.create_weapon()
                hero.add_weapon(weapon)
            elif menu_option == '3':
                armor = self.create_armor()
                hero.add_armor(armor)
            elif menu_option == '4':
                print('Finished creating ' + hero.name)
            else:
                print('Please select a value 1-4')
        return hero

    def build_team_one(self):
        '''Prompt the user to build team_one '''
        team_name = input('What is your team name?\n')
        self.team_one = Team(team_name)
        num_heroes = input('How many heroes do you want on your team?\n')
        for i in range(int(num_heroes)):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        '''Prompt the user to build team_two '''
        team_name = input('What is your team name?\n')
        self.team_two = Team(team_name)
        num_heroes = input('How many heroes do you want on your team?\n')
        for i in range(int(num_heroes)):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        '''Battle team_one and team_two'''
        self.team_one.attack(self.team_two)

    def count_alive(self, team):
        ''' Count number of heroes alive on a team'''
        alive = 0
        for hero in team.heroes:
            if hero.is_alive():
                alive += 1
        return alive
    
    def count_kills(self, team):
        ''' Count kills on a team'''
        team_kills = 0
        for hero in team.heroes:
            team_kills += hero.kills
        return team_kills      

    def count_deaths(self, team):
        ''' Count deaths on a team'''
        team_deaths = 0
        for hero in team.heroes:
            team_deaths += hero.deaths  
        return team_deaths

    def who_won(self):
        '''Prints which team won to terminal'''
        team_one_alive = self.count_alive(self.team_one)
        team_two_alive = self.count_alive(self.team_two)
        if team_one_alive > team_two_alive:
            print (self.team_one.name + ' won!')
        elif team_one_alive < team_two_alive:
            print (self.team_two.name + ' won!')
        else:
            print ('Draw!')

    def show_stats(self):
        ''' Prints team statistics to terminal'''
        team1_kills = self.count_kills(self.team_one)
        team1_deaths = self.count_deaths(self.team_one)
        average1_kills = team1_kills // len(self.team_one.heroes)
        average1_deaths = team1_deaths // len(self.team_one.heroes) 

        team2_kills = self.count_kills(self.team_two)
        team2_deaths = self.count_deaths(self.team_two)
        average2_kills = team2_kills // len(self.team_two.heroes)
        average2_deaths = team2_deaths // len(self.team_two.heroes)

        self.who_won()
        print(self.team_one.name + ' average kills: ' + str(average1_kills))
        print(self.team_one.name + ' average deaths: ' + str(average1_deaths))
        print(self.team_one.name + "'s surviving heroes: ")
        self.team_one.show_surviving_heroes()
        
        print(self.team_two.name + ' average kills: ' + str(average2_kills))
        print(self.team_two.name + ' average deaths: ' + str(average2_deaths))
        print(self.team_two.name + "'s surviving heroes: ")
        self.team_two.show_surviving_heroes()
        

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()