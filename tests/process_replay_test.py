import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import izsha, izsha_config

def setup_module(module):
	module.game = izsha.time_and_players("tests/replays/Akilon Wastes Semi Final match 1 3set.SC2Replay")

def test_game_parse():
	assert game["start_time"].isoformat() == "2013-06-09T01:49:02"
	assert game["end_time"].isoformat() == "2013-06-09T02:05:51"
	assert game["players"][0] == "sOs"
	assert game["players"][1] == "SoulKey"

def test_event_api(httpserver):
	httpserver.serve_content(open('tests/stubs/events.json').read())
	events = izsha.fetch_events(httpserver.url, game["start_time"], game["players"])
	assert len(events) == 5