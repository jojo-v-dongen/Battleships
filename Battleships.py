import random
from time import sleep

letters = ["A", "B", "C", "D", "E"]
grid = []
for i in range(1, 6):
    for x in range(1, 6):
        grid.append(letters[i - 1] + str(x))

computer_ship = random.choice(grid)

print("Computer has placed their ship on the grid!")
sleep(1)
while True:
    player_ship = str(input("What place in the grid is your ship?\n-->"))
    if player_ship in grid:
        break
    else:
        print("NOT A VALID GRID POSITION (A1, A5... ,E5")

game_finished = False
while game_finished == False:
    while True:
        player_guess = str(input("Guess a place on the grid: "))
        sleep(1)
        if player_guess in grid:
            break
        else:
            print("NOT A VALID GRID POSITION (A1, A5... ,E5")

    if player_guess == computer_ship:
        print(
            f"\n\nYOU WON!\n \nyour ship:{player_ship}\ncomputer ship: {computer_ship}"
        )
        game_finished = True
    else:
        print("MISS")
        computer_guess = random.choice(grid)
        sleep(1)
        print(f"Computer guessed {computer_guess}")
        sleep(1)
        if computer_guess == player_ship:
            print(
                f"\n\nCOMPUTER WON!\nyour ship: {player_ship}\ncomputer ship: {computer_ship}"
            )
            game_finished = True
        else:
            print("MISS")
