# Main
# SANKETH KARUTURI
# Demonstrate the use of your EightPuzzleAgent.

from eight_puzzle_problem import EightPuzzleProblem
from eight_puzzle_transition_model import EightPuzzleTransitionModel
from eight_puzzle_best_first_search_solver import EightPuzzleBestFirstSearchSolver
from eight_puzzle_agent import EightPuzzleAgent

def display_state(state):
    """
    Display the current state of the puzzle as a 3x3 grid.
    
    :param state: A tuple representing the current state of the puzzle.
    """
    for i in range(0, len(state), 3):
        print(state[i:i + 3])  # Print three elements per row to simulate a 3x3 grid.
    print()  # Add a blank line for better readability.

def main():
    """
    Demonstrate solving the eight puzzle problem using the goal-based agent and A* search algorithm.
    """

    # Define example initial states and a common goal state
    examples = [
        ((1, None, 2, 3, 4, 5, 6, 7, 8), (None, 1, 2, 3, 4, 5, 6, 7, 8)),
        ((1, 2, 3, None, 4, 5, 6, 7, 8), (None, 1, 2, 3, 4, 5, 6, 7, 8)),
        ((7, 2, 4, 5, None, 6, 8, 3, 1), (None, 1, 2, 3, 4, 5, 6, 7, 8)),
        ((8, 6, 7, 2, 5, 4, 3, None, 1), (None, 1, 2, 3, 4, 5, 6, 7, 8))
    ]

    # Iterate through each example problem
    for initial_state, goal_state in examples:
        print("Initial State:")
        display_state(initial_state)  # Show the initial state
        print("Goal State:")
        display_state(goal_state)  # Show the goal state

        # Create the transition model and problem instance
        transition_model = EightPuzzleTransitionModel()
        problem = EightPuzzleProblem(initial_state, goal_state, transition_model)

        # Create the solver and solve the problem using A* search
        solver = EightPuzzleBestFirstSearchSolver(problem)
        solution_node = solver.best_first_search()  # Execute the best-first search algorithm

        if solution_node:
            # Retrieve the list of actions from the solution node
            actions = solver.actions_to_reach_solution_node(solution_node)
            print(f"Solution found in {len(actions)} actions.")  # Print the number of actions in the solution
            print("Actions:", [action.__name__ for action in actions])  # Print action names for clarity

            # Create the agent and use it to execute the solution
            agent = EightPuzzleAgent(initial_state, transition_model, actions)
            print("Executing solution step-by-step:")

            while agent.has_actions():  # Continue until all actions are executed
                next_action = agent.action()  # Get the next action
                print("Performing action:", next_action.__name__)  # Display the action being performed
                next_action(agent)  # Execute the action
                display_state(agent.current_state)  # Display the updated state of the puzzle

            print("Final State:")
            display_state(agent.current_state)  # Display the final state after executing all actions
            print("Puzzle Solved!")
        else:
            print("No solution found.")  # If no solution is found, display a message

        print("=" * 50)  # Separator for readability between examples

if __name__ == "__main__":
    main()  # Run the main function
