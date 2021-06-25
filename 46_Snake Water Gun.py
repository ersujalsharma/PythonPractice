import random
game_tools = ["snake","water","gun"]
chance = 10
player_win = 0
computer_win = 0
while(chance>0):
    chance = chance-1
    players_choice = input(f"Choose any One in {game_tools}")
    computers_choice = random.choice(game_tools)
    print(f"Computer Chooses {computers_choice}")
    if players_choice == "snake" and computers_choice == "water" :
        print(f"You Win Now YOu have {chance} chances")
        player_win=player_win+1
    elif players_choice == "water" and computers_choice == "gun" :
        print(f"You Win Now YOu have {chance} chances")
        player_win=player_win+1
    elif players_choice == "gun" and computers_choice == "snake" :
        print(f"You Win Now YOu have {chance} chances")
        player_win=player_win+1
    else:
        print(f"Sorry: You Lost! Now YOu have {chance} chances")
        computer_win=computer_win+1
print(f"You win {player_win} and Computer win {computer_win} time")
if player_win >computer_win:
    print("You Won The Game")
else:
    print("Computer Won the Game")
