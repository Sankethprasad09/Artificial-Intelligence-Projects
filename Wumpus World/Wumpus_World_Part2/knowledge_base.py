# KnowledgeBase
# A knowledge base for a knowledge-based agent.
# SANKETH KARUTURI

from wumpus_world_agent import WumpusWorldAgent

class KnowledgeBase:
    """
    A rule-based KB that tracks:
      - agent_location: (x, y)
      - has_gold: bool
      - stench, breeze, glitter, bump, scream: booleans
    """

    def __init__(self):
        # Default to unknown location => we assume (1,1) as a fallback
        self.agent_location = None
        self.has_gold = False
        self.stench = False
        self.breeze = False
        self.glitter = False
        self.bump = False
        self.scream = False

    def tell(self, sentence):
        """
        Update our known facts. 'sentence' can be:
         - dict, e.g. {"AgentLocation": (1,1), "HasGold": True}
         - set/list of percepts, e.g. {"Stench","Breeze"}
         - a single string
        """
        if not sentence:
            return

        if isinstance(sentence, dict):
            if "AgentLocation" in sentence:
                self.agent_location = sentence["AgentLocation"]
            if "HasGold" in sentence:
                self.has_gold = bool(sentence["HasGold"])

        elif isinstance(sentence, (set, list)):
            # Reset old percept booleans
            self.stench = False
            self.breeze = False
            self.glitter = False
            self.bump = False
            self.scream = False

            for fact in sentence:
                if fact == "Stench":
                    self.stench = True
                elif fact == "Breeze":
                    self.breeze = True
                elif fact == "Glitter":
                    self.glitter = True
                elif fact == "Bump":
                    self.bump = True
                elif fact == "Scream":
                    self.scream = True
                # If "NoStench", "NoBreeze", etc., remain False

        elif isinstance(sentence, str):
            # Single fact
            if sentence == "HasGold":
                self.has_gold = True
            elif sentence == "Stench":
                self.stench = True
            elif sentence == "Breeze":
                self.breeze = True
            elif sentence == "Glitter":
                self.glitter = True
            elif sentence == "Bump":
                self.bump = True
            elif sentence == "Scream":
                self.scream = True

    def ask(self, query):
        """
        Decide the next action based on stored facts.
        """

        # If agent_location was never told, we assume (1,1).
        if self.agent_location is None:
            self.agent_location = (1,1)

        # 1) If we have gold and are at (1,1) => climb
        if self.has_gold and self.agent_location == (1,1):
            return WumpusWorldAgent.climb

        # 2) If at (1,1) and breeze => presumably no safe path => climb
        #    (but do NOT climb out for stench alone at (1,1)).
        if self.agent_location == (1,1) and self.breeze:
            return WumpusWorldAgent.climb

        # 3) If glitter and not has_gold => grab
        if self.glitter and not self.has_gold:
            return WumpusWorldAgent.grab

        # 4) If bump => turn left
        if self.bump:
            return WumpusWorldAgent.turn_left

        # 5) If stench and we don't have gold => try forging ahead
        if self.stench and not self.has_gold:
            return WumpusWorldAgent.move_forward

        # 6) If breeze (and not at home) => turn left to avoid pit
        if self.breeze:
            return WumpusWorldAgent.turn_left

        # 7) Otherwise => move forward
        return WumpusWorldAgent.move_forward
