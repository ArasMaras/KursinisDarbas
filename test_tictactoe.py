import unittest
from unittest.mock import patch
from io import StringIO
import json
from tictactoe import Player, HumanPlayer, Game, GameFactory, ScoreBoard

class TestPlayer(unittest.TestCase):
    def test_get_move(self):
        player = Player("Test", 'X')
        
        with patch('builtins.input', side_effect=['1']):
            move = player.get_move()
            self.assertEqual(move, 1)
        
        with patch('builtins.input', side_effect=['abc', '2']):
            move = player.get_move()
            self.assertEqual(move, 2)

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
        self.player1 = HumanPlayer("Player1", 'X')
        self.player2 = HumanPlayer("Player2", 'O')
        self.game.add_player(self.player1)
        self.game.add_player(self.player2)

    def test_switch_player(self):
        self.game.current_player = self.player1
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.player2)
        self.game.switch_player()
        self.assertEqual(self.game.current_player, self.player1)

    def test_check_win(self):
        self.game.board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.game.player_positions['X'] = [1, 2, 3]
        self.assertTrue(self.game.check_win())

        self.game.board = [' ', ' ', ' ', 'X', 'X', 'X', ' ', ' ', ' ']
        self.game.player_positions['X'] = [4, 5, 6]
        self.assertTrue(self.game.check_win())

        self.game.board = [' ', ' ', ' ', ' ', ' ', ' ', 'X', 'X', 'X']
        self.game.player_positions['X'] = [7, 8, 9]
        self.assertTrue(self.game.check_win())

        self.game.board = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.game.player_positions['X'] = [1, 4, 7]
        self.assertTrue(self.game.check_win())

        self.game.board = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X', ' ']
        self.game.player_positions['X'] = [2, 5, 8]
        self.assertTrue(self.game.check_win())

        self.game.board = [' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ', 'X']
        self.game.player_positions['X'] = [3, 6, 9]
        self.assertTrue(self.game.check_win())

        self.game.board = ['X', ' ', ' ', ' ', 'X', ' ', ' ', ' ', 'X']
        self.game.player_positions['X'] = [1, 5, 9]
        self.assertTrue(self.game.check_win())

        self.game.board = [' ', ' ', 'X', ' ', 'X', ' ', 'X', ' ', ' ']
        self.game.player_positions['X'] = [3, 5, 7]
        self.assertTrue(self.game.check_win())

    def test_check_draw(self):
        self.game.player_positions = {'X': [1, 3, 4, 5, 7], 'O': [2, 6, 8, 9]}
        self.assertTrue(self.game.check_draw())

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['1', '2', '3', '4', '5', '6', '7', '8', '9'])
    def test_play_game(self, mock_input, mock_print):
        self.assertEqual(self.game.play(), 'Player1')

class TestScoreBoard(unittest.TestCase):
    def setUp(self):
        self.scoreboard = ScoreBoard()

    def test_update_score(self):
        self.scoreboard.update_score('Player1')
        self.assertEqual(self.scoreboard.scores['Player1'], 1)

        self.scoreboard.update_score('Player1')
        self.assertEqual(self.scoreboard.scores['Player1'], 2)

        self.scoreboard.update_score('Player2')
        self.assertEqual(self.scoreboard.scores['Player2'], 1)

    def test_save_load_scoreboard(self):
        self.scoreboard.update_score('Player1')
        self.scoreboard.update_score('Player2')

        self.scoreboard.save_to_file('test_scoreboard.json')

        new_scoreboard = ScoreBoard()
        new_scoreboard.load_from_file('test_scoreboard.json')

        self.assertEqual(new_scoreboard.scores['Player1'], 1)
        self.assertEqual(new_scoreboard.scores['Player2'], 1)

if __name__ == '__main__':
    unittest.main()

