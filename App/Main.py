from HangMan import Hangman

def main():
    word_to_guess = "hangman"
    max_attempts = 6
    game = Hangman(word_to_guess, max_attempts)

    print("Welcome to Hangman Solver!")

    while not game.is_won() and not game.is_lost():
        print (f"Word: {game.get_display_word()}")
        guess = input("Enter a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        if game.guess(guess):
            print("Good guess!")
        else:
            print("You already guessed that letter.")
        print(f"Attemtps left: {game.attempts_left}")

    if game.is_won():
        print(f"Congratulations! You guessed the word: {game.word}")
    else:
        print(f"Game over! The word was: {game.word}")

if __name__ == "__main__":
    main()