import random

def get_user_choice():
    """Låt spelaren välja sten, sax eller påse."""
    while True:
        user_choice = input("Välj sten, sax eller påse: ").lower()
        if user_choice in ["sten", "sax", "påse"]:
            return user_choice
        else:
            print("Ogiltigt val. Försök igen.")

def get_computer_choice():
    """Datorn slumpar sitt val av sten, sax eller påse."""
    return random.choice(["sten", "sax", "påse"])

def determine_winner(player_choice, computer_choice):
    """Avgör vinnaren baserat på spelarens och datorns val."""
    if player_choice == computer_choice:
        return "Oavgjort"
    elif (
        (player_choice == "sten" and computer_choice == "sax") or
        (player_choice == "sax" and computer_choice == "påse") or
        (player_choice == "påse" and computer_choice == "sten")
    ):
        return "Du vinner!"
    else:
        return "Datorn vinner!"

def play_game():
    print("Välkommen till Sten-Sax-Påse!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nDu valde: {user_choice}")
        print(f"Datorn valde: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"\nResultat: {result}")

        play_again = input("Vill du spela igen? (ja/nej): ").lower()
        if play_again != "ja":
            print("Tack för att du spelade. Hejdå!")
            break

if __name__ == "__main__":
    play_game()
