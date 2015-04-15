from ..urfkappa.app import db

class matches(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	team1_ChampID = db.Column(db.String(80))
	team2_ChampID = db.Column(db.String(80))
	p1_item = db.Column(db.String(80))
	p2_item = db.Column(db.String(80))
	p3_item = db.Column(db.String(80))
	p4_item = db.Column(db.String(80))
	p5_item = db.Column(db.String(80))
	p6_item = db.Column(db.String(80))
	p7_item = db.Column(db.String(80))
	p8_item = db.Column(db.String(80))
	p9_item = db.Column(db.String(80))
	p10_item = db.Column(db.String(80))
	winner = db.Column(db.String(80))
	team1_pnum_to_champ = db.Column(db.String(80))
	team2_pnum_to_champ = db.Column(db.String(80))

	def __init__(self, team1_ChampID, team2_ChampID, p1_item, p2_item, p3_item, p4_item, p5_item, p6_item, p7_item, p8_item, p9_item, p10_item, winner, team1_pnum_to_champ, team2_pnum_to_champ):
		self.team1_ChampID = team1_ChampID
		self.team2_ChampID = team2_ChampID
		self.p1_item = p1_item
		self.p2_item = p2_item
		self.p3_item = p3_item
		self.p4_item = p4_item
		self.p5_item = p5_item
		self.p6_item = p6_item
		self.p7_item = p7_item
		self.p8_item = p8_item
		self.p9_item = p9_item
		self.p10_item = p10_item 
		self.winner = winner
		self.team1_pnum_to_champ = team1_pnum_to_champ
		self.team2_pnum_to_champ = team2_pnum_to_champ

	def __repr__(self):
		return '<Match %r>' % self.id
