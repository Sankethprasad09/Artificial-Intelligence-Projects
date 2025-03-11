# Exercise 9: Wumpus World Part 2, Knowledge Base

Implement the knowledge-based agent design, and a knowledge base with
propositional logic.

## What to Do

In the first part of our Wumpus World adventure, we created WumpusWorld, a
simulation of a real-world environment for our agent to operate within. We also
implemented a version of our knowledge-based agent and its knowledge base.

Implement the details of the WumpusWorldAgent that is a goal-based,
knowledge-based agent, and complete the implementation of the KnowledgeBase
that, internally, relies on propositional logic.

**This is a creative and design exercise.** There are _many_ ways you may choose
to implement this, and the entire purpose of this exercise is to enable you to
confront numerous implementation decisions. Your agent does not have to be
the smartest or the most capable, but ensure that your implementation honors the
specficiations of the KB-AGENT in the AIMA book.

## Instructions

Your agent needs help! It has capabilities, but no brain.

In this exercise, you are provided with a complete implementation of WumpusWorldAgent,
found in *wumpus_world_agent.py*, KnowledgeBase found in *knowledge_base.py*, and
the WumpusWorld found in *wumpus_world.py*. Each class has an accompanying unit
test suite, and the tests should all pass at the start of this exercise.

Now, take a look at *scratchpad.py*, where we have made one small but important
change. Previously, our agent explicity fetched a percept from location (1, 1),
and executed that action:

```
action = agent.action(wumpus_world.percept((1, 1)))
action(agent, wumpus_world)
```

Now, our agent chooses an action based on the percept of "wherever the agent is
in the world":

```
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world)
```

Your goal is to create scenarios in *main.py* that demonstrate interesting agent
behavior. You will need to implement the agent's `make_percept_sentence`,
`make_action_query` and `make_action_sentence` methods; and you will need to
implement as much of the KnowledgeBase as you can.

When complete, you should be able to run your code in *main.py* and demonstrate
three to five scenarios in which the agent seems to make the best decisions.

Two initial scenarios are provided for you in *scratchpad.py*.

We suggest the following steps.

### Step 1: Simple Scenarios

Create three simple, "single-action" scenarios in *main.py* that demonstrate
some basic rational behavior.

If you take a look at *scratchpad.py*, you will find an example of two scenarios.
Design some simple scenarios that enable you to begin experimenting with propositional
logic and some simple inference. Design scenarios that intentionally encourage
only one possible action. For example, create a scenario in which:

- the agent, in the initial location, is surrounded by pits. The only rational
  action is to climb out
- the agent is in the same location as the gold. The only rational action is to
  grab the gold
- the agent, surrounded by pits, would do nothing :(
- the agent, in the initial location, with gold in hand, should climb out

Simple scenarios will immediately get you thinking about how the agent and the
knowledge base interact, and encourage you to begin making decisions about how
to implement the KnowledgeBase and the propositional logic sentences.

### Step 2: Moderate Scenarios

When you feel like your agent and its knowledge base are authentically handling
simple scenarios, introduce moderately complex scenarios. Keep the scenarios
as constrained as possible, but expect more complex behavior. For example:

- the agent, in the initial location, with pits in every location to the north,
  might move east repeatedly, bump into the wall, turn around, move west, and
  climb out
- same as the previous scenario, but in a northerly direction
- the agent, with gold in hand, should navigate toward the exit

Keep your scenarios simple and constrained.

### Step 3: Complex Scenarios

Set up a simulation of wumpus world that matches the example in the AIMA text.
Demonstrate the agent's ability to navigate to the gold, possibly kill the wumpus,
and exit the cave with the gold.

Note that this can be challenging due to the number of sentences in the knowledge
base, and the inference that this may entail.

### Step 4: Demonstrate

Each of your scenarios should be implemented in *main.py*.

## Notes and Hints

Take risks and be creative. Run into many dead ends and try something new. Ask
questions in our discussion forum for ideas from other students.

Be sure that any scenarios that demonstrate more than one action resemble the
example fetch-execute steps mentioned above in this README and in *scratchpad.py*.
For example:

```
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # turn_left
action = agent.action(wumpus_world.percept(wumpus_world.agent_location))
action(agent, wumpus_world) # move_forward
```

Be sure to always be passing `wumpus_world.agent_location` to the `percept` method.

Be creative. Explore and hack. Apply your understanding of propositional logic
and inference to implement _simple_ logic and action production in the knowledge
base.

The function `make_action_query` can simply return a string, such as `"Action"`.

We do not recommend making changes to WumpusWorld. Its tests should remain passing.

&copy; 2023 Yong Joseph Bakos. All rights reserved.
