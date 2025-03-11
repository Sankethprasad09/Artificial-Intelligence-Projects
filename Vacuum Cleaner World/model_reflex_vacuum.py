# ModelReflexVacuum: A robot vacuum cleaner modeled as a model-based reflex agent.
# Your implementation should pass the tests in test_model_reflex_vacuum.py.
# SANKETH KARUTURI

class Location:
    """
    Represents a specific location in the vacuum world. Each location has an ID and may contain dirt.
    """
    def __init__(self, id, dirt=None):
        self.id = id
        self.dirt = dirt

    def apply_suction(self):
        """
        Removes dirt from the location by setting the dirt attribute to None.
        """
        self.dirt = None


class State:
    """
    Represents the state of the vacuum world, including all locations and the current location of the vacuum.
    """
    def __init__(self, locations, current_location_id):
        self.locations = locations
        self.current_location_id = current_location_id

    def current_location(self):
        """
        Returns the location object corresponding to the current location ID.
        """
        return self.locations[self.current_location_id]


class TransitionModel:
    """
    Defines how actions affect the state of the vacuum world, including suction and movement.
    """
    def __init__(self, state, movements):
        self.state = state
        self.movements = movements

    def apply_suction(self):
        """
        Removes dirt from the current location in the vacuum world.
        """
        self.state.current_location().apply_suction()

    def move_left(self):
        """
        Updates the current location to the left, as defined in the movements dictionary.
        """
        self.state.current_location_id = self.movements[self.state.current_location_id]['left']

    def move_right(self):
        """
        Updates the current location to the right, as defined in the movements dictionary.
        """
        self.state.current_location_id = self.movements[self.state.current_location_id]['right']


class SensorModel:
    """
    Defines how the vacuum perceives the environment, including sensing dirt and location.
    """
    def __init__(self, state):
        self.state = state

    def sense_dirt(self):
        """
        Checks if there is dirt at the current location.
        """
        return self.state.current_location().dirt is not None

    def sense_location_id(self):
        """
        Returns the ID of the current location.
        """
        return self.state.current_location().id


class ModelReflexVacuum:
    """
    A model-based reflex agent that uses state, transition, and sensor models to decide actions.
    """
    def __init__(self, state, transition_model, sensor_model):
        self.state = state
        self.transition_model = transition_model
        self.sensor_model = sensor_model
        self.most_recent_action = None

    def suck(self):
        """
        Perform the suction action to clean the current location.
        """
        self.transition_model.apply_suction()

    def move_left(self):
        """
        Perform the action to move left.
        """
        self.transition_model.move_left()

    def move_right(self):
        """
        Perform the action to move right.
        """
        self.transition_model.move_right()

    def update_state(self):
        """
        Updates the state of the world based on the most recent action.
        """
        if self.most_recent_action:
            self.most_recent_action()

    def action(self):
        """
        Determines the next action based on the current percepts.
        Updates the world state before returning the action.
        """
        self.update_state()
        if self.sensor_model.sense_dirt():
            self.most_recent_action = self.suck
        elif self.sensor_model.sense_location_id() == 'A':
            self.most_recent_action = self.move_right
        elif self.sensor_model.sense_location_id() == 'B':
            self.most_recent_action = self.move_left
        return self.most_recent_action

# Demonstration of ModelReflexVacuum
if __name__ == "__main__":
    # Define locations
    locations = {
        'A': Location('A', True),  # Location A starts with dirt
        'B': Location('B', None)  # Location B starts clean
    }

    # Define state
    state = State(locations, 'A')  # Vacuum starts at location A

    # Define movements
    movements = {
        'A': {'left': 'A', 'right': 'B'},
        'B': {'left': 'A', 'right': 'B'}
    }

    # Create transition and sensor models
    transition_model = TransitionModel(state, movements)
    sensor_model = SensorModel(state)

    # Initialize the vacuum agent
    model_reflex_vacuum = ModelReflexVacuum(state, transition_model, sensor_model)

    # Perform actions
    action = model_reflex_vacuum.action()
    action()  # Perform the first action (e.g., Suck at A)
    action = model_reflex_vacuum.action()
    action()  # Perform the second action (e.g., Move Right to B)
