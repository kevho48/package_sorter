class PackageSorter:

	def sort(
			self, 
			width: int, 
			height: int, 
			length: int, 
			mass: int
		)-> str:
		is_bulky = self._isBulky(width, height, length)
		is_heavy = self._isHeavy(mass)

		if is_bulky and is_heavy:
			return "REJECTED"

		if is_bulky or is_heavy:
			return "SPECIAL"
	
		return "STANDARD"

	@staticmethod
	def _isBulky(width: int, height: int, length: int) -> bool:
		return (
			width >= 150 
			or height >= 150 
			or length >= 150 
			or (width * height * length >= 1000000)
		)

	@staticmethod
	def _isHeavy(mass: int) -> bool:
		return mass >= 20

