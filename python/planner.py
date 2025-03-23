"""
planner.py
Planning component for goal-oriented AI modeling.
Created: Chris Branton, 2023-03-07.
Adapted from a techniques presented in AI for Games, 3rd Edition, by Ian Millington
NOTE: in AI literature, discontent (what we call value) is often called "energy metric"

"""

import copy
from typing import List, Optional

from python.worldmodel import WorldModel
from goal import Goal


class Planner:

    def __init__(self, world_model):
        self.model = world_model

    def make_plan(self, current_goal):
        pass

    # Chooses a goal to pursue based on
    def choose_goal(self):
        # check for empty list
        if not self.model.goal_list:
            return None
        top_goal = self.model.goal_list[0]
        for candidate in self.model.goal_list[1:]:
            if candidate.get_value() > top_goal.get_value():
                top_goal = candidate
        return top_goal


class SimplePlanner(Planner):
    def __init__(self, world_model):
        super(SimplePlanner, self).__init__(world_model)

    def make_plan(self, current_goal):
        plan = [self.model.action_list[0]]
        #TODO: check requirements and cost
        return plan


class GoapPlanner(Planner):
    def __init__(self, world_model):
        super(GoapPlanner, self).__init__(world_model)

    def make_plan(self, current_goal):
        for iteration in range(20):
            # Limit the depth to the number of possible actions.
            max_depth = self.model.num_actions
            action_plan = self.plan_action(self.model, max_depth)
            if action_plan:
                print("Best plan is")
                for a in action_plan:
                    if a:
                        print(a.name)
            else:
                print("No plan found")
            print()

    # This method is intentionally small to facilitate different
    # search methods
    def plan_action(self, model, max_depth=10):
        current_goal = self.choose_goal()
        action_plan = self.depth_first(model, current_goal, max_depth)
        # if we have an action, return it
        return action_plan

    # Simple depth first search to find a viable action sequence
    def depth_first(self, model: WorldModel, current_goal: Goal, max_depth: int):

        # storage for models, actions, and costs at each depth
        model_array:list[Optional[WorldModel]] = [None] * (max_depth +1)
        model_array[0]:WorldModel = model
        action_sequence = [None] * max_depth
        costs = [0] * max_depth

        # initial state
        current_depth = 0

        while current_depth >= 0:

            # check for a goal
            if current_goal.is_fulfilled(model_array[current_depth]):
                # return with result
                return action_sequence

            # otherwise try the next action
            next_action = model_array[current_depth].next_action()

            if next_action:
                # copy the current model and apply the action
                model_array[current_depth+1] = copy.deepcopy(model_array[current_depth])
                action_sequence[current_depth] = next_action
                model_array[current_depth + 1].apply_action(next_action)

                # set costs[current_depth+1]
                costs[current_depth+1] = costs[current_depth] + next_action.get_cost

                # on to the next level
                current_depth += 1

            else:  # no action to try
                   # drop back
                current_depth -= 1

        # finished iterating and didn't find an action
        return None