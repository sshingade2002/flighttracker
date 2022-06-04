import requests
import json
import datetime
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="MyApp")
ICAO24HEX = 'A64A73'
params = {
  'api_key': '', # api key goes here
  'params1': 'value1',
  'hex': ICAO24HEX
}

api_base = 'https://airlabs.co/api/v9/flights'

api_result = requests.get(api_base, params)
api_response = api_result.json()

coordinates = api_response['response'][0]['lat'], api_response['response'][0]['lng']
curr_time = datetime.datetime.fromtimestamp(api_response['response'][0]['updated'])

location = geolocator.reverse(coordinates)
address = location.raw['address']
city = address.get('city', '')
state = address.get('state', '')
country = address.get('country', '')

print('flight '+ICAO24HEX+' is in '+city+', '+state+' '+country+' at '+str(curr_time))