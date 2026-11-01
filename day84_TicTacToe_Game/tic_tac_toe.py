import time
import random


# ============================================================
# TIC TAC TOE - Text-based, two players (X and O)
# ============================================================

class TicTacToe:
    
    def __init__(self):
        self.board = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.game_mode = "1" # 1 for single player; 2 for multi-player
        self.ai_scores = 0
        self.human_o_score = 0
        
    def reset_game(self):
        self.board = [[" ", " ", " "],[" ", " ", " "], [" ", " ", " "]]
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
            # AI Player logic (Detects winning spot || blocks X || random spot)
            print("AI (Player O) is thinking...")
            move = self.ai_choose_move()
            time.sleep(2)
            row, col = move
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
        
        
    def find_winning_move(self, player):
        
        #Return (row, col) where `player` would win next move, or None.
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    self.board[row][col] = player            # 1. try the move
                    won = self.check_winner() == player      # 2. does it win?
                    self.board[row][col] = " "               # 3. undo it
                    if won:
                        return (row, col)
        return None

    def ai_choose_move(self):
        """Pick O's move by priority: win, block, or random."""
        
        # 1. Win if possible
        move = self.find_winning_move("O")
        if move is not None:
            return move

        # 2. Block X from winning
        move = self.find_winning_move("X")
        if move is not None:
            return move

        #3 Randomize the AI move 
        empty_cells = []

        for row in range(3):          # row numbers, not row lists
            for col in range(3):
                if self.board[row][col] == " ":
                    empty_cells.append((row, col))

        if empty_cells:               
            return random.choice(empty_cells)

            

        # # 3. Take the center
        # if self.board[1][1] == " ":
        #     return (1, 1)
        
        # # 4. Take a corner
        # for row, col in [(0, 0), (0, 2), (2, 0), (2, 2)]:
        #     if self.board[row][col] == " ":
        #         return (row, col)

        # # 5. Take whatever is left
        # for row in range(3):
        #     for col in range(3):
        #         if self.board[row][col] == " ":
        #             return (row, col)

        return None
        
        
    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
            
        return True
        
    def display_scores(self):
        
        print("\n=============== SCOREBOARD ===============\n")
        print(f"Player X: {self.scores['X']} | Player O: {self.scores['O']} | Draws: {self.scores['Draws']}\n")
        print("===========================================\n")
        
      
             
    def play_game(self):
        
        # 1. Print welcome message and place marker reference instructions
        self.welcome_msg()
        
        while True:
            self.reset_game()
            self.display_board()
        
            # 2. Start the playing the loop
            while True:
                result = self.place_marker()
                
                if result == False:
                    self.display_scores()
                    return
                
                winner = self.check_winner()
                if winner is not None:
                    print(f"The winner is {winner}! Congratulations\n")
                    self.scores[winner] += 1
                    break
                if self.is_board_full():
                    print("It's a draw\n")
                    self.scores["Draws"] += 1
                    break # end game
                
                self.current_player = "O" if self.current_player == "X" else "X"
                
            self.display_scores()
            
            while True:
                play_again = input("Play another match? (y/n): ").strip().lower()
                if play_again in ('y', 'n'):
                    break
                print("Invalid response. Please type 'y' for yes or 'n' for no. ")
                           
            if play_again == 'n':
                print("\nThanks for Playing!!\n")
                break
            if play_again == 'y':
                self.choose_next_mode()
                    
    def choose_next_mode(self):
        player_mode_text = "Single Player vs AI" if self.game_mode == "1" else "Multi-Player"
        
        while True:
            same_mode = input(f"Continue in the same {player_mode_text} mode? (y/n) ").strip().lower()
            if same_mode in ('y', 'n'):
                break
            print("Invalid response. Please type 'y' for yes or 'n' for no. ")
        
        if same_mode == 'y':
            print(f"\nContinuing on in {player_mode_text} mode...\n")
            time.sleep(1)
        else:
            self.game_mode = "2" if self.game_mode == "1" else "1"
            player_mode_text = "Single Player vs AI" if self.game_mode == "1" else "Multi-Player"
            print(f"\nSwitching to {player_mode_text} mode...\n")
            time.sleep(1)
        
        
        
        
        
        
        
        
       
        