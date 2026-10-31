import time


# ============================================================
# TIC TAC TOE - Text-based, two players (X and O)
# ============================================================

class TicTacToe:
    
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.game_mode = "1" # 1 for single player; 2 for multi-player
        
    def reset_game(self):
        self.board = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
        self.current_player = "X"
        self.game_mode = "1"
        
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
        print("  Tic Tac Toe ROW & COLUMN board Reference:\n")
        print("          Col 1:  Col 2:  Col 3:\n")
        print("  Row 1:   1,1  |  1,2  |  1,3")
        print("          ----------------------")
        print("  Row 2:   2,1  |  2,2  |  2,3")
        print("          ----------------------")
        print("  Row 3:   3,1  |  3,2  |  3,3")
        
        
    def welcome_msg(self):
        print("\n")
        print("================  Welcome to a Python game of Tic Tac Toe! ======================\n")
        
        self.game_mode = input("Select Mode: 1) Single Player vs AI  or  2) Multi-player: ").strip()
        if self.game_mode not in ("1", "2"):
            self.game_mode = "1"
            print("Defaulting to Single Player vs AI.\n")
        
        print("\nTic Tac Toe Instructions:")
        print("  1) Make your move based on the ROW & COLUMN BOARD Reference Board below:")
        print("  2) Type 'help' to display the Reference Board at any time.")
        print("  3) Type 'exit' to exit the game at any time.")
        self.print_board_ref()
        print("=================================================================================")  
          
        
    def get_move(self):
        if self.game_mode == "1" and self.current_player == "O":
            # AI Player logic (Basic AI picking first available empty spot)
            print("AI (Player O) is thinking...")
            time.sleep(2)

            for row in range(3):
                for col in range(3):
                    if self.board[row][col] == " ":
                        return {"row": row, "col": col}
        
        
        while True:
        
            try:
                user_input = input(f"Player {self.current_player} - Enter 'row' and 'column' number (or 'help', 'exit'): ")
            
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
        
    def display_scores(self):
        
        print("\n=============== SCOREBOARD ===============\n")
        print(f"Player X: {self.scores['X']} | Player O (AI): {self.scores['O']} | Draws: {self.scores['Draws']}\n")
        print("===========================================\n")
        
        #print(f"=========== SCOREBOARD ===========\nPlayer X: {self.scores['X']} | Player O (AI): {self.scores['O']} | Draws: {self.scores['Draws']}\n==========================")
             
    def play_game(self):
        
        # 1. Print welcome message and place marker reference instructions
        while True:
            self.welcome_msg()
            self.display_board()
        
            # 2. Start the playing the loop
            while True:
                result = self.place_marker()
                
                if result == False:
                    break
                
                winner = self.check_winner()
                if winner is not None:
                    print(f"The winner is {winner}! Congratulations\n")
                    self.scores[winner] += 1
                    break
                if self.is_board_full():
                    print("It's a draw")
                    self.scores["Draws"] += 1
                    break # end game
                
                self.current_player = "O" if self.current_player == "X" else "X"
                
            self.display_scores()
            
            play_again = input("Play another match? (y/n): ").strip().lower()
            
            if play_again != 'y':
                print("\nFinal Scores: \n")
                self.display_scores()
                break

# --- Execution ---
if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
    