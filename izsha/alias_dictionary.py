import os, yaml

class AliasDictionary:
	def __init__(self, config_url):
		self.__players = {}
		self.load_dictionary(config_url)

	def get_player(self, key):
		if key in self.__players:
			return self.__players[key]
		else:
			return key

	def load_dictionary(self, config_url):
		stream = open(config_url, 'r')
		self.__players = yaml.load(stream)['aliases']
		



