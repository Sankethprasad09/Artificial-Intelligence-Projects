# EightPuzzleBestFirstSearchSolver: A problem solver for the eight-puzzle problem
# that can apply best-first search to find a solution node. This class encapsulates
# a best-first search algorithm and an evaluation function. It encapsulates the
# application of the algorithm to the problem, and in the end can produce a
# solution, which is a list of actions.
# SANKETH KARUTURI

from queue import PriorityQueue
from eight_puzzle_node import EightPuzzleNode
from eight_puzzle_agent import EightPuzzleAgent


class EightPuzzleBestFirstSearchSolver:
    """
    A class that encapsulates the A* search algorithm to solve the eight-puzzle problem.
    It handles the problem definition, expands nodes, evaluates costs, and generates solutions.
    """

    def __init__(self):
        """
        Initialize the solver. The problem instance is not required at initialization,
        ensuring compatibility with test requirements.
        """
        pass

    def solution(self, problem):
        """
        Solve the problem using the A* search algorithm and return a list of actions 
        that lead from the initial state to the goal state.

        :param problem: An instance of EightPuzzleProblem, representing the problem.
        :return: A list of actions to reach the goal state. If no solution is found, return an empty list.
        """
        frontier = PriorityQueue()  # Priority queue to store nodes based on cost
        explored = set()  # Set to keep track of explored states

        # Create the initial node
        initial_node = EightPuzzleNode(
            state=problem.initial_state,
            parent=None,
            action=None,
            path_cost=0
        )

        # Add the initial node to the frontier with its evaluation cost
        frontier.put((self.cost_so_far_plus_estimated_cost_remaining(initial_node, problem), id(initial_node), initial_node))

        while not frontier.empty():
            # Get the node with the lowest cost
            _, _, current_node = frontier.get()

            # Check if the current node represents the goal state
            if current_node.state == problem.goal_state:
                return self.actions_to_reach_solution_node(current_node)

            # Add the current node's state to the explored set
            explored.add(current_node.state)

            # Expand the current node to generate its child nodes
            for child_node in self.expand(current_node, problem):
                if child_node.state not in explored:
                    # Add child node to the frontier with its evaluation cost
                    frontier.put((
                        self.cost_so_far_plus_estimated_cost_remaining(child_node, problem),
                        id(child_node),  # Ensures unique comparison for nodes with the same cost
                        child_node
                    ))

        return []  # Return an empty list if no solution is found

    def expand(self, node, problem):
        """
        Expand the current node by generating its child nodes based on valid actions.

        :param node: The node to expand.
        :param problem: The problem instance containing the action and transition definitions.
        :return: A list of child nodes generated from the current node.
        """
        children = []
        for action in problem.actions(node.state):
            # Generate the new state resulting from the action
            child_state = problem.result(node.state, action)
            # Calculate the path cost for the child node
            path_cost = node.path_cost + 1  # Each move has a fixed cost of 1
            # Create a new child node
            child_node = EightPuzzleNode(
                state=child_state,
                parent=node,
                action=action,
                path_cost=path_cost
            )
            children.append(child_node)  # Add the child node to the list
        return children

    def cost_so_far_plus_estimated_cost_remaining(self, node, problem):
        """
        Calculate the evaluation function f(n) = g(n) + h(n) for A* search.

        :param node: The current node to evaluate.
        :param problem: The problem instance containing the heuristic definition.
        :return: The total estimated cost to the goal.
        """
        return node.path_cost + self.heuristic(node.state, problem)

    def heuristic(self, state, problem):
        """
        Heuristic function using the Manhattan distance for the eight-puzzle problem.

        :param state: The current state of the puzzle.
        :param problem: The problem instance containing goal state information.
        :return: The heuristic cost representing the estimated distance to the goal.
        """
        # Define the goal positions for each tile
        goal_positions = {
            None: (0, 0), 1: (0, 1), 2: (0, 2),
            3: (1, 0), 4: (1, 1), 5: (1, 2),
            6: (2, 0), 7: (2, 1), 8: (2, 2)
        }

        def position(value):
            """
            Helper function to get the row and column of a value in the puzzle state.
            """
            index = state.index(value)
            return index // 3, index % 3

        # Calculate the total Manhattan distance for all tiles
        total_distance = 0
        for tile in state:
            if tile is not None:  # Skip the blank tile
                current_pos = position(tile)
                goal_pos = goal_positions[tile]
                # Calculate Manhattan distance for the tile
                total_distance += abs(current_pos[0] - goal_pos[0]) + abs(current_pos[1] - goal_pos[1])
        return total_distance

    def actions_to_reach_solution_node(self, node):
        """
        Generate the ordered list of actions from the initial state to the given solution node.

        :param node: The solution node representing the goal state.
        :return: A list of actions in order.
        """
        actions = []
        # Trace back from the solution node to the root node
        while node.parent is not None:
            actions.append(node.action)  # Append the action that led to this node
            node = node.parent  # Move to the parent node
        actions.reverse()  # Reverse the list to get the correct order
        return actions


