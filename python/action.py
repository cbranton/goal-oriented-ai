"""
action.py
Actions and related code for goal-oriented behavior modeling.
Created: Chris Branton, 2023-03-07.

Preconditions should be satisfied in the world before an action can be
applied.
"""


class Action:

    def __init__(self, action_dict):
        self.name = action_dict["name"]
        if "source" in action_dict:
            self.source = action_dict["source"]
        if "destination" in action_dict:
            self.destination = action_dict["destination"]
        self.requires = action_dict.get("precondition", [])
        self.results = action_dict.get("satisfies", [])
        self.cost = action_dict.get("cost", 0)
        self.duration = action_dict.get("duration", 0)

    def is_valid(self, preconditions):
        for condition in self.requires:
            if not condition.valid(preconditions):
                return False
        return True

    @property
    def get_duration(self):
        return self.duration

    @property
    def get_cost(self):
        return self.cost

    @property
    def get_goal_change(self):
        return self.cost

