import random

def choose_random_word():
    word_list = ["python", "programming", "hangman", "developer", "coding", "debugging"]
    return random.choice(word_list)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    max_attempts = 6
    guessed_letters = []
    word_to_guess = choose_random_word()

    print("Välkommen till Hangman!")
    print("Ordet består av", len(word_to_guess), "bokstäver.")

    while max_attempts > 0:
        guess = input("Gissa en bokstav: ").lower()

        if guess.isalpha() and len(guess) == 1:
            if guess in guessed_letters:
                print("Du har redan gissat den bokstaven. Försök igen.")
                continue

            guessed_letters.append(guess)

            if guess in word_to_guess:
                print("Bra gissning! Ordet:", display_word(word_to_guess, guessed_letters))
            else:
                max_attempts -= 1
                print("Fel gissning. Du har", max_attempts, "försök kvar.")

            if set(guessed_letters) == set(word_to_guess):
                print("Grattis! Du har gissat rätt ord:", word_to_guess)
                break

        else:
            print("Vänligen gissa en enskild bokstav.")

    if max_attempts == 0:
        print("Tyvärr, du har inga fler försök. Rätt ord var:", word_to_guess)

if __name__ == "__main__":
    hangman()
