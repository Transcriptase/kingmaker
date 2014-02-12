'''
Created on Feb 11, 2014

@author: rwill127
'''
#Globals: Tables

#Name, Stability, Consumption
PROMOTION_TABLE = {"None": [-1, 0],
                   "Token": [1, 1],
                   "Standard": [2, 2],
                   "Aggressive": [3, 4],
                   "Expansionist": [4, 8]}

#Name, Economy, Loyalty
TAXATION_TABLE = {"None": [0, 1],
                  "Light": [1, -1],
                  "Normal": [2, -2],
                  "Heavy": [3, -4],
                  "Overwhelming": [4, -8]}

#Number Per Year, Loyalty, Consumption
HOLIDAY_TABLE = {0: [-1, 0],
                 1: [1, 1],
                 6: [2, 2],
                 12: [3, 4],
                 24: [4, 8]
                 }

class Kingdom(object):
    def __init__(self):
        #Core Stats
        self.economy = 0
        self.stability = 0
        self.loyalty = 0
        
        #Secondary Stats
        self.unrest = 0
        self.treasury = 0
        self.consumption = 0
        
        #Alignment
        self.order_alignment = "Neutral"
        self.moral_alignment = "Neutral"
        
        #Size
        self.size = 0
        self.control_dc = 20 + self.size
        self.population = 0
        
        #Maps
        self.cities = []
        self.hexes = []
        
        #Leaders
        self.leader_roles = ["Ruler",
                             "Councilor",
                             "General",
                             "Grand Diplomat",
                             "High Priest",
                             "Magister",
                             "Marshal",
                             "Royal Assassin",
                             "Spymaster",
                             "Treasurer",
                             "Warden"
                             ]
        
        self.leader_stats = [["CHA"],
                             ["CHA", "WIS"],
                             ["CHA", "STR"],
                             ["CHA", "INT"],
                             ["CHA", "WIS"],
                             ["CHA", "INT"],
                             ["DEX", "WIS"],
                             ["DEX", "STR"],
                             ["DEX", "INT"],
                             ["INT", "WIS"]
                             ["CON", "STR"]
                             ]
        
        self.leader_effects = ["Flexible",
                               "Loyalty",
                               "Stability",
                               "Stability",
                               "Stability",
                               "Economy",
                               "Economy",
                               "Loyalty",
                               "Flexible",
                               "Economy",
                               "Loyalty"]
        
        #Edicts
        self.promotion = "None"
        self.taxation = "Normal"
        self.holidays = 0
        

        
        
    def calculate_economy(self):
        economy = 0
        if self.order_alignment == "Lawful":
            economy += 2
        if self.moral_alignment == "Evil":
            economy += 2
        for city in self.cities:
            economy += city.calculate_economy()
        mine_count = 0
        road_count = 0
        river_count = 0
        for hex in self.hexes:
            if hex.mine:
                mine_count += 1
            if hex.road:
                road_count += 1
            if hex.river:
                river_count += 1
        economy += (mine_count +
                          int(road_count/4) +
                          int(river_count/4)
                          )
        economy -= self.unrest
        
        
class Character(object):
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        
        self.name = None
        
    def setup(self, profile):
        '''
        Takes a dict of the character's name and stats
        and creates a Character object from it.
        '''
        self.name = profile["Name"]
        self.strength = profile["STR"]
        self.dexterity = profile["DEX"]
        self.constitution = profile["CON"]
        self.intelligence = profile["INT"]
        self.wisdom = profile["WIS"]
        self.charisma = profile["CHA"]
        
    def get_mod(self, stat):
        modifier = (int(stat) - 10)/2
        return modifier
    
class Node(object):
    '''
    A single location on a map grid.
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.occupied = False
        
    def __str__(self):
        return "Node(%s, %s)" % (self.x,self.y)
        
    def __repr__(self):
        return "Node(%r, %r)" % (self.x, self.y)
        
class Grid(object):
        '''
        A cartesian grid of nodes, stored as a list of lists
        '''
        def __init__(self):
            '''
            Note that this construction method means that the
            y coordinate comes first when calling directly from
            the map matrix.
            
            To avoid confusion, use get_node(x, y) instead of
            raw indexing.
            '''
            self.nodes = []
            for j in range(8):
                self.nodes.append([])
                for i in range(8):
                    new_node = Node(i, j)
                    self.nodes[j].append(new_node)
                    
        def get_node(self, x, y):
            return self.nodes[y][x]
        
class HexMap(object):
    def __init__(self, x, y):
        '''
        Note that this construction method means that the
        y coordinate comes first when calling directly from
        the map matrix.
        
        To avoid confusion, use get_node(x, y) instead of
        raw indexing.
        '''
        self.nodes = []
        for j in range(y):
            self.nodes.append([])
            for i in range(x):
                new_node = Node(i, j)
                self.nodes[j].append(new_node)
                
    def get_node(self, x, y):
        return self.nodes[y][x]           

        
class Settlement(object):
    def __init__(self):
        self.first_grid = Grid()
        self.grids = [self.first_grid]
        self.buildings = []
        
class Building(object):
    def __init__(self):
        self.economy = 0
        self.loyalty = 0
        self.stability = 0
        self.base_value = 0
        self.lots = 1
        self.location = (0,0)