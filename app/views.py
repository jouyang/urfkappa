from __future__ import division
from flask import jsonify, render_template
from app import app, cursor, champInformation, idToDataName
import json
import query

@app.route('/')
def index():
	return render_template('index.html', champ_list=champInformation.items())

@app.route('/stats/<id1>/<id2>')
def winpercent(id1,id2):
	if not (id1.isdigit() and id2.isdigit()):
		data = {"error": "Parameters are not digits"}
		return jsonify(data)

	if (id1 not in idToDataName or id2 not in idToDataName):
		data = {"error": "Champion ID not valid"}
		return jsonify(data)

	champID1 = int(id1)
	champID2 = int(id2)
	statistic = calculate_raw_win_rate(champID1,champID2)
	return jsonify(statistic)

def get_relevant_games(id1,id2):
	q = query.form_query(id1,id2)
	print q
	cursor.execute(q);
	data = cursor.fetchall()
	return data

def calculate_raw_win_rate(id1,id2):
	urf_matches = get_relevant_games(id1,id2)

	if (len(urf_matches)==0):
		return {"error":"No matches found"}

	champ1_name = champInformation[idToDataName[str(id1)]]["name"]
	champ2_name = champInformation[idToDataName[str(id2)]]["name"]
	total_matches = len(urf_matches)
	champ1_win_counter = 0
	skipped_matches = 0
	for match in urf_matches:
		team1 = json.loads(match[1])
		team2 = json.loads(match[2])
		winner = int(match[13])

		#check for cases of [id1,id2,3,4,5] vs [id1,id2,3,4,5], we don't count in win rate
		if all(x in team1 for x in [id1, id2]) and all(x in team2 for x in[id1, id2]):
			skipped_matches += 1
			continue

		if (winner==100) and (id1 in team1) and (id2 in team2):
			champ1_win_counter +=1
		elif (winner==200) and (id1 in team2) and (id2 in team1):
			champ1_win_counter +=1

	champ1_win_rate = champ1_win_counter/(total_matches - skipped_matches)
	stats = {"champ1_id": id1,
			 "champ2_id": id2,
			 "champ1_name": champ1_name,
			 "champ2_name": champ2_name,
			 "champ1_win_counter": champ1_win_counter,
			 "champ2_win_counter": total_matches - skipped_matches - champ1_win_counter,
			 "champ1_win_rate": champ1_win_rate,
			 "champ2_win_rate": 1.0-champ1_win_rate,
			 "total_matches": total_matches,
			 "uncounted_matches": skipped_matches}
	return stats

