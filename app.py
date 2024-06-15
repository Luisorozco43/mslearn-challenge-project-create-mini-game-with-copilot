import random

def main():


    counter = 0
    player1wins = 0
    player2wins = 0
    while counter < 5:
        
        player1 = ""
        player2 = ""

        while player1 not in ["rock", "paper", "scissors"]:
            player1 = input("Player 1, enter rock, paper, or scissors: ")

        player2 = random.choice(["rock", "paper", "scissors"])
        print(f"Player 2: {player2}")

        result = rock_paper_scissors(player1, player2)
        if result == "Player 1 wins!":
            player1wins += 1
        else:
            player2wins += 1
        
        counter += 1

    if player1wins > player2wins:
        print("Player 1 wins the game!")
    elif player1wins == player2wins:
        print("It's a tie!")
    else:
        print("Player 1 loose the game!")

def rock_paper_scissors(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif player1 == "rock":
        if player2 == "scissors":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == "scissors":
        if player2 == "paper":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    elif player1 == "paper":
        if player2 == "rock":
            return "Player 1 wins!"
        else:
            return "Player 2 wins!"
    else:
        return "Invalid input"


if __name__ == "__main__":
    main()