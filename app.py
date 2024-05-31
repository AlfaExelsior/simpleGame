import random  # Import for generating random choices
import emoji  # Import for displaying emojis

# Function to get and validate player's choice
def get_player_choice():
    while True:  # Loop until a valid choice is made
        print("Choose:")  # Display options
        print("1. 🪨 Rock")
        print("2. 📄 Paper")
        print("3. ✂️ Scissors")

        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:  # Check if choice is valid
            return int(choice)  # Convert choice to integer and return
        else:
            print("Invalid choice. Please try again.")  # Error message

# Function to generate computer's random choice
def get_computer_choice():
    return random.randint(1, 3)  # Randomly choose 1, 2, or 3

# Function to determine and display the winner
def determine_winner(player_choice, computer_choice):
    choices = ["🪨", "📄", "✂️"]  # Emojis for Rock, Paper, Scissors

    print(f"\nYou chose: {emoji.emojize(choices[player_choice - 1])}")  # Display player's choice with emoji
    print(f"Computer chose: {emoji.emojize(choices[computer_choice - 1])}")  # Display computer's choice with emoji

    # Determine the winner based on classic RPS rules
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        print("You win!")
    else:
        print("Computer wins!")

# Main game loop
while True:  # Keep playing until user chooses to stop
    player_choice = get_player_choice()  # Get player's choice
    computer_choice = get_computer_choice()  # Get computer's choice
    determine_winner(player_choice, computer_choice)  # Determine and display winner

    play_again = input("Play again? (y/n): ").lower()  # Ask to play again
    if play_again != 'y':  # If not 'y', exit the loop and end the game
        break
