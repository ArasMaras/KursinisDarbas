import json
import unittest
from unittest.mock import patch
from io import StringIO

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def get_move(self):
        try:
            move = int(input(f"Player {self.name} ({self.symbol}) turn. Which box? : "))
            return move
        except ValueError:
            print("Wrong Input!!! Try Again")
            return self.get_move()

class HumanPlayer(Player):
    pass

class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.player_positions = {'X': [], 'O': []}
        self.players = []
        self.current_player = None

    def add_player(self, player):
        self.players.append(player)

    def switch_player(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def print_board(self):
        print("\n")
        for i in range(0, 9, 3):
            print("\t     |     |")
            print(f"\t  {self.get_display_char(i)}  |  {self.get_display_char(i+1)}  |  {self.get_display_char(i+2)}")
            if i < 6:
                print('\t_____|_____|_____')
        print("\t     |     |")
        print("\n")

    def get_display_char(self, index):
        return self.board[index] if self.board[index] != ' ' else str(index + 1)

    def check_win(self):
        soln = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]
        for x in soln:
            if all(pos in self.player_positions[self.current_player.symbol] for pos in x):
                return True
        return False

    def check_draw(self):
        return len(self.player_positions['X']) + len(self.player_positions['O']) == 9

    def play(self):
        self.current_player = self.players[0]
        while True:
            self.print_board()
            move = self.current_player.get_move()
            if move < 1 or move > 9 or self.board[move-1] != ' ':
                print("Invalid move, try again.")
                continue
            self.board[move-1] = self.current_player.symbol
            self.player_positions[self.current_player.symbol].append(move)
            if self.check_win():
                self.print_board()
                print(f"Player {self.current_player.name} ({self.current_player.symbol}) has won the game!!")
                return self.current_player.name
            if self.check_draw():
                self.print_board()
                print("Game Drawn")
                return None
            self.switch_player()

class GameFactory:
    @staticmethod
    def create_game(player1_name, player2_name):
        game = Game()
        game.add_player(HumanPlayer(player1_name, 'X'))
        game.add_player(HumanPlayer(player2_name, 'O'))
        return game

class ScoreBoard:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ScoreBoard, cls).__new__(cls)
            cls._instance.scores = {}
        return cls._instance

    def update_score(self, player_name):
        if player_name in self.scores:
            self.scores[player_name] += 1
        else:
            self.scores[player_name] = 1

    def print_scoreboard(self):
        print("\t--------------------------------")
        print("\t              SCOREBOARD       ")
        print("\t--------------------------------")
        for player, score in self.scores.items():
            print(f"\t   {player}\t    {score}")
        print("\t--------------------------------\n")

    def save_to_file(self, filename='scoreboard.json'):
        with open(filename, 'w') as f:
            json.dump(self.scores, f)

    def load_from_file(self, filename='scoreboard.json'):
        try:
            with open(filename, 'r') as f:
                self.scores = json.load(f)
        except FileNotFoundError:
            self.scores = {}

def run_tests():
    unittest.main(module='test_tictactoe', exit=False)

def main():
    print("Do you want to run the game or the tests?")
    choice = input("Enter 'game' to play or 'test' to run tests: ").strip().lower()
    
    if choice == 'test':
        run_tests()
    else:
        scoreboard = ScoreBoard()
        scoreboard.load_from_file()
        scoreboard.print_scoreboard()

        player1 = input("Enter Player 1 name: ")
        player2 = input("Enter Player 2 name: ")

        while True:
            game = GameFactory.create_game(player1, player2)
            winner = game.play()
            if winner:
                scoreboard.update_score(winner)
            scoreboard.print_scoreboard()

            play_again = input("Do you want to play again? (y/n): ").lower()
            if play_again != 'y':
                break

        scoreboard.save_to_file()
        scoreboard.print_scoreboard()

if __name__ == "__main__":
    main()
