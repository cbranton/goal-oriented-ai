# goal-oriented-ai

Code to demonstrate and explore goal-oriented behavior in AI agents.

Initial Python implementation includes a simple planner that selects the first action from a list of current actions for the agent to execute. Much of the checking of preconditions is done by the agent. This could more appropriately be a part of the planner or controller's job. Goal values are not updated, so the first goal is always chosen.

Several other minor issues are present.

## Resources

Millington, Ian. AI for Games. Available from: VitalSource Bookshelf, (3rd Edition). Taylor & Francis, 2019.
IDA* Section 4.7.4