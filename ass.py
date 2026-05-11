import urllib.request, urllib.parse
import json

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo?'

address = input('Enter location: ')
params = dict()
params['q'] = address

url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()

print('Retrieved', len(data), 'characters')

js = json.loads(data)

plus = js['features'][0]['properties']['plus_code']

if isinstance(plus, dict):
    plus_code = plus.get('compound_code', '')
else:
    plus_code = plus

print('Plus code', plus_code)