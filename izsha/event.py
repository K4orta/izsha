import datetime, dateutil.parser

class Event:
	def __init__(self, start_time, end_time):
		self.id = None
		self.title = ""
		self.start_time = dateutil.parser.parse(start_time).replace(tzinfo=None)
		self.end_time = dateutil.parser.parse(end_time).replace(tzinfo=None)
		self.__teams = []
		self.__team_lookup = {}
		self.__tags = []

	def has_teams(self, players):
		for player in players:
			if not player in self.__team_lookup:
				return False

		return True

	@property
	def tags(self):
		return self.__tags

	def set_tags(self, tags):
		self.__tags = tags

	@property
	def teams(self):
		return self.__teams

	def set_teams(self, teams):
		self.__teams = teams
		self.__team_lookup = { team_name: team_name for team_name in teams }