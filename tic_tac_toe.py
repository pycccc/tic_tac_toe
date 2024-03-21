row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]
counter = 0


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


def user_choice():
    user_input = input("Enter a number between 1-9 ")
    while (not user_input.isdigit() or int(user_input) > 9 or int(user_input) < 1):
        if not user_input.isdigit():
            print("Your answer is not valid")
        else:
            print("Your answer isn't within the range of 1-9")
        user_input = input("Enter a number between 1-9 ")
    return int(user_input)


def getCurrentSymbol():
    global counter
    symbol_list = ["X", "O"]
    counter += 1
    return symbol_list[counter % 2]


def updateTable(index):
    if index in range(1, 4):
        if row1[index - 1] != " ":
            print("it had already been updated")
            print("Choose another position")
        else:
            row1[index - 1] = getCurrentSymbol()
    elif index in range(4, 7):
        if row2[index - 4] != " ":
            print("it had already been updated")
            print("Choose another position")
        else:
            row2[index - 4] = getCurrentSymbol()
    else:
        if row3[index - 7] != " ":
            print("it had already been updated")
            print("Choose another position")
        else:
            row3[index - 7] = getCurrentSymbol()


def check():
    player1_win = False
    player2_win = False
    if row1[0] == row1[1] and row1[1] == row1[2] and (""not in row1):
        if row1[0] == "O":
            player1_win = True
        elif row1[0] == "X":
            player2_win = True
    elif row2[0] == row2[1] and row2[1] == row2[2] and (""not in row2):
        if row2[0] == "O":
            player1_win = True
        elif row2[0] == "X":
            player2_win = True
    elif row3[0] == row3[1] and row3[1] == row3[2] and (""not in row3):
        if row3[0] == "O":
            player1_win = True
        elif row3[0] == "X":
            player2_win = True
    elif row1[0] == row2[0] and row2[0] == row3[0] and (row1[0] != " ") and (row2[0] != " ") and (row3[0] != " "):
        if row1[0] == "O":
            player1_win = True
        elif row1[0] == "X":
            player2_win = True
    elif row1[1] == row2[1] and row2[1] == row3[1] and (row1[1] != " ") and (row2[1] != " ") and (row3[1] != " "):
        if row1[1] == "O":
            player1_win = True
        elif row1[1] == "X":
            player2_win = True
    elif row1[2] == row2[2] and row2[2] == row3[2] and (row1[2] != " ") and (row2[2] != " ") and (row3[2] != " "):
        if row1[2] == "O":
            player1_win = True
        elif row1[2] == "X":
            player2_win = True
    elif row1[0] == row2[1] and row2[1] == row3[2] and (row1[0] != " ") and (row2[1] != " ") and (row3[2] != " "):
        if row1[0] == "O":
            player1_win = True
        elif row1[0] == "X":
            player2_win = True
    elif row1[2] == row2[1] and row2[1] == row3[0] and (row1[2] != " ") and (row2[1] != " ") and (row3[0] != " "):
        if row1[2] == "O":
            player1_win = True
        elif row1[2] == "X":
            player2_win = True

    if player1_win:
        return "p1Win"
    elif player2_win:
        return "p2Win"
    else:
        return "no one win"


def play():
    while True:
        choice = user_choice()
        updateTable(choice)
        display(row1, row2, row3)
        result = check()
        if result == "p1Win":
            print("Player 1 wins the game")
            return
        elif result == "p2Win":
            print("Player 2 wins the game")
            return
        elif result == "no one win" and (" " not in row1) and (" " not in row2) and (" " not in row3):
            print("Tie Game")
            return


play()
