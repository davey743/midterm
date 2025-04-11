def create_board():
    return [["" for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, player):
    if board[row][col] == "":
        board[row][col] = player
        return True
    return False

def check_winner(board):
    # Rows & Columns
    for i in range(3):
        if board[i][0] != "" and all(cell == board[i][0] for cell in board[i]):
            return board[i][0]
        if board[0][i] != "" and all(board[j][i] == board[0][i] for j in range(3)):
            return board[0][i]
    
    # Diagonals
    if board[0][0] != "" and all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]
    if board[0][2] != "" and all(board[i][2-i] == board[0][2] for i in range(3)):
        return board[0][2]
    
    if all(cell != "" for row in board for cell in row):
        return "Tie"

    return None
