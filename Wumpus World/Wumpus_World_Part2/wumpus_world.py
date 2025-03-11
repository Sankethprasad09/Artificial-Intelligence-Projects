# wumpus_world.py
# A simulated representation of the real Wumpus World, aligned with AIMA specs.
# SANKETH KARUTURI

class WumpusWorld:
    """
    The WumpusWorld simulates the physical environment and its rules:
    - The agent can be killed by moving into pits or a living wumpus.
    - The agent can detect stench, breeze, glitter, bump, and a persistent scream (if wumpus is dead).
    - The cave is a 4x4 grid with (1,1) as the exit.
    """
    EXIT_LOCATION = (1, 1)

    def __init__(self,
                 agent_location=(1, 1),
                 agent_direction='East',
                 agent_alive=True,
                 wumpus_alive=None,
                 wumpus_location=None,
                 gold_location=None,
                 pit_locations=None):
        """
        Initialize the world with default or user-provided values.
        """
        if pit_locations is None:
            pit_locations = []

        self.agent_location = agent_location
        self.agent_direction = agent_direction
        self.agent_alive = agent_alive
        self.wumpus_alive = wumpus_alive
        self.wumpus_location = wumpus_location
        self.gold_location = gold_location
        self.pit_locations = pit_locations

    def percept(self, location):
        """
        Return the percept in `location` as a tuple:
          (Stench, Breeze, Glitter, Bump, Scream)
        Each can be None or a string (e.g. 'Stench').
        """
        if location is None:
            # Agent is effectively out of the world
            return (None, None, None, None, None)

        stench = None
        breeze = None
        glitter = None
        bump = None
        scream = None

        # Stench: if location == wumpus_location or adjacent
        if self.wumpus_location is not None:
            if location == self.wumpus_location or self.adjacent(location, self.wumpus_location):
                stench = 'Stench'

        # Breeze: if location is adjacent to any pit
        for pit in self.pit_locations:
            if self.adjacent(location, pit):
                breeze = 'Breeze'
                break

        # Glitter: if location == gold_location
        if location == self.gold_location:
            glitter = 'Glitter'

        # Bump: if the agent is here AND is facing a wall
        if location == self.agent_location and self.agent_bumped_wall():
            bump = 'Bump'

        # Scream: if wumpus is dead
        if self.wumpus_alive == False:
            scream = 'Scream'

        return (stench, breeze, glitter, bump, scream)

    def turned_left(self):
        """
        Turn the agent counter-clockwise (left).
        East -> North -> West -> South -> East
        """
        directions = ['East', 'North', 'West', 'South']
        idx = directions.index(self.agent_direction)
        self.agent_direction = directions[(idx + 1) % 4]

    def turned_right(self):
        """
        Turn the agent clockwise (right).
        East -> South -> West -> North -> East
        """
        directions = ['East', 'South', 'West', 'North']
        idx = directions.index(self.agent_direction)
        self.agent_direction = directions[(idx + 1) % 4]

    def moved_forward(self):
        """
        Move forward in the direction the agent is facing, unless there's a wall.
        If the new location is a pit or a living wumpus, agent dies.
        """
        if not self.agent_alive:
            return

        x, y = self.agent_location
        new_x, new_y = x, y

        if self.agent_direction == 'East' and x < 4:
            new_x = x + 1
        elif self.agent_direction == 'West' and x > 1:
            new_x = x - 1
        elif self.agent_direction == 'North' and y < 4:
            new_y = y + 1
        elif self.agent_direction == 'South' and y > 1:
            new_y = y - 1

        self.agent_location = (new_x, new_y)

        # Check for death: pit or living wumpus
        if self.agent_location in self.pit_locations:
            self.agent_alive = False
        elif self.agent_location == self.wumpus_location and self.wumpus_alive is True:
            self.agent_alive = False

    def grabbed(self):
        """
        Grab the gold if we're in the gold location; remove it.
        """
        if self.agent_alive and self.agent_location == self.gold_location:
            self.gold_location = None

    def climbed(self):
        """
        Climb out of the cave if at (1,1).
        """
        if self.agent_location == self.EXIT_LOCATION:
            self.agent_location = None

    def shot(self):
        """
        Fire an arrow in the current direction. If the wumpus is in that line
        (and at the same y if East/West, or same x if North/South), the wumpus dies.
        """
        if not self.agent_alive or not self.wumpus_alive:
            return

        ax, ay = self.agent_location
        if self.wumpus_location is None:
            return
        wx, wy = self.wumpus_location

        if self.agent_direction == 'East':
            if wy == ay and wx > ax:
                self.wumpus_alive = False
        elif self.agent_direction == 'West':
            if wy == ay and wx < ax:
                self.wumpus_alive = False
        elif self.agent_direction == 'North':
            if wx == ax and wy > ay:
                self.wumpus_alive = False
        elif self.agent_direction == 'South':
            if wx == ax and wy < ay:
                self.wumpus_alive = False

    def adjacent(self, location, target):
        """
        True if location and target are directly N, S, E, W of each other.
        """
        if location is None or target is None:
            return False
        (x1, y1) = location
        (x2, y2) = target
        return ((x1 == x2 and abs(y1 - y2) == 1) or
                (y1 == y2 and abs(x1 - x2) == 1))

    def agent_can_move_east(self):
        return self.agent_location[0] < 4

    def agent_can_move_west(self):
        return self.agent_location[0] > 1

    def agent_can_move_north(self):
        return self.agent_location[1] < 4

    def agent_can_move_south(self):
        return self.agent_location[1] > 1

    def agent_bumped_wall(self):
        """
        Has the agent bumped into a wall? i.e. facing outside boundary.
        """
        if not self.agent_location:
            return False
        x, y = self.agent_location
        if self.agent_direction == 'North' and y == 4:
            return True
        if self.agent_direction == 'South' and y == 1:
            return True
        if self.agent_direction == 'East' and x == 4:
            return True
        if self.agent_direction == 'West' and x == 1:
            return True
        return False

    def wumpus_east_of_agent(self):
        if self.wumpus_location is None or self.agent_location is None:
            return False
        ax, ay = self.agent_location
        wx, wy = self.wumpus_location
        return (ay == wy and wx > ax)

    def wumpus_west_of_agent(self):
        if self.wumpus_location is None or self.agent_location is None:
            return False
        ax, ay = self.agent_location
        wx, wy = self.wumpus_location
        return (ay == wy and wx < ax)

    def wumpus_north_of_agent(self):
        if self.wumpus_location is None or self.agent_location is None:
            return False
        ax, ay = self.agent_location
        wx, wy = self.wumpus_location
        return (ax == wx and wy > ay)

    def wumpus_south_of_agent(self):
        if self.wumpus_location is None or self.agent_location is None:
            return False
        ax, ay = self.agent_location
        wx, wy = self.wumpus_location
        return (ax == wx and wy < ay)
