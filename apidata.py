import requests

url = "https://dev132-cricket-live-scores-v1.p.rapidapi.com/playersbyteam.php"

querystring = {"teamid":"6"}

headers = {
    'x-rapidapi-key': "c259dbd80emsh84df9032a28e1afp1e09b6jsneb1620080d8a",
    'x-rapidapi-host': "dev132-cricket-live-scores-v1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)