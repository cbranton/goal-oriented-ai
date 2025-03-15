"""
config.py
Test configuration data for GOAP implementation.

Created: Chris Branton, 2023-05-07.

Note: not all values are used in initial implementation.
Discover adds "discovered"
Visit adds "visited"
Develop adds "developed", increases resource production
Settle adds "settled", increases population
TODO: Move to Faction?
"""

goal_list = [
    {"name": "increase_population", "value": 100},
    {"name": "harvest_resources", "value": 10},
    {"name": "idle", "value": 1, "change": 0},
]


action_list = [
    {"name": "discover", "cost": 2, "precondition": ["neighbor_discovered"], "satisfies": ["discovered"]},
    {"name": "visit", "cost": 2, "precondition": ["discovered", "have_fleet"], "satisfies": ["visited"]},
    {"name": "develop", "cost": 2, "precondition": ["visited", "have_fleet"], "satisfies": ["developed", "population_increased"]},
    {"name": "settle", "cost": 2, "precondition": ["developed", "have_population"], "satisfies": ["settled", "increase_population"]},
    {"name": "idle", "satisfies": ["idle"], "cost": 1}
]

