class RandomChikibum:
	def fab(self,n):
		if n == 0:
			return 0
		if n == 1:
			return 1
		return self.fab(self,n-1) + self.fab(self,n-2)

myObj = RandomChikibum()
myObj.fab(5)
