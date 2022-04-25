def print_board(board):
    row_number = 8
    print("  ", end="")
    print(" ----"*8)
    for row in board:
        print(row_number, end=" ")
        row_number -= 1
        for cell in row:
            print("| {} ".format(cell), end="")
        print("|")
        print("  ", end="")
        print(" ----"*8)
    print("  ", end="")
    for letter in ['a','b','c','d','e','f','g','h']:
        print("  {}  ".format(letter), end="")
    print("")

board = [["  "]*8]*8
board[0] = ["BR","BN","BB","BQ","BK","BB","BN","BR"]
board[1] = ["BP","BP","BP","BP","BP","BP","BP","BP"]
board[6] = ["BP","BP","BP","BP","BP","BP","BP","BP"]
board[7] = ["BR","BN","BB","BQ","BK","BB","BN","BR"]

print_board(board)