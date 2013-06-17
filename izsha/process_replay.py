# on getting a replay
#     izsha should parse it to get its date and players (use abathur module)
#     then get a list of events that happened arround that time
#     izsha should find the event that the replay belongs to 
#     and move the file into the correct directory in the WCS folder
#     the processed file should be removed from the unsorted directory
#     if there is an error in this process, the replay should be left in the unsorted folder
import sc2reader, event_api, izsha_config

def process_replay(path):
	game = time_and_players(path)
	events = filter_events(event_api.fetch_events(izsha_config.event_api_url, game["start_time"], game["players"]), game)

def filter_events(events, game):
	return []

def time_and_players(path):
	replay = sc2reader.load_replay(path)
	game = {
		"start_time": replay.start_time,
		"end_time": replay.end_time,
		"players": [replay.players[0].name, replay.players[1].name]
	}
	return game