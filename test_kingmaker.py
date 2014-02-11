'''
Created on Feb 11, 2014

@author: rwill127
'''

from nose.tools import *
import kingmaker as k

class TestNode(object):
    def setup(self):
        self.n = k.Node(1, 1)
        
    def test_node_init(self):
        eq_(self.n.occupied, False)
        
class TestGrid(object):
    def setup(self):
        self.g = k.Grid()
        
    def test_grid_init(self):
        eq_(len(self.g.nodes), 8)
        eq_(len(self.g.nodes[0]), 8)
        ok_(isinstance(self.g.nodes[0][0], k.Node))
        
    def test_get_node(self):
        n = self.g.get_node(3, 4)
        eq_(n.x, 3)
        eq_(n.y, 4)
        
class TestChar(object):
    def setup(self):
        self.c = k.Character()
        
    def test_get_mod(self):
        self.c.strength = 18
        str_mod = self.c.get_mod(self.c.strength)
        eq_(str_mod, 4)
        self.c.wisdom = 9
        wis_mod = self.c.get_mod(self.c.wisdom)
        eq_(wis_mod, -1)