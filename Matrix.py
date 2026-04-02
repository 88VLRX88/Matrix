class Matrix:
	def __init__(self, matrixSize: list):
		self.matrixSize = matrixSize
		self.matrix = []
		self.vertexProperties = {}


	def createMatrix(self):
		bufArray = []

		for i in range(self.matrixSize):
			for j in range(self.matrixSize):
				bufArray.append(0)
			self.matrix.append(bufArray)
			bufArray = []

		return self.matrix


	def vertexSetProperties(self, vertexProperties: list):
		lenOfVertexesName = len(vertexProperties)
		for i in range(lenOfVertexesName):
			self.vertexProperties[i] = vertexProperties[i]
		return self.vertexProperties


	def marking(self, intersections: list):
		for i in intersections:
			self.matrix[i[0]][i[1]] = i[2]

		return self.matrix
	
	
	def arranging(self, currentVertex: int, intersectionTypes=[1,2,3,4]):
		arranging = []
		wasIntersection = [currentVertex]
		hasIntersection = [currentVertex]
		bufHasIntersection = []
		while hasIntersection != []: 
			arranging.append(hasIntersection)
			for i in range(0, self.matrixSize):
				if i in hasIntersection:
					for j in range(0, self.matrixSize):
						if self.matrix[i][j] in intersectionTypes and not j in wasIntersection:
							wasIntersection.append(j)
							bufHasIntersection.append(j)

			hasIntersection = bufHasIntersection
			bufHasIntersection = []
		
		return arranging


	def specification(self, intersectionTypes=[1,2,3,4,5]):
		specification = []
		bufSpecification = []
		for i in range(0, self.matrixSize):
			for j in range(0, self.matrixSize):
				if self.matrix[i][j] in intersectionTypes:
					bufSpecification.append(j)
			specification.append(bufSpecification)
			bufSpecification = []
		return specification
									

	def showSpecification(self, arranging: list, specification: list, showVertexesName=False):
		level = 0
		lenOfSpecification = len(specification)
		for i in range(0, lenOfSpecification):
			for j in arranging:
				if i in j:
					if showVertexesName:
						print(f"{level} -", end=' ')
						for n in specification[i]: 
							print(f"{self.vertexProperties[n]['Name']} |", end=' ')
						print('\n', end='')
					else: print(f"{level} - {specification[i]}")
				level = level + 1
			level = 0


	def showMatrix(self):
		for i in self.matrix:
			for j in i:
				print(j, end=' ')
			print('\n', end='')


	def showArranging(self, arranging: list, showVertexesName=False):
		lenOfArranging = len(arranging)
		for i in range(lenOfArranging):
			if showVertexesName:
				print(f"{i} - ", end='')
				for j in arranging[i]: 
					print(f"{self.vertexProperties[j]['Name']} |", end=' ')
				print()
			else:
				print(f"{i} - {arranging[i]}")


	def getProperties_wr(self, request: str):
		responce = []
		responceField = {}
		request = request.split('?')
		request[0] = request[0].split('|')
		request[0] = list(map(int, request[0]))
		request[1] = request[1].split('|')
		for i in range(0, self.matrixSize):
			if i in request[0]:
				for j in self.vertexProperties[i].keys():
					if '*' in request[1]: responceField[j] = self.vertexProperties[i][j]
					elif j in request[1]: responceField[j] = self.vertexProperties[i][j]
				responce.append(responceField)
				responceField = {}
		return(responce)
	
					 
	def setProperties_wr(self, request: str):
		responce = []
		request = request.split('!')
		request[0] = request[0].split('|')
		request[0] = list(map(int, request[0]))
		request[1] = request[1].split('|')
		lenOfValues = len(request[1])
		for i in range(lenOfValues):
			request[1][i] = request[1][i].split('=')
		for i in range(0, self.matrixSize):
			if i in request[0]:
				for j in request[1]:
					if j[1].startswith("i'"): self.vertexProperties[i][j[0]] = int(j[1][2:])
					elif j[1].startswith("s'"): self.vertexProperties[i][j[0]] = j[1][2:] 		
				responce.append(self.vertexProperties[i])
		return(responce)

