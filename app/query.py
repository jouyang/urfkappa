def form_query(id1,id2):
	query = "SELECT * FROM urfkappa.matches where (((team1_ChampID like \"[" + str(id1) + \
		",%\" or team1_ChampID like \"%, "+ str(id1) + \
		", %\" or team1_ChampID like \"%, "+ str(id1) + \
		"]\") and (team2_ChampID like \"["+ str(id2) + \
		",%\" or team2_ChampID like \"%, "+ str(id2) + \
		", %\" or team2_ChampID like \"%, "+ str(id2) + \
		"]\"))" + \
		" or " + \
		"((team1_ChampID like \"[" + str(id2) + \
		",%\" or team1_ChampID like \"%, "+ str(id2) + \
		", %\" or team1_ChampID like \"%, "+ str(id2) + \
		"]\") and (team2_ChampID like \"["+ str(id1) + \
		",%\" or team2_ChampID like \"%, "+ str(id1) + \
		", %\" or team2_ChampID like \"%, "+ str(id1) + \
		"]\")))"  
	return query