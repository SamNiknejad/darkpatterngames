import json

l = open ("hlinks.txt", "w")

with open("hgames.json", "r") as f:
       jsonlist = json.load(f)

for i in range(len(jsonlist)):
    if "link" in jsonlist[i]:
       url = jsonlist[i]["link"][0]
       full = "https://www.darkpattern.games" + url + "\n"
       l.write(full)


