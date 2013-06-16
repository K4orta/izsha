class Event:
	def __init__(self):
		self.__id = None
		self.title = ""
		self.__teams = []
		self.__tags = []

	@property
	def tags(self):
		return self.__tags

	@tags.setter
	def tags(self, tags):
		self.__tags = tags