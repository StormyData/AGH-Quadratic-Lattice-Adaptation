from edge import HyperEdge
from graph import Graph
from node import Node
from edge import HyperEdge
from visualisation import draw
from productions.p4 import P4


g = Graph()
n1 = Node(0, 0, "n1")
n2 = Node(1, 0, "n2")
n3 = Node(1, 1, "n3")
n4 = Node(0, 1, "n4")
n5 = Node(1, 0.5, "n5", hanging=True)
n6 = Node(0, 0.5, "n6", hanging=True)
e1 = HyperEdge((n1, n2), "E", boundary=True)
e2 = HyperEdge((n2, n5), "E", boundary=True)
e3 = HyperEdge((n5, n3), "E", boundary=True)
e4 = HyperEdge((n3, n4), "E", boundary=True)
e5 = HyperEdge((n4, n6), "E", boundary=True)
e6 = HyperEdge((n6, n1), "E", boundary=True)
e7 = HyperEdge((n3, n4, n1, n2), "Q", rip=True)

g.add_node(n1)
g.add_node(n2)
g.add_node(n3)
g.add_node(n4)
g.add_node(n5)
g.add_node(n6)
g.add_edge(e1)
g.add_edge(e2)
g.add_edge(e3)
g.add_edge(e4)
g.add_edge(e5)
g.add_edge(e6)
g.add_edge(e7)

draw(g, "test-before-production.png")
p4 = P4()
g.apply(p4)
draw(g, "test-after-production.png")
