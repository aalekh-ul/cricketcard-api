import jsons

json_data = open("sa_apidata2.json").read()
json_obj=jsons.loads(json_data)

for item in json_obj:
	data=item.get("data")
	for i in data:
		id=i.get("pid")
		print(id)

