import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import izsha, izsha_config

def setup_module(module):
	module.akas = izsha.AliasDictionary(izsha_config.alias_dictionary)

def test_dictionary():
	assert akas.get_player('SoulKey') == 'Soulkey' 
