import random

def check_winner(player, board):
 
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def computer_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    return random.choice(empty_cells)

def display_board(board):
    for row in board:
        print(row)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("You are playing as 'x'")
    while True:
        display_board(board)
        print("Player's Move")
        row = int(input("Enter the row: "))
        col = int(input("Enter the column: "))
        
        if board[row][col] == ' ':
            board[row][col] = 'x'

            if check_winner('x', board):
                display_board(board)
                print("You Have Won!!")
                break

            elif all(cell != ' ' for row in board for cell in row):
                display_board(board)
                print("It's a Draw!")
                break

            print("Computer's Move")
            row, col = computer_move(board)
            board[row][col] = 'o'

            if check_winner('o', board):
                display_board(board)
                print("Computer has Won!!")
                break

            elif all(cell != ' ' for row in board for cell in row):
                display_board(board)
                print("It's a Draw!")
                break
        else:
            print("Enter correct choice")

if __name__ == '__main__':
    main()
