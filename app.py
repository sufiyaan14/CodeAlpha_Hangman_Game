import random

def choose_word():
    words = ["python", "developer", "software", "hangman", "challenge", "algorithm", "variable"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Attempts left: {attempts}")
        print("Guessed letters:", " ".join(sorted(guessed_letters)) if guessed_letters else "None")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word):
                print(f"\nCongratulations! You guessed the word: {word}")
                break
        else:
            attempts -= 1
            print("Incorrect guess.")
            
    else:
        print(f"\nGame over! The word was: {word}")

if __name__ == "__main__":
    hangman()
