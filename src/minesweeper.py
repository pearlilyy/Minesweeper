import random

score = 0
random_box = []


def MinesweeperMap(n, j):
    grid = [[0 for row in range(n)] for column in range(n)]

    for num in range(j):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        if (x, y) in random_box:
            x = random.randint(0, n-1)
            y = random.randint(0, n-1)
        else:
            random_box.append((x, y))
        # print(random_box)
        grid[y][x] = '*'

        if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-1):
            if grid[y][x+1] != '*':
                grid[y][x+1] += 1  # center right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-1):
            if grid[y][x-1] != '*':
                grid[y][x-1] += 1  # center left
        if (x >= 1 and x <= n-1) and (y >= 1 and y <= n-1):
            if grid[y-1][x-1] != '*':
                grid[y-1][x-1] += 1  # top left

        if (x >= 0 and x <= n-2) and (y >= 1 and y <= n-1):
            if grid[y-1][x+1] != '*':
                grid[y-1][x+1] += 1  # top right
        if (x >= 0 and x <= n-1) and (y >= 1 and y <= n-1):
            if grid[y-1][x] != '*':
                grid[y-1][x] += 1  # top center

        if (x >= 0 and x <= n-2) and (y >= 0 and y <= n-2):
            if grid[y+1][x+1] != '*':
                grid[y+1][x+1] += 1  # bottom right
        if (x >= 1 and x <= n-1) and (y >= 0 and y <= n-2):
            if grid[y+1][x-1] != '*':
                grid[y+1][x-1] += 1  # bottom left
        if (x >= 0 and x <= n-1) and (y >= 0 and y <= n-2):
            if grid[y+1][x] != '*':
                grid[y+1][x] += 1  # bottom center
    return grid


def DisplayMap(map):
    for row in map:
        print("   ".join(str(cell) for cell in row))
        print("")


def FlagMap(n):
    grid = [['P' for row in range(n)] for column in range(n)]
    return grid


def HideMap(n):
    grid = [['-' for row in range(n)] for column in range(n)]
    return grid


mines = MinesweeperMap(10, 10)
play_map = HideMap(10)
flag_map = FlagMap(10)
while True:
    print("the number of mines is: 10\n")
    OpenOrFlag = input("1) Open a cell OR 2) Plant a flag: ")
    if OpenOrFlag == "1":
        print("\nSelect the cell you want to open")
        # if x_cell or y_cell is lower than 0 or grater than n, return and print warning
        x = int(input("Select the column(x = 1 to 10): "))-1
        y = int(input("Select the row(y = 1 to 10): "))-1

        if x > 9 or y > 9 or x < 0 or y < 0:
            print(f"\nSelect from 1 to 10 !!\n")
            continue

        if mines[y][x] == '*':
            print("\nYou Selected Mine! Game Over!!\n")
            DisplayMap(mines)
            break
        else:
            score += 1
            if score == 90:
                print("Congratulations!! You found all of the mines. You won the game!")
                DisplayMap(mines)
                break
            else:
                print("\nGood! You've got +1 point!")
                print(f"Your current score is: {score}\n")

            play_map[y][x] = mines[y][x]
            DisplayMap(play_map)

    elif OpenOrFlag == "2":
        print("\nSelect the cell you want to plant a flag")
        x = int(input("Select the column(x = 1 to 10: "))-1
        y = int(input("Select the row(y = 1 to 10: "))-1

        if x > 9 or y > 9 or x < 0 or y < 0:
            print("\nSelect from 1 to 10 !!\n")
            continue
        play_map[y][x] = flag_map[y][x]
        DisplayMap(play_map)

    else:
        print("Select 1 or 2 !")
        continue
