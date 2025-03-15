"""
planner.py
Planning component for goal-oriented AI modeling.
Created: Chris Branton, 2023-03-07.
Adapted from a techniques presented in AI for Games, 3rd Edition, by Ian Millington
NOTE: in AI literature, discontent (what we call value) is often called "energy metric"

"""

import copy

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
