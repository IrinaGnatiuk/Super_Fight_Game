import random


class Player:
    name = "player"

    def __init__(self, name, power, skill, health):
        self.name = name
        self.power = power
        self.skill = skill
        self.health = health

    def info_player(self):
        print('Your {} :  {} '.format(Player.name, self.name))

    @classmethod
    def choice(cls):
        choice = int(input('Please select warrior: 1 - strong, 2 - healthy, 3 - skill'))
        if choice == 1:
            player = player1
        elif choice == 2:
            player = player2
        elif choice == 3:
            player = player3
        return cls(player.name, player.power, player.skill, player.health)


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
            opponent = opponent1
        elif choice == 2:
            opponent = opponent2
        elif choice == 3:
            opponent = opponent3
        return cls(opponent.name, opponent.power, opponent.skill, opponent.health)


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


player1 = Player('Power man', 15, 1.0, 100)
player2 = Player('Healthy man', 10, 1.0, 150)
player3 = Player('Skill man', 10, 2.0, 100)
opponent1 = Opponent('Power man', 15, 1.0, 100)
opponent2 = Opponent('Healthy man', 10, 1.0, 150)
opponent3 = Opponent('Skill man', 10, 2.0, 100)
print(Fight.start)
player = Player.choice()
player.info_player()
opponent = Opponent.choice()
opponent.info_opponent()
Fight.fithing(player, opponent)











