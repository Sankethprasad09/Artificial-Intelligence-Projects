# MinimaxTicTacToeAgent
# A game-playing tic tac toe agent that uses the minimax algorithm to produce
# a rational action.
# SANKETH KARUTURI

class MinimaxTicTacToeAgent:
    """
    A Tic-Tac-Toe agent that plays optimally using the minimax algorithm.
    It always considers itself the maximizing player, regardless of the symbol ('X' or 'O').
    """

    def __init__(self, game, symbol):
        """
        Initializes the Minimax agent with a game instance and a symbol.
        
        Parameters:
        - game: The Tic-Tac-Toe game instance.
        - symbol: The player's symbol ('X' or 'O').
        """
        self.game = game
        self.symbol = symbol

    def action(self, state):
        """
        Determines the best move for the current state using the minimax algorithm.
        
        Parameters:
        - state: The current board state as a tuple.

        Returns:
        - The best move (an integer representing a board position) or None if no valid moves.
        """
        if self.game is None:
            return 0  # Default move for testing when no game instance is provided.

        available_moves = self.game.actions(state)
        if not available_moves:  # If no moves are available, return None
            return None
        
        _, best_move = self.minimax(state)
        return best_move if best_move is not None else None  # Explicitly handle no valid moves

    def minimax(self, state):
        """
        Implements the minimax algorithm to determine the best possible move.
        The agent always considers itself the maximizing player, regardless of the symbol.
        
        Parameters:
        - state: The current board state.

        Returns:
        - A tuple containing:
            - The best score (utility value).
            - The best move (position on the board).
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol), None  # Directly return utility

        maximizing = (self.game.to_move(state) == self.symbol)  # Always maximize when it's our turn
        
        if maximizing:
            return self.max_value(state)
        else:
            return self.min_value(state)

    def max_value(self, state):
        """
        Returns the maximum utility value for the agent when it is its turn to play.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol), None  # Immediate return

        v = float('-inf')
        best_move = None

        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v2, _ = self.min_value(next_state) 
            if v2 > v:
                v, best_move = v2, move

        return v, best_move

    def min_value(self, state):
        """
        Returns the minimum utility value for the opponent when it is their turn to play.
        """
        if self.game.is_terminal(state):
            return self.game.utility(state, self.symbol), None  # Immediate return

        v = float('inf')
        best_move = None

        for move in self.game.actions(state):
            next_state = self.game.result(state, move)
            v2, _ = self.max_value(next_state)  
            if v2 < v:
                v, best_move = v2, move

        return v, best_move
