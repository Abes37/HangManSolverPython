class Hangman:
    def __init__(self, word, max_attempts):
        self.word = word
        self.guesses = set()
        self.max_attemps = max_attempts
        self.attempts_left = self.max_attemps

    def guess(self, letter):
        if letter in self.guesses:
            return False
        self.guesses.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1
        return True
    
    def get_display_word(self):
        return ' '.join([letter if letter in self.guesses else '_' for letter in self.word])
    
    def is_won(self):
        return all(letter in self.guesses for letter in self.word)
    
    def is_lost(self):
        return self.attempts_left <= 0