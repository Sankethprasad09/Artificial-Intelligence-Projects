# TicTacToeGame
# A formal representation of a game of Tic Tac Toe, aligned with the specification
# from the AIMA text. The Game encapsulates the state, transition model,
# objective function, and other game mechanics.
# It uses a TicTacToeBoardRenderer to 'draw' itself when necessary.
# SANKETH KARUTURI

class IllegalTicTacToeMoveException(Exception):
    pass

class TicTacToeGame:

    P1_SYMBOL = 'X'
    P2_SYMBOL = 'O'

    def __init__(self, initial_state, renderer):
        self.state = initial_state
        self.renderer = renderer

    def utility(self, state, player):
        """
        Returns the utility value of a game state:
        - 1 if `player` wins.
        - -1 if the opponent wins.
        - 0 for a draw.
        """
        if self.is_win(state, player):
            return 1
        elif self.is_win(state, self.P2_SYMBOL if player == self.P1_SYMBOL else self.P1_SYMBOL):
            return -1
        return 0

    def is_not_over(self):
        """
        Returns True if the game is not over.
        """
        return not self.is_terminal(self.state)

    def is_terminal(self, state):
        """
        A state is terminal if no moves are left (win or draw).
        """
        return self.no_moves_left(state)

    def to_move(self, state):
        """
        Returns which player's turn it is.
        """
        if self.no_moves_left(state):
            return None
        return self.P1_SYMBOL if state.count(self.P1_SYMBOL) == state.count(self.P2_SYMBOL) else self.P2_SYMBOL

    def actions(self, state):
        """
        Returns a tuple of available actions (empty board positions).
        """
        return tuple(i for i in range(len(state)) if state[i] is None)

    def result(self, state, action):
        """
        Returns the new state after applying `action` to `state`.
        """
        if state[action] is not None:
            raise IllegalTicTacToeMoveException(f"Illegal move: {action} on state {state}.")
        
        new_state = list(state)
        new_state[action] = self.to_move(state)
        return tuple(new_state)

    def no_moves_left(self, state):
        """
        Returns True if no moves are left or a player has won.
        """
        return None not in state or self.is_win(state, self.P1_SYMBOL) or self.is_win(state, self.P2_SYMBOL)

    def is_win(self, state, player):
        """
        Is the `state` a winning state for `player` ?
        """
        if [0, 1, 2] == [i for i in [0, 1, 2] if state[i] == player] or\
           [3, 4, 5] == [i for i in [3, 4, 5] if state[i] == player] or\
           [6, 7, 8] == [i for i in [6, 7, 8] if state[i] == player] or\
           [0, 3, 6] == [i for i in [0, 3, 6] if state[i] == player] or\
           [1, 4, 7] == [i for i in [1, 4, 7] if state[i] == player] or\
           [2, 5, 8] == [i for i in [2, 5, 8] if state[i] == player] or\
           [0, 4, 8] == [i for i in [0, 4, 8] if state[i] == player] or\
           [2, 4, 6] == [i for i in [2, 4, 6] if state[i] == player]:
            return True
        else:
            return False

    def __str__(self):
        return self.renderer.render(self.state)
