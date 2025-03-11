# EightPuzzleAgent: A goal-based agent that emits the actions from a solution to
# an "eight puzzle" problem.
# Your implementation should pass the tests in test_eight_puzzle_agent.py.
# SANKETH KARUTURI

class EightPuzzleAgent:
    def __init__(self, initial_state, transition_model, actions):
        """
        Initialize the EightPuzzleAgent with the required attributes.

        :param initial_state: The starting state of the puzzle (a tuple representing the board).
        :param transition_model: An object that provides methods to define state transitions for each action.
        :param actions: A list of actions that the agent will execute to solve the puzzle.
        """
        self.current_state = initial_state  # Set the initial state of the puzzle.
        self.transition_model = transition_model  # Define how actions transition the state.
        self.actions = actions  # List of actions to reach the goal state.

    def has_actions(self):
        """
        Check if there are any actions left for the agent to perform.

        :return: True if there are remaining actions, False otherwise.
        """
        return len(self.actions) > 0  # Check if the actions list is not empty.

    def action(self):
        """
        Retrieve and execute the next action from the list of actions.

        :return: The next action to be executed if available, otherwise None.
        """
        if self.has_actions():  # If there are actions left to execute:
            return self.actions.pop(0)  # Remove and return the first action from the list.
        return None  # If no actions are left, return None.

    def move_left(self):
        """
        Perform the "move left" action. Updates the current state accordingly.
        """
        print("Left")  # Print the action being performed.
        self.current_state = self.transition_model.move_left(self.current_state)  
        # Use the transition model to compute the new state after moving left.

    def move_right(self):
        """
        Perform the "move right" action. Updates the current state accordingly.
        """
        print("Right")  # Print the action being performed.
        self.current_state = self.transition_model.move_right(self.current_state)  
        # Use the transition model to compute the new state after moving right.

    def move_up(self):
        """
        Perform the "move up" action. Updates the current state accordingly.
        """
        print("Up")  # Print the action being performed.
        self.current_state = self.transition_model.move_up(self.current_state)  
        # Use the transition model to compute the new state after moving up.

    def move_down(self):
        """
        Perform the "move down" action. Updates the current state accordingly.
        """
        print("Down")  # Print the action being performed.
        self.current_state = self.transition_model.move_down(self.current_state)  
        # Use the transition model to compute the new state after moving down.
