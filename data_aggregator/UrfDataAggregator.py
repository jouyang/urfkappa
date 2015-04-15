# import sys, os
# base_path = os.path.dirname(os.path.basename(__file__))
# sys.path.append(base_path)

import key
import requests
import time
from BucketGenerator import BucketGenerator
from collections import deque
from ..urfkappa import app
import matches

required_payload = {'api_key': key.api_key()}
root_url = "https://na.api.pvp.net/api/lol/na/v2.2/match/"

class UrfDataAggregator:
	bucket = BucketGenerator()
	current_bucket = deque([])

	def __init__(self):
		self.current_bucket = deque(self.bucket.get_bucket())

	def update_bucket(self):
		self.current_bucket = deque(self.bucket.get_bucket())

	def extract_items(self, data):
		items = []
		items.append(data['item0'])
		items.append(data['item1'])
		items.append(data['item2'])
		items.append(data['item3'])
		items.append(data['item4'])
		items.append(data['item5'])
		items.append(data['item6'])
		return items

	def get_match_data(self):
		while(True):
			if(self.bucket.reach_end()):
				return
			else:
				time.sleep(1)
				
			while(not self.current_bucket):
				self.update_bucket()
			
			match_id = self.current_bucket.pop()
			req = requests.get(root_url + str(match_id), params=required_payload)

			while(req.status_code !=200):
				time.sleep(10)
				req = requests.get(root_url + str(match_id), params=required_payload)

			reqJson = req.json()
			players = reqJson['participants']
			if (reqJson['queueType'] == u"URF_5x5"):
				team1_ChampID = []
				team2_ChampID = []
				team1_pnum_to_champ = {}
				team2_pnum_to_champ = {}
				p1_item = []
				p2_item = []
				p3_item = []
				p4_item = []
				p5_item = []
				p6_item = []
				p7_item = []
				p8_item = []
				p9_item = []
				p10_item = []
				winner = "100"
				for p in players:
					
					if (p['teamId'] == 100):
						team1_ChampID.append(p['championId'])
						team1_pnum_to_champ[p['participantId']] = p['championId']
					elif (p['teamId'] == 200):
						team2_ChampID.append(p['championId'])
						team2_pnum_to_champ[p['participantId']] = p['championId']
					
					if (p['participantId'] ==  1):
							p1_item = self.extract_items(p['stats'])
							if (not p['stats']['winner']):
								winner = "200"
					elif (p['participantId'] ==  2):
							p2_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  3):
							p3_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  4):
							p4_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  5):
							p5_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  6):
							p6_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  7):
							p7_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  8):
							p8_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  9):
							p9_item = self.extract_items(p['stats'])
					elif (p['participantId'] ==  10):
							p10_item = self.extract_items(p['stats'])
				team1_ChampID = str(team1_ChampID)
				team2_ChampID = str(team2_ChampID)
				team1_pnum_to_champ = str(team1_pnum_to_champ)
				team2_pnum_to_champ = str(team2_pnum_to_champ)
				p1_item = str(p1_item)
				p2_item = str(p2_item)
				p3_item = str(p3_item)
				p4_item = str(p4_item)
				p5_item = str(p5_item)
				p6_item = str(p6_item)
				p7_item = str(p7_item)
				p8_item = str(p8_item)
				p9_item = str(p9_item)
				p10_item = str(p10_item)
				m = matches.matches(team1_ChampID, team2_ChampID, p1_item, p2_item, p3_item, p4_item, p5_item, p6_item, p7_item, p8_item, p9_item, p10_item, winner, team1_pnum_to_champ, team2_pnum_to_champ)
				app.db.session.add(m)
				app.db.session.commit()


