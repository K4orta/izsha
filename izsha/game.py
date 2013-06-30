from alias_dictionary import AliasDictionary
import izsha_config
class Game:
	aliases = AliasDictionary(izsha_config.alias_dictionary)
	def __init__(self, players, start_time, end_time, bids):
		self.start_time = start_time
		self.end_time = end_time
		self.set_players(players)
		self.player_ids = bids
		print (self.player_ids) 

	@property 
	def players(self):
		return self.__players

	def set_players(self, players):
		self.__players=[Game.aliases.get_player(player) for player in players] 

	@property 
	def start_time(self):
		return self.__start_time

	@start_time.setter
	def start_time(self, time):
		self.__start_time = time

	@property 
	def end_time(self):
		return self.__end_time

	@end_time.setter
	def end_time(self, time):
		self.__end_time = time

