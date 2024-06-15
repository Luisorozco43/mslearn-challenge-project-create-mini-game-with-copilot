
def main():

    player1 = ""
    player2 = ""

    while player1 not in ["rock", "paper", "scissors"]:
        player1 = input("Player 1, enter rock, paper, or scissors: ")

    while player2 not in ["rock", "paper", "scissors"]:
        player2 = input("Player 2, enter rock, paper, or scissors: ")
        
    result = rock_paper_scissors(player1, player2)
    print(result)


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