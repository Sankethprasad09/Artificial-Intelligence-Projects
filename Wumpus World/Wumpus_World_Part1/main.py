# Main
# A demonstration of the WumpusWorld and WumpusWorldAgent.
# SANKETH KARUTURI

from wumpus_world import WumpusWorld
from wumpus_world_agent import WumpusWorldAgent
from knowledge_base import KnowledgeBase

def main():
    """
    Demonstrates a loop of interactions between a WumpusWorldAgent and its environment
    (WumpusWorld), including a performance measure calculation.
    """

    # --- Create a canonical 4x4 Wumpus World ---
    # Default example:
    # - The agent starts at (1,1), facing East, alive
    # - The Wumpus is at (1,3) and is alive
    # - Gold is at (2,3)
    # - Pits at (3,1), (3,3), (4,3)
    world = WumpusWorld(
        agent_location=(1, 1),
        agent_direction='East',
        agent_alive=True,
        wumpus_alive=True,
        wumpus_location=(1, 3),
        gold_location=(2, 3),
        pit_locations=[(3, 1), (3, 3), (4, 3)]
    )

    # --- Create a KnowledgeBase and the WumpusWorldAgent ---
    kb = KnowledgeBase()
    agent = WumpusWorldAgent(kb)

    # Track whether the agent has picked up gold
    has_gold = False

    # Performance measure scoring:
    score = 0

    # --- Simulation Loop ---
    step_count = 0

    while True:
        step_count += 1
        if not world.agent_alive:
            # Agent has died (fell in a pit or eaten by Wumpus)
            score -= 1000
            print("\nAgent died. Final score:", score)
            break

        if world.agent_location is None:
            # Agent has exited the cave (climbed out)
            # If agent has gold, reward is +1000
            if has_gold:
                score += 1000
            print(f"\nAgent has left the cave. Final score: {score}")
            break

        # The agent perceives the environment at current location
        current_loc = world.agent_location
        percepts = world.percept(current_loc)
        print(f"\nStep {step_count}: Agent is in {current_loc}, facing {world.agent_direction}.")
        print("Percepts:", percepts)

        # Agent decides on an action using the KB (the agent function)
        chosen_action = agent.action(percepts)

        # We figure out which of the standard actions it is, and adjust scoring:
        if chosen_action == agent.move_forward:
            # Each move/turn is -1
            score -= 1
        elif chosen_action == agent.turn_left or chosen_action == agent.turn_right:
            # Each move/turn is -1
            score -= 1
        elif chosen_action == agent.shoot:
            # Shooting costs -10, plus the normal step cost -1, 
            # but you can treat them cumulatively or singly. 
            score -= 10
        elif chosen_action == agent.grab:
            # If gold is here, the agent will pick it up
            # We'll track has_gold with a flag
            pass
        elif chosen_action == agent.climb:
            # The agent tries to climb out if at (1,1)
            pass
        # else: (no default case, but we can handle unrecognized actions if we like)

        # Execute the chosen action in the environment
        chosen_action(agent, world)

        # If the agent just grabbed gold, check if gold was indeed in that location
        if chosen_action == agent.grab:
            # If the world's gold_location is now None, it means agent got it
            if world.gold_location is None:
                has_gold = True
                print("Agent picked up the gold!")

    print("\nSimulation Complete.")

if __name__ == '__main__':
    main()
