"""
faction.py

Faction class represents a party in the simulation. Each faction keeps their own
world model.
"""

class Faction():

    def __init__(self, name, systems):
        self.name = name
        self.systems = systems
        self.population = 0
        self.resources = 0

    # TODO: make sure we are copying system
    def add_system(self, system, status):
        self.systems[system.name] = system
        self.systems[system.name].status = status
        self.update()

    def update(self):
        for system in self.systems.values():
            if system.status == "settled":
                self.population += system.habitable_planets
                self.resources += system.total_resources()
                self.resources -= system.total_population()
            if system.status == "developed":
                self.resources += system.total_resources()

