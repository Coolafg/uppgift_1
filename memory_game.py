import random

def generate_sequence(length):
    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return [random.choice(symbols) for _ in range(length)]

def display_sequence(sequence):
    print("Sekvensen är:", " ".join(sequence))

def shuffle_sequence(sequence):
    shuffled = sequence.copy()
    random.shuffle(shuffled)
    return shuffled

def get_player_input():
    player_input = input("Ange den ordning du tror på, separerad med mellanslag: ")
    return player_input.split()

def check_guess(original, guess):
    return original == guess

def memory_game(difficulty):
    length_dict = {"easy": 4, "medium": 6, "hard": 8}
    length = length_dict.get(difficulty.lower(), 4)

    original_sequence = generate_sequence(length)
    display_sequence(original_sequence)

    input("Tryck Enter för att fortsätta...")
    print("\n" * 50)  # Rensa konsolen

    shuffled_sequence = shuffle_sequence(original_sequence)
    display_sequence(shuffled_sequence)

    player_guess = get_player_input()

    if check_guess(original_sequence, player_guess):
        print("Grattis! Du har gissat rätt ordning.")
    else:
        print("Tyvärr, du har gissat fel. Rätt ordning var:", " ".join(original_sequence))

if __name__ == "__main__":
    difficulty_level = input("Välj svårighetsgrad (easy/medium/hard): ")
    memory_game(difficulty_level)
