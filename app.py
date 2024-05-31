import random
import emoji

# Expanded choices with corresponding emojis
choices = {
    "🪨": "Rock",
    "📄": "Paper",
    "✂️": "Scissors",
    "🦎": "Lizard",
    "🖖": "Spock"
}

# Function to get and validate player's choice (updated)
def get_player_choice():
    while True:
        print("Choose your champion:")
        for i, (emoji_choice, name) in enumerate(choices.items()):
            print(f"{i+1}. {emoji_choice} {name}")

        choice = input("Enter your choice (1-5): ")
        if choice.isdigit() and 1 <= int(choice) <= len(choices):
            return list(choices.keys())[int(choice) - 1]  # Return the chosen emoji
        else:
            print("Invalid choice. Please try again.")

# Function to generate computer's random choice (updated)
def get_computer_choice():
    return random.choice(list(choices.keys()))  # Randomly choose from all emojis

# Function to determine and display the winner (updated)
def determine_winner(player_choice, computer_choice):
    print(f"\nYou chose: {player_choice} {choices[player_choice]}")
    print(f"Computer chose: {computer_choice} {choices[computer_choice]}")

    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice, computer_choice) in [
        ("🪨", "✂️"), ("🪨", "🦎"),
        ("📄", "🪨"), ("📄", "🖖"),
        ("✂️", "📄"), ("✂️", "🦎"),
        ("🦎", "📄"), ("🦎", "🖖"),
        ("🖖", "🪨"), ("🖖", "✂️")
    ]:
        print("You win! 🎉")
    else:
        print("Computer wins! 🤖")

# Main game loop (updated)
while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break


# Main game loop
while True:  # Keep playing until user chooses to stop
    player_choice = get_player_choice()  # Get player's choice
    computer_choice = get_computer_choice()  # Get computer's choice
    determine_winner(player_choice, computer_choice)  # Determine and display winner

    play_again = input("Play again? (y/n): ").lower()  # Ask to play again
    if play_again != 'y':  # If not 'y', exit the loop and end the game
        break
