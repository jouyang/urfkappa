from flask import Flask, jsonify, render_template
from flask.ext.sqlalchemy import SQLAlchemy
import key
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:%s@127.0.0.1/urfkappa' % key.passw()
db = SQLAlchemy(app)

@app.route('/')
def index():
	json_data = open("champ_data.json", "r")
	data = json.load(json_data)
	return render_template('index.html', champ_list=data.items())

@app.route('/data')
def names():
    data = {
        "first_names": ["John", "Jacob", "Julie", "Jennifer"],
        "last_names": ["Connor", "Johnson", "Cloud", "Ray"]
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
