import os, izsha_config
from game import Game
from event import Event

# find the right folder to put a replay file
def find_matchup_folder(game, event):
	event_path = find_tag(izsha_config.abathur_root, event.tags)
	dest_folder = find_set(izsha_config.abathur_root, event_path)
	return dest_folder

def find_set(root_dir, event_tags):
	event_path = os.path.join(root_dir,*event_tags)
	sets = os.listdir( os.path.join(event_path, ))
	set_num = 1
	set_dir = "set{0}".format(set_num)
	os.mkdir(os.path.join( event_path, set_dir))
	return os.path.join( event_path, set_dir)

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
