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