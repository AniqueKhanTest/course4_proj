import requests
OMDB_API_KEY = "18f98edc"


params = {"apikey":OMDB_API_KEY,"t":"star wars"}
resp = requests.get("https://www.omdbapi.com/", params=params)

print(resp.json())