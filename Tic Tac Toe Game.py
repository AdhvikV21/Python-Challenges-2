TheBoard = {'7': ' ', '8':' ', '9':' ', '4':' ', '5':' ', '6':' ', '1':' ', '2':' ', '3': ' ' }

board_keys = []

for key in TheBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')

def game():

    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(TheBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if TheBoard[move] == '':
            TheBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue
    
        if count >= 5:
            if TheBoard['7'] == TheBoard['8'] == TheBoard['9'] != '':          
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['4'] == TheBoard['5'] == TheBoard['6'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['1'] == TheBoard['2'] == TheBoard['3'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['1'] == TheBoard['4'] == TheBoard['7'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['2'] == TheBoard['5'] == TheBoard['8'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['3'] == TheBoard['6'] == TheBoard['9'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break          
            elif TheBoard['7'] == TheBoard['5'] == TheBoard['3'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break
            elif TheBoard['1'] == TheBoard['5'] == TheBoard['9'] != '':
                printBoard(TheBoard)
                print("\nGame Over.\n")
                print("****" +turn + " won,****")
                break

            if count == 9:
                print("\nGame Over.\n")
                print("It's a Tie!!")

            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            
            for key in board_keys:
                TheBoard[key] =" "
            
            game()

if __name__ == "__main__":
    game()