# on getting a replay
#     izsha should parse it to get its date and players
#     then get a list of events that happened arround that time
#     izsha should find the event that the replay belongs to 
#     and move the file into the correct directory in the WCS folder
#     the processed file should be removed from the unsorted directory
#     if there is an error in this process, the replay should be left in the unsorted folder
import sc2reader, event_api, izsha_config, os
from game import Game
from locate_directory import find_matchup_folder

def process_replay(path):
	game = time_and_players(path)
	if game == None:
		return None;
	event = filter_events(event_api.fetch_events(izsha_config.event_api_url, game.start_time, game.players), game)
	if len(event) < 1:
		return None
	print event[0].title
	dest_folder = find_matchup_folder(game, event[0])
	err = move_replay(path, dest_folder)
	return event

def move_replay(src, dest):
	dest_file = os.path.join(dest, os.path.basename(src))
	os.rename(src, dest_file)
	return None

def filter_events(events, game):
	# remove events that don't contain both players
	print("players: {0}".format(game.players))
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
	# print("Found {0} with the tags {1}".format(filtered[0].title, filtered[0].tags))
	return filtered

def has_all_teams(search_ar, teams):
	expected_matches = len(teams)

	return expected_matches

def time_and_players(path):
	if os.path.exists(path):
		replay = sc2reader.load_replay(path)
		return Game([replay.players[0].name, replay.players[1].name], 
			replay.start_time, 
			replay.end_time, 
			[player.uid for player in replay.players],
			replay.winner.players[0].name
			)
	return None