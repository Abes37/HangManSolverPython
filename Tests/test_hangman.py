import unittest
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from App.hangman import Hangman

class TestHangman(unittest.TestCase):

    def setUp(self):
        self.word_to_guess = "hangman"
        self.max_attempts = 6
        self.game = Hangman(self.word_to_guess, self.max_attempts)

    def test_initial_state(self):
        self.assertEqual(self.game.word, self.word_to_guess)
        self.assertEqual(self.game.attempts_left, self.max_attempts)
        self.assertEqual(self.game.get_display_word(), "_ _ _ _ _ _ _")
        self.assertFalse(self.game.is_won())
        self.assertFalse(self.game.is_lost())

    def test_correct_guess(self):
        self.game.guess('h')
        self.assertIn('h', self.game.guesses)
        self.assertEqual(self.game.get_display_word(), "h _ _ _ _ _ _")
        self.assertEqual(self.game.attempts_left, self.max_attempts)
    
    def test_incorrect_guess(self):
        self.game.guess('z')
        self.assertIn('z', self.game.guesses)
        self.assertEqual(self.game.get_display_word(), "_ _ _ _ _ _ _")
        self.assertEqual(self.game.attempts_left, self.max_attempts - 1)

    def test_repeat_guess(self):
        self.game.guess('h')
        self.assertFalse(self.game.guess('h'))  # Guessing 'h' again should return False
        self.assertEqual(self.game.attempts_left, self.max_attempts)

    def test_win_condition(self):
        for letter in self.word_to_guess:
            self.game.guess(letter)
        self.assertTrue(self.game.is_won())
        self.assertFalse(self.game.is_lost())

    def test_loss_condition(self):
        incorrect_guesses = ['z', 'x', 'y', 'q', 'w', 'r']
        for letter in incorrect_guesses:
            self.game.guess(letter)
        self.assertTrue(self.game.is_lost())
        self.assertFalse(self.game.is_won())

if __name__ == '__main__':
    unittest.main()
