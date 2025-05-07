import sys

def create_empty_board():
    """Create a 9x9 empty Sudoku board"""
    return [[0 for _ in range(9)] for _ in range(9)]

def print_board(board):
    """Print the Sudoku board with borders and separators"""
    print("\n   " + " ".join([str(i) for i in range(1, 10)]))
    print("  " + "-" * 19)
    for i in range(9):
        row = [str(x) if x != 0 else "." for x in board[i]]
        print(f"{i+1} |" + " ".join(row) + "|")
        if (i + 1) % 3 == 0 and i != 8:
            print("  " + "-" * 19)
    print("  " + "-" * 19)

def is_valid_move(board, row, col, num):
    """Check if placing 'num' at (row, col) is valid"""
    # Check row
    if num in board[row]:
        return False
    
    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False
    
    # Check 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def is_board_full(board):
    """Check if the board is completely filled"""
    for row in board:
        if 0 in row:
            return False
    return True

def play_sudoku():
    """Main game loop for Sudoku"""
    board = create_empty_board()
    current_player = 1
    
    print("Welcome to Terminal Sudoku for 2 Players!")
    print("Players take turns entering numbers (1-9) into the grid.")
    print("Enter row (1-9), column (1-9), and number (1-9) separated by spaces.")
    print("Enter 'q' at any time to quit the game.\n")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        
        try:
            user_input = input("Enter row, column, number (e.g., '3 5 7'): ").strip()
            
            if user_input.lower() == 'q':
                print("\nGame ended by player. Goodbye!")
                sys.exit(0)
                
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please enter 3 numbers separated by spaces.")
                continue
                
            row, col, num = map(int, parts)
            
            # Validate input ranges
            if not (1 <= row <= 9) or not (1 <= col <= 9) or not (1 <= num <= 9):
                print("All numbers must be between 1 and 9.")
                continue
                
            # Convert to 0-based index
            row -= 1
            col -= 1
            
            # Check if cell is empty
            if board[row][col] != 0:
                print("That cell is already filled. Choose another.")
                continue
                
            # Check if move is valid
            if not is_valid_move(board, row, col, num):
                print(f"Invalid move! {num} cannot be placed there.")
                continue
                
            # Make the move
            board[row][col] = num
            
            # Check if board is full
            if is_board_full(board):
                print_board(board)
                print(f"Player {current_player} has completed the Sudoku! Congratulations!")
                break
                
            # Switch players
            current_player = 2 if current_player == 1 else 1
            
        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except KeyboardInterrupt:
            print("\nGame ended by user. Goodbye!")
            sys.exit(0)

if __name__ == "__main__":
    play_sudoku()