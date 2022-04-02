import random
import argparse
import time

random.seed(0)


class Die:
    def __init__(self):
        self.sides = 6
        self.roll()

    def roll(self):
        self.value = int(random.random() * self.sides + 1)


class Factory:
    def __init__(self):
        player_type = input("Please enter 'p' to play against another human, or 'c' to play against a computer:")

        if player_type == 'p':
            self.p1 = Player("Player1")
            self.p2 = Player("Player2")
        elif player_type == 'c':
            self.p1 = Player("Player")
            self.p2 = ComputerPlayer("Computer")
        elif player_type != 'p' or player_type != 'c':
            self.p1 = ComputerPlayer("Computer1")
            self.p2 = ComputerPlayer("Computer2")
        else:
            print("Try again, Not an option")


class Game:
    def __init__(self, p1, p2):
        self.die = Die()
        self.p1 = p1
        self.p2 = p2
    """
    main gameplay, checks for a winner or continues gameplay
    """
    def play(self):
        while self.p1.score <= 100 and self.p2.score <= 100:
            self.p1.turn()
            if self.p1.score < 100:
                self.p2.turn()
        if self.p1.score > self.p2.score:
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')


class Player:
    def __init__(self, title):
        self.name = title
        self.score = 0
        self.die = Die()

    """
    while loop continues player's turn until 1 is rolled or 'h' entered.
    """

    def turn(self):
        round_score = 0
        roll_again = 'r'

        while roll_again == 'r':
            self.die.roll()
            roll = self.die.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                roll_again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                print("{}'s round score is {}".format(self.name, round_score))
                roll_again = input('Roll = r or Hold = h?  ')
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))


class ComputerPlayer(Player):
    def turn(self):
        round_score = 0
        roll_again = 'r'

        while roll_again == 'r':
            self.die.roll()
            roll = self.die.value
            if roll == 1:
                print('{} rolled a 1'.format(self.name))
                round_score = 0
                roll_again = 'n'
            else:
                print('{} rolled a {}'.format(self.name, roll))
                round_score = round_score + roll
                if round_score < (25 if 25 < (100 - self.score) else (100 - self.score)):
                    roll_again = 'r'
                else:
                    roll_again = 'n'
                print("{}'s round score is {}".format(self.name, round_score))
        self.score += round_score
        print("{}'s turn is over".format(self.name))
        print("{}'s total score is {}\n\n".format(self.name, self.score))


# determine game type and player type

def main():
    parser = argparse.ArgumentParser(description='choose type of player')
    parser.add_argument('player1',  type=str, metavar='player1', help='Enter "p" to play against another human or "c" to play against the computer')
    parser.add_argument('player2', type=str, metavar='player2',  help='Enter "p" to play against another human or "c" to play against the computer')
    args = parser.parse_args()

    if args.player1 == 'p' and args.player2 == 'p':
        print('Lets play Pig!')
        p1 = Player('Player 1')
        p2 = Player('Player 2')
        pig = Game(p1, p2)
        pig.play()

        print('Rerun program to play again')

    if args.player1 == 'c' and args.player2 == 'c':
        print('Lets play Pig!')
        p1 = ComputerPlayer('Player 1')
        p2 = ComputerPlayer('Player 2')
        pig = Game(p1, p2)
        pig.play()

        print('Rerun program to play again')

    if args.player1 == 'c' and args.player2 == 'p':
        print('Lets play Pig!')
        p1 = ComputerPlayer('Player 1')
        p2 = Player('Player 2')
        pig = Game(p1, p2)
        pig.play()
        print('Rerun program to play again')

    if args.player1 == 'p' and args.player2 == 'c':
        print('Lets play Pig!')
        p1 = Player('Player 1')
        p2 = ComputerPlayer('Player 2')
        pig = Game(p1, p2)
        pig.play()
        print('Rerun program to play again')


if __name__ == "__main__":
    main()

