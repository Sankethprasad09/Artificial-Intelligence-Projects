# main.py
# A demonstration of the WumpusWorldAgent, KnowledgeBase, and WumpusWorld in action.
# We illustrate 5 different scenarios that each produce different behavior.
# SANKETH KARUTURI

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


def main():
    """
    We create five scenarios, each with a distinct world setup, and demonstrate
    how the agent + knowledge base respond.
    """

    # 1) SCENARIO A: Agent at (1,1) with gold also at (1,1).
    #    The simplest scenario: the agent should just grab the gold and then climb out.
    kb_a = KnowledgeBase()
    agent_a = WumpusWorldAgent(kb_a)
    world_a = WumpusWorld(
        agent_location=(1, 1),
        agent_direction='East',
        agent_alive=True,
        wumpus_alive=False,
        wumpus_location=None,
        gold_location=(1, 1),
        pit_locations=[]
    )
    run_scenario("A: Gold in start square", world_a, agent_a)

    # 2) SCENARIO B: Agent at (1,1), with pits to the north. The agent might see 'Breeze'
    #    if it tries to move. Possibly it climbs out immediately if it senses danger.
    kb_b = KnowledgeBase()
    agent_b = WumpusWorldAgent(kb_b)
    world_b = WumpusWorld(
        agent_location=(1, 1),
        agent_direction='East',
        agent_alive=True,
        wumpus_alive=None,
        wumpus_location=None,
        gold_location=(2, 2),
        pit_locations=[(1,2), (2,1)]
    )
    run_scenario("B: Surrounded by pits", world_b, agent_b)

    # 3) SCENARIO C: Agent near a wall. We want to see if 'bump' triggers climbing or turning.
    #    Put agent at (4,1) facing east, so there's an immediate bump. Gold is unreachable.
    kb_c = KnowledgeBase()
    agent_c = WumpusWorldAgent(kb_c)
    world_c = WumpusWorld(
        agent_location=(4, 1),
        agent_direction='East',
        agent_alive=True,
        wumpus_alive=None,
        wumpus_location=None,
        gold_location=(2, 1),
        pit_locations=[]
    )
    run_scenario("C: Agent at (4,1), immediate wall to the east", world_c, agent_c)

    # 4) SCENARIO D: Agent can get gold in (2,1) then come back to (1,1).
    #    Minimal environment with no pits. Let’s see if it tries to pick up gold,
    #    then might come back if we run enough steps.
    kb_d = KnowledgeBase()
    agent_d = WumpusWorldAgent(kb_d)
    world_d = WumpusWorld(
        agent_location=(1,1),
        agent_direction='East',
        agent_alive=True,
        wumpus_alive=False,
        wumpus_location=(2,1), # wumpus is dead but location is smelly
        gold_location=(2,1),
        pit_locations=[]
    )
    run_scenario("D: Gold in (2,1), wumpus dead, no pits", world_d, agent_d)

    print("\nAll scenarios complete.")

if __name__ == '__main__':
    main()
