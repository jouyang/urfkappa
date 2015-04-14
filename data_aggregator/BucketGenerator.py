import requests
from time import gmtime

required_payload = {'api_key': 'a1dd0a0a-5b05-41be-85d1-6efc4ea04f79'}
root_url = "https://na.api.pvp.net/"

def merge_dicts(*dict_args):
    result = {}
    for dictionary in dict_args:
        result.update(dictionary)
    return result

class BucketGenerator:
	challenge_api_suffix = "api/lol/na/v4.1/game/ids"
	begin_slot = 1427865900
	current_slot = 1427865900
	challenge_payload = {}

	def __init__(self):
		self.challenge_payload["beginDate"] = self.begin_slot

	def increment_time_slot(self):
		self.current_slot += 300
		self.challenge_payload["beginDate"] = self.current_slot

	def reset_time_slot(self):
		self.current_slot = self.begin_slot
		self.challenge_payload["beginDate"] = self.current_slot

	#Returns list of game id's
	def get_bucket(self):
		req = requests.get(root_url + self.challenge_api_suffix, params=merge_dicts(required_payload, self.challenge_payload))
		self.increment_time_slot()
		return req.text

