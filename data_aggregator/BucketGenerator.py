import requests
import key
import ast
import time

required_payload = {'api_key': key.api_key()}
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
	end_slot = 1428890400
	challenge_payload = {}

	def __init__(self):
		self.challenge_payload["beginDate"] = self.begin_slot

	def increment_time_slot(self):
		self.current_slot += 300
		self.challenge_payload["beginDate"] = self.current_slot

	def reset_time_slot(self):
		self.current_slot = self.begin_slot
		self.challenge_payload["beginDate"] = self.current_slot

	def reach_end(self):
		return (self.current_slot >= self.end_slot)

	#Returns list of game id's
	def get_bucket(self):
		req = requests.get(root_url + self.challenge_api_suffix, params=merge_dicts(required_payload, self.challenge_payload))

		while(req.status_code !=200):
			time.sleep(10)
			req = requests.get(root_url + self.challenge_api_suffix, params=merge_dicts(required_payload, self.challenge_payload))

		self.increment_time_slot()
		game_ids = [item for item in ast.literal_eval(req.text)]
		return game_ids


