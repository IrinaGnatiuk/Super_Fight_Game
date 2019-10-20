import random
import csv


class Player:
    name = "player"

    def __init__(self, name, power, skill, health):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = health

    def __eq__(self, other):
        print('Oдинаковы ли воин {} с воином {}'.format(self.name, other.name))
        return self.power == other.power and self.name == other.name and self.skill == other.skill and self.health == other.health

    def __lt__(self, other):
        print('Mеньше или равна сила воина {} чем сила воина {}'.format(self.name, other.name))
        return print('сила МЕНЬШЕ') if int(self.power) < int(other.power) else print('сила ТАКАЯ ЖЕ')

    def __gt__(self, other):
        print('Больше ли навыки воина {} чем навыки воина{}'.format(self.name, other.name))
        if float(self.skill) > float(other.skill):
            return True
            return False

    def info_player(self):
        print('Your {} :  {} '.format(Player.name, self.name))

    def setter(self, new_value):
        print('присвоено новое имя воину {} теперь его имя {}'.format(self.name, new_value))
        self.name = new_value

    def getter(self):
        return self.name

    @classmethod
    def choice(cls):
        choice = int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill'))
        if choice == 1:
            player = player1
        elif choice == 2:
            player = player2
        elif choice == 3:
            player = player3
        return cls(player.name, int(player.power), float(player.skill), int(player.health))


class Opponent(Player):
    name = "opponent"

    def __init__(self, name, power, skill, health):
        super().__init__(name, power, skill, health)

    def info_opponent(self):
        print('Your {} :  {} '.format(Opponent.name, self.name))

    @classmethod
    def choice(cls):
        choice = random.randint(1,3)
        if choice == 1:
            opponent = player1
        elif choice == 2:
            opponent = player2
        elif choice == 3:
            opponent = player3
        return cls(opponent.name, int(opponent.power), float(opponent.skill), int(opponent.health))


class Fight:

    start = "SUPER FIGHT GAME!"
    level = 1

    def __init__(self):

        self.level += 1

    @classmethod
    def fithing(cls, opponent, player):
        win = False
        while True:
            print('===========================================================================')
            print('LEVEL   {} '. format(cls.level))
            cls.level += 1
            print('Your player HP: ', player.health)
            print('Opponent    HP: ', opponent.health, '\n')
            kick = int(input('Please select kick: 1 - to head, 2 - to body, 3 - to foot = '))
            block = int(input('Please select block: 1 - to head, 2 - to body, 3 - to foot = '))
            print('\n')
            opponent_kick = random.randint(1, 3)
            opponent_block = random.randint(1, 3)
            if kick != opponent_block:
                print('You hit an opponent!')
                opponent.health = opponent.health - (player.power * player.skill)*5
            if block != opponent_kick:
                print('Opponent hit you :( ')
                player.health = player.health - (opponent.power * opponent.skill)*5
            if player.health <= 0:
                break
            if opponent.health <= 0:
                win = True
                break
        if win:
            print('YOU WINNER!!!')
        else:
            print('GAME OVER.')


FILENAME = "warrior1.csv"
dict_players = {}
with open(FILENAME, 'r') as file:
    reader = csv.reader(file)
    for num, line in enumerate(reader, 0):
        dict_players['player ' + str(num)] = Player(name=line[0], power=line[1], skill=line[2], health=line[3])

player1 = dict_players['player 1']
player2 = dict_players['player 2']
player3 = dict_players['player 3']
print(Fight.start)
player = Player.choice()
player.info_player()
opponent = Opponent.choice()
opponent.info_opponent()
Fight.fithing(player, opponent)
player3.setter('Super Skill man')
print(player3.__eq__(player1))
print(player3.__eq__(player3))
print(player3.__lt__(player2))
print(player2.__lt__(player1))
print(player3.__gt__(player1))
