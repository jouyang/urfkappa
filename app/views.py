from flask import jsonify, render_template
from app import app, champInformation, idToDataName
from UrfStatsAggregator import calculate_raw_win_rate

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

