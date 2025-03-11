# Main(PART1)
# SANKETH KARUTURI
# The start of your overall agent program.
# Demonstrate the use of your SimpleReflexVacuum and your ModelReflexVacuum.
# The code for using a SimpleReflexVacuum is provided for you.

from simple_reflex_vacuum import SimpleReflexVacuum

def main():
    """
    Main function to demonstrate the SimpleReflexVacuum in a two-location world.
    """

    # Create an instance of the SimpleReflexVacuum agent
    simple_reflex_vacuum = SimpleReflexVacuum()

    # Scenario 1: Location A has dirt
    print("Scenario 1: Location A has dirt")
    action = simple_reflex_vacuum.action('A', 'Dirt')  # Get the action for this percept
    action()  # Execute the action (expected: Sucking dirt...)

    # Scenario 2: Location A is clean
    print("\nScenario 2: Location A is clean")
    action = simple_reflex_vacuum.action('A', None)  # Get the action for tShis percept
    action()  # Execute the action (expected: Moving right...)

    # Scenario 3: Location B has dirt
    print("\nScenario 3: Location B has dirt")
    action = simple_reflex_vacuum.action('B', 'Dirt')  # Get the action for this percept
    action()  # Execute the action (expected: Sucking dirt...)

    # Scenario 4: Location B is clean
    print("\nScenario 4: Location B is clean")
    action = simple_reflex_vacuum.action('B', None)  # Get the action for this percept
    action()  # Execute the action (expected: Moving left...)

    