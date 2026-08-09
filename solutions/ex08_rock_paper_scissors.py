"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:
Rock beats scissors
Scissors beats paper
Paper beats rock

"""

def game(player1,player2):
    print("Choose rock,scissors or paper.")
    score1 = 0
    score2 = 0
    while(True):
        move1 = input("Choose your move: ")
        move2 = input("Choose your move: ")
        
        if move1 == "rock":
            if move2 == "paper":
                print(f"{player2} won this match!")
                score2+=1
            if move2 == "rock":
                print("It is draw")

            if move2 == "scissors":
                print(f"{player1} won this match!")
                score1+=1
        if move1 == "paper":
            if move2 == "scissors":
                print(f"{player2} won this match!")
                score2+=1
        
            if move2 == "paper":
                print("It is draw")
        
            if move2 == "rock":
                print(f"{player1} won this match!")
                score1+=1

        if move1 == "scissors":
            if move2 == "rock":
                print(f"{player2} won this match!")
                score2+=1

            if move2 == "scissors":
                print("It is draw")
        
            if move2 == "paper":
                print(f"{player1} won this match!")
                score1+=1
        print(f"{player1} score:{score1} | {player2} score:{score2}")

        next_match = input("Do you wanna continue? Input yes or no: ")
        if next_match == "no":
            break

game("Emre", "Ayse")