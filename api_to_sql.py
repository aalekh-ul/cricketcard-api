import jsons
import mysql.connector

null = None;
json_data = open("aus_apidata3.json").read()
json_obj=jsons.loads(json_data)

mydb = mysql.connector.connect(host="localhost",user="root",passwd="mrrobot",database="crickgame_api")
cursor = mydb.cursor()




for item in json_obj:
	p_name=item.get("name")
	p_country=item.get("country")
	p_image=item.get("imageURL")

	"""try:
		runs=item.get("data").get("batting").get("T20Is").get("Runs")
		strikrate=item.get("data").get("batting").get("T20Is").get("SR")
		match=item.get("data").get("batting").get("T20Is").get("Mat")
		avg=item.get("data").get("batting").get("T20Is").get("Mat")
		wickets=item.get("data").get("bowling").get("T20Is").get("Wkts")
		economy=item.get("data").get("bowling").get("T20Is").get("Econ")
		hundreds=item.get("data").get("batting").get("T20Is").get("100")
		


	except AttributeError :
		runs=0
		strikrate=0.00


	cursor.execute("insert into crick_tt(runs,strikrate,matches,avg,wickets,economy,hundreds) values(%s,%s,%s,%s,%s,%s,%s)",(runs,strikrate,match,avg,wickets,economy,hundreds))"""

	
	

	cursor.execute("insert into crick_players(p_name,p_country,p_image) values(%s,%s,%s)",(p_name,p_country,p_image))

mydb.commit()


