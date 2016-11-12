class Graph():

	def __init__(self, new_graph: "dictionary of vertices" = {}):
		Graph.check_graph(new_graph) #checking new graph for a mutual connectivity of vertices

		self.__graph = new_graph

	def __str__(self):
		"""returns string representation of a graph"""
		str_rep = ""

		for node in self.__graph.keys():
			str_rep += str(node) + ": "

			if not self.__graph[node]:
				str_rep += "<isolated>"
			else:
				for vertex in self.__graph[node]:
					str_rep += str(vertex) + " "

			str_rep += '\n'

		return str_rep

	@staticmethod
	def check_graph(graph):
		"""checks a graph for mutual connectivity of vertices and for the """
		if type(graph) != dict:
			raise TypeError("Graph must be represented as a dictionary")

		for node in graph.keys():
			if type(graph[node]) != list:
				raise TypeError("Neighbours must be represented as a list; first detected disparity under a key " + str(node))

		for node in graph.keys():
			for neighbour in graph[node]:
				if neighbour not in graph.keys():
					raise ValueError("Vertex " + str(neighbour) + " that is connected with " + str(node) + "does not consist")
				if node not in graph[neighbour]:
					raise ValueError("Vertex " + str(node) + " is connected with " + str(neighbour) + ", but " + str(neighbour) + " is not connected with " + str(node))

	@staticmethod
	def check_edge(edge: "tuple of 2 vertices"):
		if type(edge) != tuple:
			raise TypeError("Edge must be represented as a tuple with 2 vertices")

		if not edge:
			raise ValueError("Vertices are not specified")

		if len(edge) != 2:
			raise ValueError("Edge can connect only 2 vertices")

	@property
	def graph(self):
		"""returns an implicit representation of a graph"""
		return self.__graph
	
	def edges(self):
		"""returns a list of edges; each edge is represented as a tuple of 2 mutually connected vertices"""
		if not self.__graph:
			raise AttributeError("Graph is empty")

		edges = []

		for node in self.__graph.keys():
			for neighbour in self.__graph[node]:
				edges.append((node, neighbour))

		return edges

	def isolated_vertices(self):
		"""returns a list of vertices that are not connected to some others"""
		if not self.__graph:
			raise AttributeError("Graph is empty")

		isolated = []

		for node in self.__graph:
			if not self.__graph[node]:
				isolated.append(node)

		return isolated

	def vertices(self):
		"""returns a list of all vertices"""
		if not self.__graph:
			raise AttributeError("Graph is empty")

		return list(self.__graph.keys())

	def add_vertex(self, vertex: "unmutable", neighbours: "list of vertices" = []):
		"""adds new vertex and its neighbours
connects new vertex with already presented vertices if it is necessary
new vertex must not be in vertices that are already presented in graph"""
		if vertex in self.__graph.keys():
			raise ValueError("Vertex " + str(vertex) + " is alredy in the graph")

		if type(neighbours) != list:
			raise TypeError("Neighbourhood must be represented as a list")

		self.__graph[vertex] = neighbours

		for neighbour in self.__graph[vertex]:
			if neighbour in self.__graph.keys():
				self.__graph[neighbour].append(vertex)
			else:
				self.__graph[neighbour] = [vertex]

	def add_edge(self, edge: "tuple of 2 vertices"):
		"""adds an edge represented as a tuple of 2 vertices in a graph"""
		Graph.check_edge(edge)

		if edge[0] in self.__graph.keys() and edge[1] not in self.__graph.keys():
			self.add_vertex(edge[1], [edge[0]])
		elif edge[0] in self.__graph.keys() and edge[1] in self.__graph.keys():
			if edge[0] in self.__graph[edge[1]] and edge[1] in self.__graph[edge[0]]:
				raise ValueError("Edge " + str(edge) + " is already in the graph")

			self.__graph[edge[1]].append(edge[0])
			if edge[1] not in self.__graph[edge[0]]: #for pseudographs
				self.__graph[edge[0]].append(edge[1])
		elif edge[0] not in self.__graph.keys() and edge[1] in self.__graph.keys():
			self.add_vertex(edge[0], [edge[1]])
		elif edge[0] not in self.__graph.keys() and edge[1] not in self.__graph.keys():
			self.__graph[edge[1]] = [edge[0]]
			self.__graph[edge[0]] = [edge[1]]

	def add_graph(self, added_graph: "dictionary (use method graph() for objects)", connecting_edge: "tuple of 2 vertices" = None):
		"""concatenates 2 graphs; they can be isolated from each other or have common edge connecting_edge"""
		if connecting_edge:
			Graph.check_edge(connecting_edge)

		if connecting_edge and connecting_edge[0] == connecting_edge[1]:
			raise ValueError("Incorrect value for connecting edge")

		Graph.check_graph(added_graph)

		for node in added_graph.keys():
			if node in self.__graph.keys():
				raise ValueError("The vertex " + str(node) + " of added graph is already in the calling graph")
		for node in self.__graph.keys():
			if node in added_graph.keys():
				raise ValueError("The vertex " + str(node) + " of calling graph is already in the added graph")

		for node in added_graph.keys():
			self.__graph[node] = added_graph[node]

		if connecting_edge:
			if not ((connecting_edge[0] in self.__graph.keys() and connecting_edge[1] in added_graph.keys()) or (connecting_edge[1] in self.__graph.keys() and connecting_edge[0] in added_graph.keys())): #condition was checked mathematecally
				raise ValueError("Specified connecting edge " + str(connecting_edge) + " can't exist in ")

			self.add_edge(connecting_edge)

if __name__ == "__main__":
	g = {
	"a" : ["d"],
	"b" : ["c"],
	"c" : ["b", "c", "d", "e"],
	"d" : ["a", "c"],
	"e" : ["c"],
	"f" : []
	}

	grph = Graph(g)

	print(grph.edges())
	print(grph.graph)
	print(grph.isolated_vertices())

	grph.add_vertex("g", ["c", "b"])
	print(grph.edges())

	grph.add_edge(("c", "a"))
	print(grph.edges())

	grph.add_edge(("b", "b"))
	print(grph.edges())
	print(grph.graph)

	grph.add_edge(("c", "l"))
	print("lol", grph.graph)

	grph.add_edge(("k", "a"))
	print("lel", grph.graph)

	grph.add_edge(("v", "m"))
	print("lal", grph.graph)

	print(grph)

	gr = {
	1 : [2],
	2 : [1, 3, 4],
	4 : [2, 5, 6],
	3 : [2, 7],
	7 : [3],
	5 : [4],
	6 : [4]
	}

	grph.add_graph(gr, (1, "f"))
	print(grph)

