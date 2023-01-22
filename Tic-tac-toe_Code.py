'''
Author: Michael Powell
Narrative:
    This program allows the user to play Tic-Tac-Toe in four different modes.

@author: mpowell23@gcds.net
'''

# Import Box
import random                                                                                       

def player_marker_selection(taken_positions, type_player):
    '''
        Summary:
        This function asks the user for the row and column they want to place their marker.
        
        Parameters:
        Taken_positions (list): A list of board positions that the markers have taken.
        
        Returns:
        Row_column (list): A list of two elements containing the row and column the user has selected.
    '''
    
    # Asking the player for their selections
    while True :
        # Row selection 
        while True :
            row = input(type_player + ', please select the row you want to place your marker.\n')
            row = row.strip()
            
            # Ensuring proper conditions for the row selection
            try :
                row = int(row)                                                                              # Turn the row position into an integer
                
                if row < 0 or row > 2:                                                                      # Continue the loop if the row selection does not equal 0, 1, or 2
                    print('Please insert a row value between 0 to 2.')
                    continue
                
                else:
                    break
            
            except :                                                                                        # Continue the loop if the row selection is not an integer
                print('Please insert a row value between 0 to 2.')
                continue 
    
        # Column selection
        while True :
            column = input(type_player + ', please select the column you want to place your marker.\n')
            column = column.strip()
            
            # Ensuring proper conditions for the column selection
            try :
                column = int(column)                                                                        # Turn the column position into an integer
                
                if column < 0 or column > 2 :                                                               # Continue the loop if the column selection does not equal 0, 1, or 2
                    print('Please insert a column value between 0 to 2.')
                    continue
                
                else :
                    break
            
            except:                                                                                         # Continue the loop if the column selection is not an integer
                print('Please insert a column value between 0 to 2.')
                continue
        
        # Ensuring the position inputed is not already taken
        if (row, column) in taken_positions :
            print('Please insert a position that has not been taken already.')
            continue
        
        else :
            break
    
    row_column = [row, column]
    return row_column


def computer_marker_selection(taken_positions):
    '''
        Summary and Description of Function:
        This function randomizes the row and column where the computer places their marker.
        
        Parameters:
        Taken_positions (list): A list of board positions that the markers have taken.
        
        Returns:
        Row_column (list): A list of two elements containing the row and column the user has selected.
    '''
    
    while True :
        row = random.randint(0,2)                                                                           # The row = the random import to randomize an integer from 0 to 2
        column = random.randint(0,2)                                                                        # The column = the random import to randomize an integer from 0 to 2
        
        if (row, column) in taken_positions :                                                               # If the row and the column are in taken_positions, repeat the loop
            continue
        
        else :                                                                                              # Else, break the loop
            break
        
    row_column = [row, column]                                                                              # Return the row_column of the computer
    return row_column


def win_determination(board, marker):
    '''
        Summary and Description of Function:
        This function determines if a marker has won the game by taking three positions in a row.
        
        Parameters:
        Board (2-D array): The Tic-Tac-Toe board.
        Marker (string): The marker 
        
        Returns:
        Row_column (list): A list of two elements containing the row and column the user has selected.
    '''
    
    if board[0][0] == marker and board[0][1] == marker and board[0][2] == marker :
        win = marker
        
    elif board[1][0] == marker and board[1][1] == marker and board[1][2] == marker :
        win = marker
    
    elif board[2][0] == marker and board[2][1] == marker and board[2][2] == marker :
        win = marker
    
    elif board[0][0] == marker and board[1][0] == marker and board[2][0] == marker :
        win = marker
    
    elif board[0][1] == marker and board[1][1] == marker and board[2][1] == marker :
        win = marker
    
    elif board[0][2] == marker and board[1][2] == marker and board[2][2] == marker :
        win = marker
    
    elif board[0][0] == marker and board[1][1] == marker and board[2][2] == marker :
        win = marker
    
    elif board[2][0] == marker and board[1][1] == marker and board[0][2] == marker :
        win = marker
    
    else :
        win = 0
    
    return win


def gameboard(board):
    '''
        Summary and Description of Function:
        This function prints the board as it is updated.
        
        Parameters:
        Board (2-D array): The Tic-Tac-Toe board.
        
        Returns:
        Printed board.
    '''
    
    print('The current board is as follows:')
    for row in board :
        print(row)
    

def main():
    # Game Description
    board_print = [['0', '1', '2'],
                   ['-', '-', '-', '0'],                                                                    # The board represented by a 2-D array for printing purposes
                   ['-', '-', '-', '1'],
                   ['-', '-', '-', '2']]
    print('This program allows the user to play Tic-Tac-Toe in four modes from the following board.')
    gameboard(board_print)
    
    
    play_again = 'yes'                                                                                      # Set play_again = yes
    while play_again == 'yes' :                                                                             # Run the program when play_again = yes
        # Asking the user want mode they want to play
        while True :
            mode = input('What mode do you want to play (X vs O)?\n(1) Player vs Computer\n(2) Computer vs Player\n(3) Computer vs Computer\n(4) Player vs Player\n')
            mode = mode.lower()                                                                             # Make all the letters lower case 
            
            if mode == 'player vs computer' or mode == 'computer vs player' or mode == 'computer vs computer' or mode == 'player vs player' or mode == '1' or mode == '2' or mode == '3' or mode == '4':                            
                break
            
            else :
                print('Please insert a mode from the listed options.')                                      # Re-run the loop when they do not insert a given option
                continue
        
        
        # Defining the game's variables
        taken_positions = []                                                                                # A list that appends the taken positions by the markers after each move
        win = 0                                                                                             # A variable that determines when a marker has won
        move_counter = 0                                                                                    # A variable that counts the number of moves                             
        board = [['-', '-', '-'],                                                                           # The board represented by a 2-D array
                 ['-', '-', '-'],
                 ['-', '-', '-']]
        
        
        # Running the game
        while win == 0 :
            # Mode: Player vs Computer 
            if mode == 'player vs computer' or mode == '1' :
                # Player Marker Selection
                type_player = 'Player'
                row_column_X = player_marker_selection(taken_positions, type_player)
                
                # X's Turn
                taken_positions.append((row_column_X[0], row_column_X[1]))
                board[row_column_X[0]][row_column_X[1]] = 'X'
                gameboard(board)
                
                # Win Determination X
                marker = 'X'
                win = win_determination(board, marker)
                if win == 'X' :
                    print('The player has won the game with three spaces in a row as X.')
                    break 
                
                # Tie Determination
                move_counter = move_counter + 1
                if move_counter == 5 :
                    print('The player and the computer have tied.')
                    win = 'Tie'
                    break

                # Computer Marker Selection
                row_column_O = computer_marker_selection(taken_positions)
                
                # Turn O
                taken_positions.append((row_column_O[0], row_column_O[1]))
                board[row_column_O[0]][row_column_O[1]] = 'O'
                gameboard(board)
                
                
                # Win Determination O
                marker = 'O'
                win = win_determination(board, marker)
                if win == 'O' :
                    print('The computer has won the game with three spaces in a row as O.')
                    break
            
            
            elif mode == 'computer vs player' or mode == '2' :
                # Computer Marker Selection
                row_column_X = computer_marker_selection(taken_positions)
                
                # X's Turn
                taken_positions.append((row_column_X[0], row_column_X[1]))
                board[row_column_X[0]][row_column_X[1]] = 'X'
                gameboard(board)
                
                # Win Determination X
                marker = 'X'
                win = win_determination(board, marker)
                if win == 'X' :
                    print('The computer has won the game with three spaces in a row as X.')
                    break 
                
                # Tie Determination
                move_counter = move_counter + 1
                if move_counter == 5 :
                    print('The player and the computer have tied.')
                    win = 'Tie'
                    break
                
                # Player Marker Selection
                type_player = 'Player'
                row_column_O = player_marker_selection(taken_positions, type_player)
                
                # Turn O
                taken_positions.append((row_column_O[0], row_column_O[1]))
                board[row_column_O[0]][row_column_O[1]] = 'O'
                gameboard(board)
                
                # Win Determination O
                marker = 'O'
                win = win_determination(board, marker)
                if win == 'O' :
                    print('The player has won the game with three spaces in a row as O.')
                    break
            
            
            # Mode: Computer vs Computer
            elif mode == 'computer vs computer' or mode == '3' :
                # Computer 1 Marker Selection
                row_column_X = computer_marker_selection(taken_positions)
                
                # X's Turn
                taken_positions.append((row_column_X[0], row_column_X[1]))
                board[row_column_X[0]][row_column_X[1]] = 'X'
                gameboard(board)
                
                # Win Determination X
                marker = 'X'
                win = win_determination(board, marker)
                if win == 'X' :
                    print('The first computer has won the game with three spaces in a row as X.')
                    break 
                
                # Tie Determination
                move_counter = move_counter + 1
                if move_counter == 5 :
                    print('The computers have tied.')
                    win = 'Tie'
                    break
                
                # Computer 2 Marker Selection
                row_column_O = computer_marker_selection(taken_positions)
                
                # Turn O
                taken_positions.append((row_column_O[0], row_column_O[1]))
                board[row_column_O[0]][row_column_O[1]] = 'O'
                gameboard(board)
                
                # Win Determination O
                marker = 'O'
                win = win_determination(board, marker)
                if win == 'O' :
                    print('The second computer has won the game with three spaces in a row as O.')
                    break
            
            
            # Mode: Player vs Player
            else :
                # Player 1 Marker Selection
                type_player = 'Player #1'
                row_column_X = player_marker_selection(taken_positions, type_player)
                
                # X's Turn
                taken_positions.append((row_column_X[0], row_column_X[1]))
                board[row_column_X[0]][row_column_X[1]] = 'X'
                gameboard(board)
                
                # Win Determination X
                marker = 'X'
                win = win_determination(board, marker)
                if win == 'X' :
                    print('The first player has won the game with three spaces in a row as X.')
                    break 
                
                # Tie Determination
                move_counter = move_counter + 1
                if move_counter == 5 :
                    print('The players have tied.')
                    win = 'Tie'
                    break
                
                # Player 2 Marker Selection
                type_player = 'Player #2'
                row_column_O = player_marker_selection(taken_positions, type_player)
                
                # Turn O
                taken_positions.append((row_column_O[0], row_column_O[1]))
                board[row_column_O[0]][row_column_O[1]] = 'O'
                gameboard(board)
                
                # Win Determination O
                marker = 'O'
                win = win_determination(board, marker)
                if win == 'O' :
                    print('The second player has won the game with three spaces in a row as O.')
                    break


        # Play Again Option
        while True :
            play_again = input('Do you want to use the program again?\n')
            play_again = play_again.lower()
            if play_again == 'yes' :
                print('The program will restart.')
                break
            elif play_again == 'no' :
                print('The program has ended.')
                break
            else :
                print('Please insert a yes or no answer.')

      
if __name__ == '__main__':
    main()