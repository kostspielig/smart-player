
# with hexagons numbering the directions 0 = N, 1 = NE, 2 = NO, 3 = S, 4 = SE, 5 = SO

class Node:

    def __init__(self, pos=[1,1], parent):
        self.pos = pos
        self.parent = parent
        self.h = distance(self.pos, pos_f)
        # pos_f is a final position which is declared globally

        if self.parent == None:
            self.g = 0
        else:
            self.g = self.parent.g + 1
        self.f = self.g + self.h


def distance (a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 

class AStar:
	def __init__(self, map, start, end):
		
            self.map = map
            globals()["pos_f"] = buscarPos(3, self.mapa)

            # Nodes start and end.
            self.start = start
            self.end = end

            # Create open and close lists.
            self.open = []
            self.close = []
		
            # Includes to the close list the initial node.
            self.close.append(self.start)
		
            # Includes neighbors to the open list
            self.open += self.neighbors(self.start)
		
            # Buscar mientras objetivo no este en la lista close.
            while self.objetivo():
                if not self.open:
                    break
                self.buscar()
		
            if not self.open:
                self.path = -1
            else:	
		self.path = self.path()
        
	
	# Devuelve una lista con los nodes neighbors transitables.	
	def neighbors(self, node):
		neighbors = []

                if validPosition(node.pos[0], node.pos[1]-1) == True:
                    neighbors.append( Node([node.pos[0], node.pos[1]-1], node) )
                if validPosition(node.pos[0], node.pos[1]+1) == True:
                    neighbors.append( Node([node.pos[0], node.pos[1]+1], node) )
                if validPosition(node.pos[0]+1, node.pos[1]-1) == True:
                    neighbors.append( Node([node.pos[0]+1, node.pos[1]-1], node) )
                if validPosition(node.pos[0]+1, node.pos[1]) == True:
                    neighbors.append( Node([node.pos[0]+1, node.pos[1]], node) )
                if validPosition(node.pos[0]-1, node.pos[1]-1) == True:
                    neighbors.append( Node([node.pos[0]-1, node.pos[1]-1], node) )
                if validPosition(node.pos[0]-1, node.pos[1]) == True:
                    neighbors.append( Node([node.pos[0]-1, node.pos[1]], node) )
                    
		return neighbors
                                      
        def validPosition(self, x, y):
            if
            return True
                                      
	# Pasa el elemento de f menor de la lista open a la close. 	
	def smallerF(self):
		a = self.open[0]
		n = 0
		for i in range(1, len(self.open)):
			if self.open[i].f < a.f:
				a = self.open[i]
				n = i
		self.close.append(self.open[n])
		del self.open[n]
		
	
	# Comprueba si un nodo está en una lista.	
	def inList(self, nodo, lista):
		for i in range(len(lista)):
			if nodo.pos == lista[i].pos:
				return 1
		return 0
	
	
	# Gestiona los neighbors del nodo seleccionado.	
	def route(self):
		for i in range(len(self.nodes)):
			if self.inList(self.nodes[i], self.close):
				continue
			elif not self.inList(self.nodes[i], self.open):
				self.open.append(self.nodes[i])
			else:
				if self.select.g+1 < self.nodes[i].g:
					for j in range(len(self.open)):
						if self.nodes[i].pos == self.open[j].pos:
							del self.open[j]
							self.open.append(self.nodes[i])
							break
	
	# Analiza el último elemento de la lista close.
	def buscar(self):
		self.smallerF()
		self.select = self.close[-1]
		self.nodes = self.neighbors(self.select)
		self.route()
	
	# Comprueba si el objetivo está en la lista open.
	def objetivo(self):
		for i in range(len(self.open)):
			if self.end.pos == self.open[i].pos:
				return 0
		return 1
	
	# Retorna una lista con las posiciones del path a seguir.
	def path(self):
		for i in range(len(self.open)):
			if self.end.pos == self.open[i].pos:
				objetivo = self.open[i]
				
		path = []
		while objetivo.parent != None:
			path.append(objetivo.pos)
			objetivo = objetivo.parent
		path.reverse()
		return path

# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

# Devuelve la posición de "x" en una lista.
def buscarPos(x, mapa):
	for f in range(len(mapa)):
		for c in range(len(mapa[0])):
			if mapa[f][c] == x:
				return [f, c]
	return 0

# ---------------------------------------------------------------------

def main():
	
	return 0

if __name__ == '__main__':
	main()
