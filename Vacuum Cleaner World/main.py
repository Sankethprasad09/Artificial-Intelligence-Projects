# main.py(PART2)
# Demonstration of the ModelReflexVacuum agent in a two-location Vacuum-Cleaner World.
# The ModelReflexVacuum agent keeps track of the environment state and acts accordingly.
#SANKETH KARUTURI

from model_reflex_vacuum import ModelReflexVacuum
from location import Location
from state import State
from movement_model import MovementModel
from transition_model import TransitionModel
from sensor_model import SensorModel

def main():
    """
    Main function to demonstrate the ModelReflexVacuum in a two-location world.
    """

    # Initialize the vacuum world with two locations (A and B)
    location_a = Location('A', True)  # A starts with dirt
    location_b = Location('B', False)  # B starts clean
    vacuum_world = State({'A': location_a, 'B': location_b}, 'A')  # Initial state: vacuum at A

    # Define movement rules between the locations
    movements = {
        'A': MovementModel('A', 'B'),
        'B': MovementModel('A', 'B')
    }

    # Create transition and sensor models
    transition_model = TransitionModel(vacuum_world, movements)
    sensor_model = SensorModel(vacuum_world)

    # Instantiate the ModelReflexVacuum agent
    model_vacuum = ModelReflexVacuum(vacuum_world, transition_model, sensor_model)

    # Scenario 1: Start in location A, which has dirt
    print("Scenario 1: Start in location A with dirt")
    action = model_vacuum.action()  # Get the agent's action
    action()  # Execute the action (expected: Sucking dirt...)

    # Scenario 2: Move to location B, which is clean
    print("\nScenario 2: Move to location B, which is clean")
    action = model_vacuum.action()  # Get the agent's action
    action()  # Execute the action (expected: Moving right...)

    # Scenario 3: B is clean, move back to A, now clean
    print("\nScenario 3: Move back to location A, now clean")
    action = model_vacuum.action()  # Get the agent's action
    action()  # Execute the action (expected: Moving left...)

    # Scenario 4: Alternate actions
    print("\nScenario 4: Additional actions based on updated state")
    for _ in range(3):  # Execute a few more actions to see the behavior
        action = model_vacuum.action()
        action()

if __name__ == "__main__":
    main()
