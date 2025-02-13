import urllib.request as request
import json
link= "https://data.europa.eu/api/hub/repo/distributions/12aa6500-ec65-49bb-b8d4-1b02f7731e78.jsonld"
with request.urlopen(link) as resp:
    data=json.load(resp)
print(data)


