import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import izsha, izsha_config

def setup_module(module):
	module.event = izsha.Event('2013-06-20T13:00:00+00:00', '2013-06-20T13:00:00+00:00')

def test_event_creation():
	event.title = "abc"
	assert event.start_time.year == 2013
	assert event.title == "abc"

def test_has_players():
	event.set_teams(['Stephano', 'TLO', 'Grubby', 'ToD'])
	assert event.has_teams(['ToD', 'Grubby']) == True
	assert event.has_teams(['ToD', 'TLO']) == True
	assert event.has_teams(['ToD', 'Sky']) == False

