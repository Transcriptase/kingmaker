'''
Created on Feb 11, 2014

@author: rwill127
'''

class Kingdom(object):
    def __init__(self):
        self.economy = 0
        self.stability = 0
        self.loyalty = 0
        self.unrest = 0
        self.treasury = 0
        self.consumption = 0
        self.alignment = "neutral"
        self.size = 0
        self.control_dc = 20 + self.size
        self.population = 0
        self.cities = []
        self.hexes = []
        self.leaders = {"Ruler": None,
                        "Councilor": None,
                        "General": None,
                        "Grand Diplomat": None,
                        "High Priest": None,
                        "Magister": None,
                        "Marshal": None,
                        "Royal Assassin": None,
                        "Spymaster": None,
                        "Treasurer": None
                        }     
        
class Character(object):
    def __init__(self):
        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0
        
        self.name = None
        
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
        self.grids = [first_grid]
        self.buildings = []
        
class Building(object):
    def __init__(self):
        self.economy = 0
        self.loyalty = 0
        self.stability = 0
        self.base_value = 0
        self.lots = 1
        self.location = (0,0)