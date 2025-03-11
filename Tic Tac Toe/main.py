# Main
# A demonstration of the MinimaxTicTacToeAgent.
# SANKETH KARUTURI

# Import necessary classes for game setup and execution
from tic_tac_toe_game import TicTacToeGame
from tic_tac_toe_board_renderer import TicTacToeBoardRenderer
from minimax_tic_tac_toe_agent import MinimaxTicTacToeAgent
from human_tic_tac_toe_agent import HumanTicTacToeAgent

# Initialize the Tic-Tac-Toe board renderer (used for displaying the game state)
renderer = TicTacToeBoardRenderer()

# Allow the user to choose their symbol
while True:
    user_symbol = input("Choose your symbol (X or O): ").upper()
    if user_symbol in ['X', 'O']:
        break
    print("Invalid choice. Please choose either X or O.")

# Assign AI symbol
ai_symbol = 'O' if user_symbol == 'X' else 'X'

# Create a new game with an empty board (represented as a tuple of None values)
game = TicTacToeGame((None, None, None, None, None, None, None, None, None), renderer)

# Set up human and AI players
human_agent = HumanTicTacToeAgent(game, user_symbol)
ai_agent = MinimaxTicTacToeAgent(game, ai_symbol)

# Display game instructions
print(f"You are {human_agent.symbol}, AI is {ai_agent.symbol}. Let's play!\n")
print("Board positions are indexed as follows:")
print("0 | 1 | 2\n3 | 4 | 5\n6 | 7 | 8\n")

# Determine who plays first
current_agent = human_agent if user_symbol == 'X' else ai_agent

# Main game loop: Continues until a player wins or the board is full (draw)
while game.is_not_over():
    print("----------------------------------------------")
    
    # Current player's move
    move = current_agent.action(game.state)
    game.state = game.result(game.state, move)  # Update game state
    print(game)  # Display updated board

    # Check for a winner
    if game.is_win(game.state, current_agent.symbol):
        print(f"{current_agent.symbol} wins! {'Congratulations!' if current_agent == human_agent else 'Better luck next time.'} 🎉")
        break
    if game.no_moves_left(game.state):  # Check for a draw
        print("It's a draw! 🤝")
        break

    # Switch turns
    current_agent = ai_agent if current_agent == human_agent else human_agent

# Game over message
print("Game Over. Thanks for playing!")
