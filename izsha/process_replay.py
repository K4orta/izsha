# on getting a replay
#     izsha should parse it to get its date and players
#     then get a list of events that happened arround that time
#     izsha should find the event that the replay belongs to 
#     and move the file into the correct directory in the WCS folder
#     the processed file should be removed from the unsorted directory
#     if there is an error in this process, the replay should be left in the unsorted folder
import sc2reader, event_api, izsha_config
from game import Game

def process_replay(path):
	game = time_and_players(path)
	event = filter_events(event_api.fetch_events(izsha_config.event_api_url, game["start_time"], game["players"]), game)
	print(path)
	return event

def filter_events(events, game):
	# remove events that don't contain both players
	filtered = [event for event in events if event.has_teams(game.players)]
	# remove events when the game is played before the event starts
	filtered = [event for event in filtered if event.start_time < game.start_time]
	# if more than one event is left, find the one that started closest to when the game was played
	if len(filtered) > 1:
		selected = filtered[0]
		lowest = float("inf")
		for ev in filtered:
			cur_delta = abs((ev.start_time - game.start_time).total_seconds())
			if cur_delta < lowest:
				lowest = cur_delta
				selected = ev
		filtered = [selected]
		
	return filtered

def has_all_teams(search_ar, teams):
	expected_matches = len(teams)

	return expected_matches

def time_and_players(path):
	replay = sc2reader.load_replay(path)
	game = {
		"start_time": replay.start_time,
		"end_time": replay.end_time,
		"players": [replay.players[0].name, replay.players[1].name]
	}
	
	return Game([replay.players[0].name, replay.players[1].name], replay.start_time, replay.end_time, [player.uid for player in replay.players])