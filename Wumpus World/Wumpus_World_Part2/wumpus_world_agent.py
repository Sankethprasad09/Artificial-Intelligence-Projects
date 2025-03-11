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
        print("Turning left")
        world.turned_left()

    def turn_right(self, world):
        print("Turning right")
        world.turned_right()

    def move_forward(self, world):
        print("Moving forward")
        world.moved_forward()

    def shoot(self, world):
        print("Shooting the arrow")
        world.shot()

    def grab(self, world):
        print("Grabbing the gold")
        world.grabbed()

    def climb(self, world):
        print("Climbing out")
        world.climbed()

    def make_percept_sentence(self, percept):
        """
        Transform the percept into a 'sentence' (a set of facts) for the KB.
        A percept is typically a 5-tuple: (Stench, Breeze, Glitter, Bump, Scream).
        If percept is None, handle gracefully by returning an empty set.
        """
        facts = set()
        if percept is None:
            return facts

        (stench, breeze, glitter, bump, scream) = percept

        # Example: if stench is 'Stench', we add "Stench". Otherwise "NoStench".
        if stench == 'Stench':
            facts.add("Stench")
        else:
            facts.add("NoStench")

        if breeze == 'Breeze':
            facts.add("Breeze")
        else:
            facts.add("NoBreeze")

        if glitter == 'Glitter':
            facts.add("Glitter")
        if bump == 'Bump':
            facts.add("Bump")
        if scream == 'Scream':
            facts.add("Scream")

        return facts

    def make_action_query(self):
        """
        Create a 'sentence' (query) asking the KB what action to take.
        We just return a string, "Action?" for the KB to interpret.
        """
        return "Action?"

    def make_action_sentence(self, action):
        """
        Create a 'sentence' describing the action performed.
        e.g. "Action_MoveForward", "Action_Grab", etc.
        Also set "HasGold" if we grabbed the gold.
        """
        facts = set()
        if action == self.move_forward:
            facts.add("Action_MoveForward")
        elif action == self.turn_left:
            facts.add("Action_TurnLeft")
        elif action == self.turn_right:
            facts.add("Action_TurnRight")
        elif action == self.shoot:
            facts.add("Action_Shoot")
        elif action == self.grab:
            facts.add("Action_Grab")
            # Suppose we say that we now have gold:
            facts.add("HasGold")
        elif action == self.climb:
            facts.add("Action_Climb")

        return facts

    def action(self, percept):
        """
        The agent function (KB-AGENT) that decides the next action:
          1) TELL the KB about the current percept.
          2) ASK the KB what action to take.
          3) TELL the KB that we performed that action.
          4) Increment time and return the chosen action.
        """
        # 1) TELL KB about the percept
        self.kb.tell(self.make_percept_sentence(percept))

        # 2) ASK KB for an action
        chosen_action = self.kb.ask(self.make_action_query())

        # 3) TELL KB about the action taken
        self.kb.tell(self.make_action_sentence(chosen_action))

        # 4) Increment time
        self.time += 1

        return chosen_action
