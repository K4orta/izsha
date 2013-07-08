import urllib2, izsha_config, datetime, json
from event import Event

def fetch_events(url, start_time=None, players=None, time_range=12):
    query = ""
    if start_time != None:
        range_start = (start_time - datetime.timedelta(hours=time_range)).isoformat()
        range_end = (start_time + datetime.timedelta(hours=time_range)).isoformat()
        query += "?startsAt={0}&endsAt={1}".format(range_start, range_end)
    if players != None:
        query += "&teams={0}".format(",".join(players).lower())
    print(url + query)
    res = urllib2.urlopen(url + query)
    out = res.read()
    print "got {0} events".format(len(json.loads(out)))
    return [event_factory(ev) for ev in json.loads(out)]

def event_factory(raw_event):
    new_event = Event(raw_event['starts_at'], raw_event['ends_at'])
    new_event.title = raw_event['title']
    new_event.set_teams([player['name'] for player in raw_event['teams']])
    print("possible players: {0}".format(new_event.teams))
    new_event.set_tags(raw_event['tags_array'])
    return new_event