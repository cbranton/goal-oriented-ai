"""
agent.py
Simple agent for goal-oriented system. Agents do things.
Created: Chris Branton, 2023-03-07.

"""

from action import Action
from worldmodel import WorldModel


# helper class
class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Agent():
    def __init__(self, model):

        self.world_model:WorldModel = model


    def take_action(self, assigned_action):
        action_result:tuple = ()
        if assigned_action.name == "discover":
            pass
        if assigned_action.name == "visit":
            action_result = self.visit(assigned_action.source, assigned_action.destination, assigned_action.cost)
        if assigned_action.name == "develop":
            action_result = self.develop (assigned_action.destination, assigned_action.cost)
        self.world_model.action_list.remove(assigned_action)
        return action_result


#TODO: propagate cost/duration
    #TODO: potential problem?
    def add_action(self, action_desc):
        if action_desc[0] == "visit":
            act = Action({"name": action_desc[0], "source": action_desc[1], "destination": action_desc[2],
                      "preconditions": "discovered", "satisfies": "visited",
                      "cost": 0, "duration": 0})
        elif action_desc[0] == "develop":
            act = Action({"name": action_desc[0], "destination": action_desc[1],
                      "preconditions": "visited", "satisfies": "developed",
                      "cost": 0, "duration": 0})
        elif action_desc[0] == "settle":
            act = Action({"name": action_desc[0], "destination": action_desc[1],
                      "preconditions": "developed", "satisfies": "settled",
                      "cost": action_desc[2], "duration": 1})
        self.world_model.action_list.append(act)


    def visit(self,source, destination, cost):
            sys1 = self.world_model.systems[source]
            sys2 = self.world_model.systems[destination]
            print("Visiting", destination, "from", source)
            if sys2.status == "discovered":
                sys2.status = "visited"
                if sys2.habitable_planets > 0:
                    self.add_action(("develop", sys2.name, sys2.total_resources()))
            else: # we don't need to visit
                return sys2.habitable_planets, sys2.total_resources, cost
            # discover undiscovered sys2 neighbors and add possible visit
            for new_dest in sys2.neighbors:
                sys3 = self.world_model.systems[new_dest[0]]
                if sys3.status == "undiscovered":
                    sys3.status = "discovered"
                    self.add_action(("visit", destination, sys3.name))
            habitable_planets = sys2.habitable_planets
            resources = sys2.total_resources()
            return habitable_planets, resources, cost



    def develop(self, destination, cost):
        print ("Developing", destination)
        sys = self.world_model.systems[destination]
        sys.status = "developed"
        if sys.habitable_planets > 0:
            self.add_action(("settle", destination, sys.habitable_planets))
        return sys.habitable_planets, sys.total_resources, cost


    # possible other actions
    def patrol(self):
        pass

    def attack(self, target):
        pass

# Empty module test routine
# TODO: make some tests
def test():
    pass


if __name__ == '__main__':
    test()