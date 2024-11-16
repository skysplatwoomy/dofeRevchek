import json
from datetime import datetime
from requests import get
try:
    with open("previousrev.json", "r") as json_file:
        thefile = json.load(json_file)
        print(type(thefile))
        previousrevenue = thefile["revenue"]
        olddate = datetime.fromisoformat(thefile["date"])
        nopreviousfile = False
except:
    nopreviousfile = True
def datefinddif(prevdate):
    curdate = datetime.now().replace(microsecond=0)
    datedif = curdate-prevdate
    return datedif
response = get("https://api.gamalytic.com/game/2073850?fields=revenue")
rev = response.json()
revenue = rev["revenue"]
if nopreviousfile == False:
    print(f"the current revenue made by the finals is ${revenue}. it has been {datefinddif(olddate)} since you last checked, and the revenue has increased by ${revenue-previousrevenue}")
else:
    print(f"the current revenue made by the finals is ${revenue}.")
if input("would you like to save this value to compare it later? (y/n) ").lower() == "y":
    if nopreviousfile == True:
        print("no previous data found. a new json file will be created")
    with open("previousrev.json", "w") as json_file:
        curdate = datetime.now().replace(microsecond=0)
        tosave = {
            "revenue": revenue,
            "date": curdate.isoformat()
        }
        json.dump(tosave, json_file, indent=4)
        print("the data has been saved to a file named 'previousrev.json'")