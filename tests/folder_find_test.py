import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import izsha, izsha_config

def test_find_folder():
	test_tags = ["2013","Season Finals","OGN","Semi-Final","Season 1","WCS"]
	found_folder = izsha.find_tag("tests", test_tags)
	proper_path = ["WCS","2013","Season 1","OGN","Season Finals","Semi-Final"]
	assert list(found_folder) == proper_path

def test_not_enough_tags():
	pass

def test_too_many_tags():
	pass

def test_find_set():
	final_path = izsha.find_set("tests", ["WCS","2013","Season 1","OGN","Season Finals","Semi-Final"])
	assert final_path == "tests/WCS/2013/Season 1/OGN/Season Finals/Semi-Final/set1"

def teardown_module(module):
	os.rmdir(os.path.join("tests", *["WCS","2013","Season 1","OGN","Season Finals","Semi-Final", "set1"]))