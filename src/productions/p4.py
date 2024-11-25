from edge import HyperEdge
from graph import Graph
from node import Node
from productions.production import Production

@Production.register
class P4(Production):
    def get_left_side(self) -> Graph:
        g = Graph()
        
        n1 = Node(1, 0, "n1")
        n2 = Node(0, 0, "n2")
        n3 = Node(1, 1, "n3")
        n4 = Node(0, 1, "n4")
        n5 = Node(1, 0.5, "n5", hanging=True)
        n6 = Node(0, 0.5, "n6", hanging=True)

        for node in [n1, n2, n3, n4, n5, n6]:
            g.add_node(node)
        
        g.add_edge(HyperEdge((n1, n2), "E"))
        g.add_edge(HyperEdge((n2, n5), "E"))
        g.add_edge(HyperEdge((n5, n3), "E"))
        g.add_edge(HyperEdge((n3, n4), "E"))
        g.add_edge(HyperEdge((n4, n6), "E"))
        g.add_edge(HyperEdge((n6, n1), "E"))
        g.add_edge(HyperEdge((n3, n4, n1, n2), "Q", rip=True))
        return g

    def get_right_side(self, left: Graph, lvl: int):
        n1, n2, n3, n4, n5, n6, hn1, hn2, hn3, hn4, hn5, hn6, hQ = left.ordered_nodes
        g = Graph()
        n5 = Node(n5.x, n5.y, n5.label, hanging=False)
        n6 = Node(n6.x, n6.y, n6.label, hanging=False)
        n7 = Node((n1.x + n2.x)/2, n1.y, f"{lvl}n7", hanging=not hn1.hyperref.boundary)
        n8 = Node((n3.x + n4.x)/2, n3.y, f"{lvl}n8", hanging=not hn4.hyperref.boundary)
        n9 = Node((n1.x+n2.x+n3.x+n4.x)/4, (n1.y+n2.y+n3.y+n4.y)/4, f"{lvl}n9", hanging=False)
        for n in [n1, n2, n3, n4, n5, n6, n7, n8, n9]:
            g.add_node(n)

        # border of graph
        g.add_edge(HyperEdge((n1, n7), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n7, n2), "E", boundary=hn1.hyperref.boundary))
        g.add_edge(HyperEdge((n2, n5), "E", boundary=hn2.hyperref.boundary))
        g.add_edge(HyperEdge((n5, n3), "E", boundary=hn3.hyperref.boundary))
        g.add_edge(HyperEdge((n3, n8), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n8, n4), "E", boundary=hn4.hyperref.boundary))
        g.add_edge(HyperEdge((n4, n6), "E", boundary=hn5.hyperref.boundary))
        g.add_edge(HyperEdge((n6, n1), "E", boundary=hn6.hyperref.boundary))

        # to center hyper-node
        g.add_edge(HyperEdge((n5, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n6, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n7, n9), "E", boundary=False))
        g.add_edge(HyperEdge((n8, n9), "E", boundary=False))

        # Q-tag hyper-nodes
        g.add_edge(HyperEdge((n1, n7, n9, n6), "Q", rip=False))
        g.add_edge(HyperEdge((n7, n2, n5, n9), "Q", rip=False))
        g.add_edge(HyperEdge((n9, n5, n3, n8), "Q", rip=False))
        g.add_edge(HyperEdge((n6, n9, n8, n4), "Q", rip=False))

        return g