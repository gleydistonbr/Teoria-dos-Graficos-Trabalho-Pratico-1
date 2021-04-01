

# Implementação dos métodos básicos #

  def isRegular(self):
    adj_vertex = []
    for vertex in self.vertList:
      adj_vertex.append(len(vertList))
      if len(set(len_adj_vertices)) > 1:
        return False
    return

  def isCompleted(self):
    graphSize = len(self.vertList)
    print(graphSize)
    for vertex in self.vertList:
      if len(vertList != graphSize):
        return False
    return

  def isConnected(self):
    self.bfs(self.vertList[0])
    for vertex in self.vertList:
      if vertex.visited == False:
        print(f'{vertex} Visitado: {vertex.visited}')
        return False
    return

# Implementação do método de busca BFS #

  def bfs(self, vertice):
      vertexRow = []
      vertex.visited = True
      vertexRow.append(vertice)

      while len(vertexRow):
        u = vertexRow[0]

        vertexRow.pop(0)

        for w in u.arestas:
          if w.visited == False:
            w.visited = True
            vertexRow.append(w)
        print(vertexRow)



# Representação do grafo

print(G) 

print(G.isRegular())
print(G.isCompleted())
print(G.isConnected())
print(G.bfs(G.vertexs[0]))