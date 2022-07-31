class Solution:
	def __init__(self):
		self.n = 0
		self.m = 0
		self.memory = [[0]]
	def rcsv(self, x, y, M: List[List[int]]):
		if x >= self.n or x < 0:
			return 0
		if self.memory[x][y] != -1:
			return self.memory[x][y]
		if x == self.n - 1:
			self.memory[x][y] = M[x][y]
			return M[x][y]
		if y-1 >= 0:
			left = self.rcsv(x+1, y-1, M)
		else:
			left = 0
		down = self.rcsv(x+1, y, M)
		if y+1 < self.m:
			right = self.rcsv(x+1, y+1, M)
		else:
			right = 0
			
		result = max(left, down, right) + M[x][y]
		self.memory[x][y] = result
		return result
	
	def findMaxPath(self, M: List[List[int]]) -> int:
		# add your logic here
		n = len(M)
		m = len(M[0])
		self.n = n
		self.m = m
		self.memory = [[-1]*m for i in range(n)]
		_max = 0
		for j in range(m):
			_max = max(self.rcsv(0, j, M), _max)
		
		return _max
