"""

1. ford-fulkerson
2. TSP
3. ???
4. rework djikstra and a* to be more similar.
5. rework floyd_warshall so that output is tabular. it sucks right now.

exec(open('/home/duchess/Desktop/graphs').read())

THE ONE BELOW IS FOR FLOYD-WARSHALL.

g = Graph()
g.addEdge(1, 3, -2)
g.addEdge(2, 1, 4)
g.addEdge(2, 3, 3)
g.addEdge(3, 4, 2)
g.addEdge(4, 2, -1)

THE ONE BELOW IS FOR BELLMAN-FORD.

g = Graph()
g.addEdge('S', 'E', 8)
g.addEdge('S', 'A', 10)
g.addEdge('E', 'D', 1)
g.addEdge('D', 'A', -4)
g.addEdge('D', 'C', -1)
g.addEdge('C', 'B', -2)
g.addEdge('A', 'C', 2)
g.addEdge('B', 'A', 1)

THE ONE BELOW IS FOR A-STAR.

g = Graph()
g.addEdge((0,0), (0,1), 1)
g.addEdge((0,0), (1,0), 1)
g.addEdge((1,0), (0,0), 1)
g.addEdge((1,0), (1,1), 1)
g.addEdge((1,0), (2,0), 1)
g.addEdge((2,0), (1,0), 1)
g.addEdge((2,0), (2,1), 1)
g.addEdge((0,1), (0,0), 1)
g.addEdge((0,1), (0,2), 1)
g.addEdge((0,1), (1,1), 1)
g.addEdge((1,1), (0,1), 1)
g.addEdge((1,1), (1,2), 1)
g.addEdge((1,1), (2,1), 1)
g.addEdge((1,1), (1,0), 1)
g.addEdge((2,1), (2,0), 1)
g.addEdge((2,1), (1,1), 1)
g.addEdge((2,1), (2,2), 1)
g.addEdge((0,2), (0,1), 1)
g.addEdge((0,2), (1,2), 1)
g.addEdge((1,2), (0,2), 1)
g.addEdge((1,2), (1,1), 1)
g.addEdge((1,2), (2,2), 1)
g.addEdge((2,2), (1,2), 1)
g.addEdge((2,2), (2,1), 1)

THE ONE BELOW IS FOR DJIKSTRA'S.

g = Graph()
g.addEdge('A', 'B', 4)
g.addEdge('A', 'C', 2)
g.addEdge('B', 'C', 3)
g.addEdge('B', 'D', 2)
g.addEdge('B', 'E', 3)
g.addEdge('C', 'B', 1)
g.addEdge('C', 'D', 4)
g.addEdge('C', 'E', 5)
g.addEdge('E', 'D', 1)

g = Graph()
g.addEdge('A', 'B', 1)
g.addEdge('A', 'C', 5)
g.addEdge('A', 'D', 3)
g.addEdge('B', 'C', 4)
g.addEdge('B', 'D', 2)
g.addEdge('C', 'D', 1)

THE ONE BELOW IS FOR TOPO_SORT TESTING.

g = Graph()
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

g = Graph()
g.addEdge('A','B',2)
g.addEdge('A','C',3)
g.addEdge('B','C',1)
g.addEdge('B','D',1)
g.addEdge('B','E',4)
g.addEdge('D','E',1)
g.addEdge('E','F',1)
g.addEdge('C','F',5)
g.addEdge('F','G',1)

g = Graph()
g.addEdge(0,1,5)
g.addEdge(0,5,2)
g.addEdge(1,2,4)
g.addEdge(2,3,9)
g.addEdge(3,4,7)
g.addEdge(3,5,3)
g.addEdge(4,0,1)
g.addEdge(5,4,8)
g.addEdge(5,2,1)

g = Graph()
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3)
g.addEdge(3, 3)

"""

from collections import deque, defaultdict
from heapq import *
import itertools
import sys

class Vertex(object):

    def __init__(self, value):
        self.value = value
        self.neighbors = {}

    def __repr__(self):
        return str(self.value) + '--> ' + str([x.value for x in self.neighbors])

    def addNeighbor(self, neighbor, weight=0):
        self.neighbors[neighbor] = weight

    def getWeight(self, neighbor):
        return self.neighbors[neighbor]

class Graph(object):

    def __init__(self):
        self.vertices = {}

    def __iter__(self):
        return iter(self.vertices.values())

    def __repr__(self):
        g = ("(" + str(v.value) + ", " + str(w.value) + ")" for v in self for w in v.neighbors)
        return "\n".join(g)

    def __contains__(self, n):
        return n in self.vertices

    def addVertex(self, value):
        vertex = Vertex(value)
        self.vertices[value] = vertex
        return vertex

    def addEdge(self, v1, v2, cost=0):
        if v1 not in self.vertices:
            v3 = self.addVertex(v1)
        if v2 not in self.vertices:
            v3 = self.addVertex(v2)
        self.vertices[v1].addNeighbor(self.vertices[v2], cost)

    def getVertex(self, n):
        if n in self.vertices:
            return self.vertices[n]

    def bfs(self, start):
        # NOTE: for disconnected graphs, not all nodes are reachable from an arbitrary node. Call function on each node.
        # NOTE: Can also use a heap instead of a queue, to simulate a priority queue. Not necessary, though.
        visited = []
        queue = deque()
        v_start = self.getVertex(start)
        queue.append(v_start)

        while queue:
            current = queue.popleft()
            visited.append(current)
            for v in current.neighbors:
                if v not in visited and v not in queue:
                    queue.append(v)
        return [v.value for v in visited]

    def dfs(self, start):
        # NOTE: Alternative is to use the path list to check whether node was visited. Sets have fast lookups, so more space means less time.
        visited = set()
        path = []
        v_start = self.getVertex(start)
        stack = [v_start]

        while stack:
            v = stack.pop()
            if v not in visited:
                visited.add(v)
                path.append(v)
                stack.extend(n for n in v.neighbors)
        return [v.value for v in path]

    def dfs_recursive(self, start):
        visited = set()
        path = []

        v_start = self.getVertex(start)
        visited.add(v_start)
        path.append(v_start.value)

        def recursive_helper(node):
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    path.append(neighbor.value)
                    recursive_helper(neighbor)

        recursive_helper(v_start)
        return path

    def topological_sort(self):
        # NOTE: This is very similar to dfs_recursive.
        visited = set()
        path = deque()

        def recursive_helper(node):
            for neighbor in node.neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    recursive_helper(neighbor)
            path.appendleft(node.value)

        for v in self:
            if v not in visited:
                recursive_helper(v)
        return list(path)

    def prim_MST(self, start):
        total = 0
        tiebreak = itertools.count().__next__
        explored = set()
        result = []
        v_start = self.getVertex(start)
        unexplored = [(0, tiebreak(), v_start)]

        while unexplored:
            cost, _, winner = heappop(unexplored)
            if winner not in explored:
                explored.add(winner)
                result.append(winner)
                total += cost
                for neighbor in winner.neighbors:
                    if neighbor not in explored:
                        heappush(unexplored, (winner.getWeight(neighbor), tiebreak(), neighbor))
        return total

    def kruskal_MST(self):
        parent = {}
        rank = {}

        def make_set(v):
            parent[v] = v
            rank[v] = 0

        def find_root(v):
            if parent[v] != v:
                parent[v] = find_root(parent[v])
            return parent[v]

        def union(u, v):
            root_u = find_root(u)
            root_v = find_root(v)
            if root_u != root_v:
                if rank[root_u] > rank[root_v]:
                    parent[root_v] = root_u
                else:
                    parent[root_u] = root_v
                    if rank[root_u] == rank[root_v]:
                        rank[root_v] += 1

        for v in self:
            make_set(v)

        MST = set()
        h = []
        tiebreak = itertools.count().__next__
        for v in self:
            for n in v.neighbors:
                heappush(h, (v.getWeight(n), tiebreak(), v, n))
        while h:
            weight, _, u, v = heappop(h)
            if find_root(u) != find_root(v):
                union(u, v)
                MST.add((weight, u, v))
        return MST

    def djikstra(self, start):
        distance = {}
        previous = {}
        unvisited = set(self.vertices.values())

        for v in unvisited:
            distance[v] = sys.maxsize
            previous[v] = None

        v_start = self.getVertex(start)
        distance[v_start] = 0
    
        while unvisited:
            current = min(unvisited, key=lambda v: distance[v])
    
            if distance[current] == sys.maxsize:
                break
    
            for neighbor in current.neighbors:
                alternative_route = distance[current] + current.getWeight(neighbor)
    
                if alternative_route < distance[neighbor]:
                    distance[neighbor] = alternative_route
                    previous[neighbor] = current
    
            unvisited.remove(current)

        min_distances = [(start, node.value, cost) for node, cost in distance.items()]
        min_distances.sort(key=lambda x: x[2])
        return min_distances

    def bellman_ford(self, start):
        # NOTE: BF works on graphs with negative edge weights, unlike Djikstra's.
        # NOTE: BF is inferior to Djikstra's, UNLESS there are negative edge weights.
        # NOTE: BF is NOT greedy, unlike Djikstra's.
        # NOTE: fails for graphs with negative cycles, like Djikstra's.
        # NOTE: Tarjan's Algorithm handles negative cycles, I believe? Check it out.
        
        distance = {}
        parents = {}

        def initialize(self, start):
            d = {}
            p = {}

            for v in self.vertices.values():
                d[v] = sys.maxsize
                p[v] = None

            v_start = self.getVertex(start)
            d[v_start] = 0

            return d, p

        def relax(node, neighbor, self, d, p):
            if d[neighbor] > d[node] + node.getWeight(neighbor):
                d[neighbor] = d[node] + node.getWeight(neighbor)
                p[neighbor] = node

            return node, neighbor, d, p
 
        vertices = self.vertices.values()
        distance, parents = initialize(self, start)

        for i in range(len(self.vertices)-1):
            for v in vertices:
                for n in v.neighbors:
                    v, n, distance, parents = relax(v, n, self, distance, parents)

        return distance, parents

    def a_star(self, start, goal):

        def heuristic(a, b):
            (x1, y1) = a.value
            (x2, y2) = b.value
            return abs(x2 - x1) + abs(y2 - y1)

        v_start = self.getVertex(start)
        v_goal = self.getVertex(goal)
        frontier = []
        tiebreak = itertools.count().__next__
        heappush(frontier, (0, tiebreak(), v_start))
        parent = {}
        previous_cost = {}
        parent[v_start] = None
        previous_cost[v_start] = 0

        while frontier:
            _, _, current = heappop(frontier)

            if current == v_goal:
                break

            for child in current.neighbors:
                new_cost = previous_cost[current] + current.getWeight(child)
                if child not in previous_cost or new_cost < previous_cost[child]:
                    previous_cost[child] = new_cost
                    priority = new_cost + heuristic(v_goal, child)
                    heappush(frontier, (priority, tiebreak(), child))
                    parent[child] = current

        return parent, previous_cost

    def floyd_warshall(self):
        # NOTE: this is the first all-sources SPA. Bellman-Ford, but for ALL nodes.
        # NOTE: you can use a defaultdict(dict) instead of doing nested dictionaries this way...
        
        distance = defaultdict(dict)
        vertices = self.vertices.values()

        for u in vertices:
            for v in vertices:
                if u == v:
                    distance[u][v] = 0
                else:
                    try:
                        distance[u][v] = u.getWeight(v)
                    except KeyError:
                        distance[u][v] = sys.maxsize

        for v_k in vertices:
            for v_i in vertices:
                for v_j in vertices:
                    if distance[v_i][v_j] > distance[v_i][v_k] + distance[v_k][v_j]:
                        distance[v_i][v_j] = distance[v_i][v_k] + distance[v_k][v_j]

        return distance

    def floyd_fulkerson(self):
        # NOTE: This is a max flow problem. Only one of its kind.
        pass
