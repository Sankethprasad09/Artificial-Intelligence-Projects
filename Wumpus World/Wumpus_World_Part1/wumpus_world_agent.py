# WumpusWorldAgent
# An agent designed to perform in the wumpus world environment.
# SANKETH KARUTURI


class WumpusWorldAgent:
    """
    A knowledge-based agent that uses a KnowledgeBase (kb)
    to decide what action to perform in the Wumpus World.
    """

    def __init__(self, kb):
        """
        Store the knowledge base and initialize time.
        """
        self.kb = kb
        self.time = 0

    def turn_left(self, world):
        """
        Turn left actuator:
        - Print a message for clarity
        - Communicate to the world that we turned left
        """
        print("Turning left")
        world.turned_left()

    def turn_right(self, world):
        """
        Turn right actuator:
        - Print a message for clarity
        - Communicate to the world that we turned right
        """
        print("Turning right")
        world.turned_right()

    def move_forward(self, world):
        """
        Move forward actuator:
        - Print a message for clarity
        - Communicate to the world that we moved forward
        """
        print("Moving forward")
        world.moved_forward()

    def shoot(self, world):
        """
        Shoot actuator:
        - Print a message for clarity
        - Communicate to the world that we shot an arrow
        """
        print("Shooting the arrow")
        world.shot()

    def grab(self, world):
        """
        Grab actuator:
        - Print a message for clarity
        - Communicate to the world that we grabbed the gold
        """
        print("Grabbing the gold")
        world.grabbed()

    def climb(self, world):
        """
        Climb actuator:
        - Print a message for clarity
        - Communicate to the world that we climbed out
        """
        print("Climbing out")
        world.climbed()

    def make_percept_sentence(self, percept):
        """
        Transform the percept into a 'sentence' for the KB.
        For now, we do not implement any real logic – just a stub.
        """
        pass

    def make_action_query(self):
        """
        Create a 'sentence' (query) asking the KB what action to take.
        For now, a stub.
        """
        pass

    def make_action_sentence(self, action):
        """
        Create a 'sentence' telling the KB that this action was performed.
        For now, a stub.
        """
        pass

    def action(self, percept):
        """
        The agent function (KB-AGENT) that decides the next action:
          1) TELL the KB about the current percept.
          2) ASK the KB what action to take.
          3) TELL the KB that we are performing that action.
          4) Increment time and return the chosen action.
        """
        # 1. TELL KB about the percept
        self.kb.tell(self.make_percept_sentence(percept))

        # 2. ASK KB for an action
        chosen_action = self.kb.ask(self.make_action_query())

        # 3. TELL KB about the action taken
        self.kb.tell(self.make_action_sentence(chosen_action))

        # 4. Increment time and return the chosen action
        self.time += 1
        return chosen_action
