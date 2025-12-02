import json

l = open ("links.txt", "w")

with open("games.json", "r") as f:
       jsonlist = json.load(f)

for i in range(len(jsonlist)):
    if "link" in jsonlist[i]:
       url = jsonlist[i]["link"][0]
       full = "https://www.darkpattern.games" + url + "\n"
       l.write(full)