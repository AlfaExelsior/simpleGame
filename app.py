import random
import emoji

# Expanded choices as a dictionary with corresponding emojis
choices = {
    "🪨": "Rock",
    "📄": "Paper",
    "✂️": "Scissors",
    "🦎": "Lizard",
    "🖖": "Spock"
}

# Function to get and validate player's choice (Corrected)
def get_player_choice():
    while True:
        print("Choose your champion:")
        for i, choice in enumerate(choices.keys()):  # Iterate directly over keys
            print(f"{i+1}. {choice} {choices[choice]}")  # Use choice as key to get name

        choice_input = input("Enter your choice (1-5): ")
        if choice_input.isdigit() and 1 <= int(choice_input) <= len(choices):
            return list(choices.keys())[int(choice_input) - 1]  # Return the chosen emoji
        else:
            print("Invalid choice. Please try again.")

# Function to generate computer's random choice
def get_computer_choice():
    return random.choice(list(choices.keys()))  

# Function to determine and display the winner (Unchanged)
def determine_winner(player_choice, computer_choice):
    # ... (rest of the function is the same)

# Main game loop (Unchanged)
while True:
    player_choice = get_player_choice()
    computer_choice = get_computer_choice()
    determine_winner(player_choice, computer_choice)

    play_again = input("Play again? (y/n): ").lower()
    if play_again != 'y':
        break

