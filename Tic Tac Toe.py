my_dict = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8"}

def tablePrint():
    print()
    print(my_dict[0], "\t|\t", my_dict[1], "\t|\t", my_dict[2])
    print("------------------")
    print(my_dict[3], "\t|\t", my_dict[4], "\t|\t", my_dict[5])
    print("------------------")
    print(my_dict[6], "\t|\t", my_dict[7], "\t|\t", my_dict[8])
    print("------------------")
    print()


def game():
    player_1 = input("Enter player 1 name (X): ")
    player_2 = input("Enter player 2 name (O): ")
    count = 0
    count2 = 0

    while True:
        tablePrint()

        p1 = int(input("Enter X at any position: "))
        if p1 in my_dict.keys():
            my_dict[p1] = "X"
            count += 1
            tablePrint()
            if my_dict[0] == my_dict[1] == my_dict[2] == "X" or my_dict[3] == my_dict[4] == my_dict[5] == "X" \
                    or my_dict[6] == my_dict[7] == my_dict[8] == "X" or my_dict[0] == my_dict[3] == my_dict[6] == "X" \
                    or my_dict[1] == my_dict[4] == my_dict[7] == "X" or my_dict[2] == my_dict[5] == my_dict[8] == "X" \
                    or my_dict[0] == my_dict[4] == my_dict[8] == "X" or my_dict[6] == my_dict[4] == my_dict[2] == "X":
                print("<---------------------------- Player ", player_1, " Win ------------------------------>")
                break

        p2 = int(input("Enter O at any position: "))
        if p2 in my_dict.keys():
            my_dict[p2] = "O"
            count2 += 1
            if my_dict[0] == my_dict[1] == my_dict[2] == "O" or my_dict[3] == my_dict[4] == my_dict[5] == "O" \
                    or my_dict[6] == my_dict[7] == my_dict[8] == "O" or my_dict[0] == my_dict[3] == my_dict[6] == "O" \
                    or my_dict[1] == my_dict[4] == my_dict[7] == "O" or my_dict[2] == my_dict[5] == my_dict[8] == "O" \
                    or my_dict[0] == my_dict[4] == my_dict[8] == "O" or my_dict[6] == my_dict[4] == my_dict[2] == "O":
                tablePrint()
                print("<---------------------------- Player ", player_2, " Win ------------------------------>")
                break

        if count >= 4 or count2 >= 4:
            print()
            print("<-------------------------------- GAME TIED BETWEEN Player ", player_1, " and ", player_2,
                  "-------------------------------------->")
            break

game()

print()
print("Game Over! Thanks For Playing")
