# controller.py
"""
Controller coordinates the work of the planner and agent for a specific faction, managing the shared world model.
"""
from agent import Agent
from planner import *
from worldmodel import WorldModel
from faction import Faction
from action import Action
import config

class Controller:
    def __init__(self):
        self.model: WorldModel = None
        self.active_faction: Faction = None
        self.agent:Agent = None
        self.planner: Planner = None

    def setup(self, current_faction: Faction):
        self.model = WorldModel(current_faction.systems, config.goal_list, [])
        self.active_faction = current_faction
        self.agent = Agent(self.model)
        self.planner = SimplePlanner(self.model)

        # Set up initial candidate actions
        # TODO: what's wrong with this?
        for sys1 in self.active_faction.systems.values():
            for sys2_desc in sys1.neighbors:
                sys2 = self.active_faction.systems[sys2_desc[0]]
                if sys1.status == "settled":
                    sys2.status = "discovered"
                    act = Action({"name": "visit", "source": sys1.name, "destination": sys2_desc[0],
                                  "preconditions": [sys1.status], "satisfies": "visited",
                                  "cost": sys2_desc[1], "duration": sys2_desc[1]})
                    self.model.action_list.append(act)

    def run(self) -> bool:
        time = 1
        while time < 100 and len(self.model.action_list) > 0:
            print("\nYear", time)
            # choose a goal
            current_goal = self.planner.choose_goal()
            print("Current goal is {}".format(current_goal.name))
            # make a plan
            current_plan = self.planner.make_plan(current_goal)
            # execute the plan
            for action in current_plan:
                self.agent.take_action(action)
            self.update_faction()
            #TODO: is this the right order for these? what else could be done better?
            self.update_goals()
            time += 1
        return False

    def update_goals(self):
        pass

    def execute_plan(self, plan):
        for action in plan:
            self.agent.take_action(action)

    def update_faction(self):
        self.active_faction.update()
        print (self.active_faction.name, " population =", self.active_faction.population)
        print (self.active_faction.name, " resources =", self.active_faction.resources)
        print (self.active_faction.name, " available resources =", self.active_faction.resources-self.active_faction.population)

# Controller class for use with goal oriented action planner
class GoapController(Controller):
    def __init__(self):
        Controller.__init__(self)
        self.planner: GoapPlanner = None
