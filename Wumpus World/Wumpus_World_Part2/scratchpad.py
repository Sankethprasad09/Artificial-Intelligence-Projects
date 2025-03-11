# main.py
# A demonstration of the WumpusWorldAgent, KnowledgeBase, and WumpusWorld in action.
# We illustrate 5 different scenarios that each produce different behavior.

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

def run_scenario(name, world, agent):
    """
    Run a scenario until the agent either dies or leaves the cave.
    We'll keep a simple step limit so we don't get stuck forever.
    """
    print(f"\n=== SCENARIO: {name} ===")
    has_gold = False
    step = 0

    while True:
        step += 1
        if step > 40:
            print("Stopping scenario (step limit reached).")
            break

        if not world.agent_alive:
            print("Agent died! Ending scenario.")
            break

        if world.agent_location is None:
            # Agent has left the cave
            if has_gold:
                print("Agent successfully exited with gold!")
            else:
                print("Agent exited (no gold).")
            break

        # We might want to see if the agent holds gold. Since the environment
        # doesn't track that directly, let's do a quick check:
        # If gold_location is None and the agent is alive, we assume we have gold.
        if world.gold_location is None and not has_gold:
            has_gold = True

        # TELL the KB about the agent's location, has_gold
        agent.kb.tell({"AgentLocation": world.agent_location,
                       "HasGold": has_gold})

        # Perceive
        percept = world.percept(world.agent_location)
        print(f"Step {step}, Agent loc: {world.agent_location}, dir: {world.agent_direction}, "
              f"Alive: {world.agent_alive}, HasGold: {has_gold}, Percept: {percept}")

        action_to_execute = agent.action(percept)
        action_to_execute(agent, world)  # e.g., agent.move_forward(world), etc.

"""
Scenario 1: An agent in the initial location, surrounded by pits, should
climb out of the cave.
. . . .
W G . .
P . . .
A P . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 1) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # climb?


"""
Scenario 2: An agent in the initial location, with pits to every immediate
location to the north, would *at least* move once to the east.
. . . .
W G . .
P P P P
A . . .
"""
wumpus_world = WumpusWorld(
    agent_location = (1, 1),
    agent_direction = 'East',
    wumpus_location = (1, 3),
    gold_location = (2, 3),
    pit_locations = [ (1, 2), (2, 2), (3, 2), (4, 2) ]
    )

kb = KnowledgeBase()
# Hint: tell the kb the initial given facts, such as the initial location
# of the agent, and its initial direction.

agent = WumpusWorldAgent(kb)
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # move_forward?

