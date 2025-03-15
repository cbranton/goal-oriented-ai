

'''
Universe: systems
System: planets, location, discovers, navigates.
Planet: habitable, resources, moons, enemies.


'''

class Planet:
    name = "unnamed"
    moons = 0
    resources = 0
    population = 0
    habitable = False

    def __init__(self, name, moons, resources, population, habitable):
        self.name = name
        self.moons = moons
        self.resources = resources
        self.population = population
        self.habitable = habitable

    def print(self):
        print(self.name, self.moons, "moons, ", self.resources, "resources, ",
              "population:", self.population, ", habitable=", self.habitable)

class System:
    name = "unnamed"
    status = "unknown"
    planets = []
#    neighbors = []

    def __init__(self, name, status, planets):
        self.name = name
        self.status = status
        self.planets = planets
        self.habitable_planets = sum([planet.habitable for planet in planets])
        self.neighbors =[]

    def total_resources(self):
        total = 0
        for planet in self.planets:
            total += planet.resources
        return total

    def total_population(self):
        total = 0
        for planets in self.planets:
            total += planets.population
        return total


    def print(self):
        print()
        print(self.name, "system: ", self.status)
        print(self.total_population(), "population, ", self.total_resources(), " resources")
        for planet in self.planets:
            planet.print()


class Sector:
    name = "unnamed"
    systems = []
    def __init__(self, name, systems):
        self.name = name
        self.systems = systems

    def print(self):
        print()
        print("Sector", self.name)
        for system in self.systems:
            system.print()

local_sector = Sector(
name = "Local Sector",
systems = [System("Sol", "settled", [
        Planet("Mercury", 0,0,0,False),
        Planet("Venus", 0,0,0,False),
        Planet("Earth", 1,0,2,True),
        Planet("Mars", 0,1,1,True),
        Planet("Jupiter", 4,3,2,True),
        Planet("Saturn", 1,2,1,True),
        Planet("Uranus", 0,1,0,False),
        Planet("Neptune", 1,1,0,False)]),
    System("ProcyonA", "undiscovered", [
        Planet("ProcyonA-I", 1,0,0,False),
        Planet("ProcyonA-II", 0,0,0,False),
        Planet("ProcyonA-III", 1,1,0,True),
        Planet("ProcyonA-IV", 1,0,0,True),
        Planet("ProcyonA-V", 3,1,0,False),
        Planet("ProcyonA-VI", 3,2,0,False)]),
    System( "ProcyonB", "undiscovered", [
        Planet("ProcyonB-I", 0,0,0,False)]),
    System("Barnard'sStar", "undiscovered", [
         Planet("Barnard/'sStar-I", 0,2,0,False)]),
    System("Toliman", "undiscovered", [
        Planet("Toliman-I", 0,0,0,False),
        Planet("Toliman-II", 3,2,0,True)]),
    System("AlphaCentauri", "undiscovered", [
        Planet("AlphaCentauri-I", 0,0,0,False),
        Planet("AlphaCentauri-II", 3,2,0,True),
        Planet("AlphaCentauri-III", 1,1,0,True),
        Planet("AlphaCentauri-IV", 1,0,0,False)]),
    System("Altair", "undiscovered", [
        Planet("Altair-I", 0,2,0,False),
        Planet("Altair-II", 3,0,0,True),
        Planet("Altair-III", 2,1,0,True),
        Planet("Altair-IV", 4,1,0,False),
        Planet("Altair-V", 1,1,0,False)]),
    ])

starlanes =[("ProcyonA", "ProcyonB", 1), ("ProcyonA", "Sol", 12),("Sol", "AlphaCentauri", 4),
            ("Sol", "Altair", 18), ("Sol", "Barnard'sStar",6), ("Toliman", "ProcyonA", 14),
            ("Barnard'sStar","ProcyonA", 18), ("Barnard'sStar", "Altair", 13),
            ("Barnard'sStar", "AlphaCentauri", 2)]


for i in range(len(starlanes)):
    (x,y,z) = starlanes[i]
    starlanes.append((y, x, z))

for system in local_sector.systems:
    for lane in starlanes:
        if system.name == lane[0] and system.name != lane[1]:
            system.neighbors.append((lane[1], lane[2]))
