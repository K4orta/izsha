import os, izsha_config
from game import Game
from event import Event

def find_matchup():
	pass


def find_tag(root_path, tags, proper_path=()):
	if tags == None or len(tags) < 1:
		return proper_path 
	for f_obj in os.listdir(root_path):
		if os.path.isdir(os.path.join(root_path, f_obj)) and f_obj in tags:
			proper_path += (f_obj,)
			tags.remove(f_obj)
			return find_tag(os.path.join(root_path, f_obj), tags, proper_path)
	print "Couldn't find tag"
	return proper_path
