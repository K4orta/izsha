import urllib2, izsha_config, datetime, json

def fetch_events(url, start_time=None, players=None, time_range=6,):
    query = ""
    if start_time != None:
        range_start = (start_time - datetime.timedelta(hours=time_range)).isoformat()
        range_end = (start_time + datetime.timedelta(hours=time_range)).isoformat()
        query += "?startsAt={0}&endsAt={1}".format(range_start, range_end)
    if players != None:
        query += "&teams={0}".format(",".join(players).lower())
    res = urllib2.urlopen(url + query)
    out = res.read()
    print(query)
    return json.loads(out)