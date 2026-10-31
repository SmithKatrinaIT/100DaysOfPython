class TicTacToe:
    
    def __init__(self):
        self .board = [
                [" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]
            ]
        self.current_player = "X"
        
    def display_board(self):
        print("\n")
    
        divider = "--+---+--"
        for i, row in enumerate(self.board):
            print(" | ".join(row))
            if i < len(self.board) -1:
                print(divider)
    
        print("\n")
        
        
    def print_board_ref(self):
        print("\n")
        print("   Tic Tac Toe ROW & COLUMN board Reference:\n")
        print("           Col 1:  Col 2:  Col 3:\n")
        print("   Row 1:   1,1  |  1,2  |  1,3")
        print("           ----------------------")
        print("   Row 2:   2,1  |  2,2  |  2,3")
        print("           ----------------------")
        print("   Row 3:   3,1  |  3,2  |  3,3")
        
        
    def welcome_msg(self):
        print("\n")
        print("================  Welcome to a Python game of Tic Tac Toe! ======================\n")
        print("Tic Tac Toe Instructions:\n")
        print("  1) Make your move based on the ROW & COLUMN BOARD Reference Board below:")
        print("  2) Type 'help' to display the Reference Board at any time.")
        print("  3) Type 'exit' to exit the game at any time.")
        print("=================================================================================")  
          
        
    def get_move(self):
        while True:
        
            try:
                user_input = input(f"Player {self.current_player} - Please enter your 'row' and 'column' number from the board: ")
            
                if user_input.strip().lower() == 'help':
                    self.print_board_ref()
                    continue
                
                if user_input.strip().lower() == 'exit':
                    print("\nThank you for playing!!")
                    return "exit"
                
                else:
                    row_str, col_str, *_ = user_input.replace(",", " ").split()
                    row = int(row_str) 
                    col = int(col_str)   
                    
                    # Validate numbers are in range 1-3; if not, print a message and ask
                    if row not in (1,2,3) or col not in (1,2,3):
                        print("\nInvalid Input.  Row and/or Column number must be between 1 - 3.")
                        continue
                    
                    else:
                        # Convert 1-based row/column to 0-based indexes by subtracting 1.
                        row_i = row - 1
                        col_i = col - 1
                        
                        #Check the chosen cell is still blank (== " "). If taken, tell theplayer and ask again.
                        if self.board[row_i][col_i] == " ":
                            return  {"row":row_i, "col": col_i}
                        else:
                            print("\nThat space is already taken. Please Try again. \n")
                            continue
                
            except ValueError:
                print("Invalid Input.  Try again! Enter at least 2 values -  numbers only.")
                
                
    def place_marker(self):
        move = self.get_move() 
    
        if isinstance(move, dict):
            self.board[move['row']][move['col']] = self.current_player
            self.display_board()
            return True
            
        elif isinstance(move, str) and move.lower() == 'exit':
            return False
        
        
    def check_winner(self):
        if self.board[0][0] != " " and self.board[0][0] == self.board[0][1] == self.board[0][2]: # top row
            return self.board[0][0]
        elif self.board[1][0] != " " and self.board[1][0] == self.board[1][1] == self.board[1][2]: # middle row
            return self.board[1][0]
        elif self.board[2][0] != " " and self.board[2][0] == self.board[2][1] == self.board[2][2]: # bottom row
            return self.board[2][0]
        elif self.board[0][0] != " " and self.board[0][0] == self.board[1][0] == self.board[2][0]: # 1st column
            return self.board[0][0]
        elif self.board[0][1] != " " and self.board[0][1] == self.board[1][1] == self.board[2][1]: # 2nd column
            return self.board[0][1]
        elif self.board[0][2] != " " and self.board[0][2] == self.board[1][2] == self.board[2][2]: # 3rd column
            return self.board[0][2]
        elif self.board[0][0] != " " and self.board[0][0] == self.board[1][1] == self.board[2][2]: # diagonal right
            return self.board[0][0]
        elif self.board[0][2] != " " and self.board[0][2] == self.board[1][1] == self.board[2][0]: # diagonal left
            return self.board[0][2]
        else:
            return None
        
        
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
            
        return True
        
             
    def play_game(self):
        
        # 1. Print welcome message and place marker reference instructions
        self.welcome_msg()
        self.print_board_ref()
        
        # 2. Start the playing the loop
        while True:
            result = self.place_marker()
            
            if result == False:
                break
            
            winner = self.check_winner()
            if winner is not None:
                print(f"The winner is {winner}! Congratulations")
                break
            if self.is_board_full():
                print("It's a draw")
                break # end game
            
            self.current_player = "O" if self.current_player == "X" else "X"
        
        
        
        
        
        
        
       
        