class NodeNotFound(Exception):
    def __init__(self,message):
        super(NodeNotFound,self).__init__(message)

class Graph():
    def __init__(self,vertices={},edges={}):
        self._vertices = set(vertices)
        self._edges = set(edges)
    def insert_node(self,vertice):
        self._vertices.add(vertice)
        return self
    def insert_relation(self,first_node,second_node):
        if not (first_node in self._vertices) or not (second_node in self._vertices): raise NodeNotFound
        self._edges.add((first_node,second_node))
        return self
    def bf_visit_adjacent_nodes(self,node,visited):
        return [adjacent for (first,adjacent) in self._edges if first==node and not adjacent in visited]
    def bf_visit(self):
        visited = self.bf_visit_impl(self._vertices,[])
        return ', '.join(visited)
    def bf_visit_impl(self,vertices,visited):
        print("visited till now: {0}".format(visited))
        for vertice in vertices:
            if not vertice in visited:
                print("Visito vertice {0}".format(vertice))
                adjacents = self.bf_visit_adjacent_nodes(vertice,visited)
                visited = visited+[vertice]
                print("Visito i suoi adiacents {0}".format(adjacents))
                visited = self.bf_visit_impl(adjacents, visited)
        return visited
    def __str__(self):
        return self.bf_visit()

if __name__=='__main__':
    graph = Graph({"sandra","francesco","andrea"},{("sandra","francesco")})
    graph.insert_node("kerstin")
    graph.insert_node("gabriele")
    graph.insert_relation("kerstin","gabriele")
    graph.insert_relation("gabriele","kerstin")
    graph.insert_relation("francesco", "andrea")
    graph.insert_relation("sandra","andrea")
    print(graph._edges)
    print(graph)
