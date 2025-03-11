# SimpleReflexVacuum: A simple reflex agent modeled as a robot vacuum cleaner.
# The agent decides its actions based only on the current percepts (location and dirt status).
# This implementation should pass the tests in test_simple_reflex_vacuum.py.
# SANKETH KARUTURI

class SimpleReflexVacuum:
    """
    A simple reflex agent representing a vacuum cleaner in a two-location world.
    The agent can perform three actions: suck (to clean dirt), move left, or move right.
    It makes decisions based solely on its current percepts (location and whether there is dirt).
    """

    def suck(self):
        """
        Perform the 'suck' action to clean dirt in the current location.
        """
        print("Sucking dirt...")

    def move_left(self):
        """
        Perform the 'move left' action to move to the left location.
        """
        print("Moving left...")

    def move_right(self):
        """
        Perform the 'move right' action to move to the right location.
        """
        print("Moving right...")

    def action(self, location_id, dirt):
        """
        Decide the next action based on the current percepts.

        Parameters:
        location_id (str): The ID of the current location ('A' or 'B').
        dirt (str): The status of dirt in the current location ('Dirt' or None).

        Returns:
        function: The action (method) to be executed.
        """
        # If there is dirt in the current location, suck it up
        if dirt == "Dirt":
            return self.suck
        # If there is no dirt and the location is A, move to the right
        elif location_id == "A":
            return self.move_right
        # If there is no dirt and the location is B, move to the left
        elif location_id == "B":
            return self.move_left
