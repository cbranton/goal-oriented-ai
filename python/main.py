"""
main.py
Main program for goal-oriented planning exploration.
"""

import universe
from controller import Controller
from faction import Faction
from universe import starlanes

# For finer grained control of debug statements use an integer
# that increases for greater verbosity
__DEBUG_SIMULATION__ = False

# Run if this script is the top level script
if __name__ == '__main__':
    if __DEBUG_SIMULATION__:
        universe.local_sector.print()
        print("Star lanes:", starlanes)
    faction = Faction("Federation", {})
    for system in universe.local_sector.systems:
        faction.add_system(system, system.status)
    faction_controller = Controller()
    faction_controller.setup(faction)
    faction_controller.run()
#    goap_main()
    print ('Simulation complete')

