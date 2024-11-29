import json
from sys import exit
from datetime import datetime
from requests import get
from os import path
def jsonmagic(action, data, reve, n): # w for writing, r for reading, data is what to read, n is to see if the file is there
    if action == "r":
        with open("previousrev.json", "r") as json_file:
            thefile = json.load(json_file)
            print(type(thefile))
            previousrevenue = thefile["revenue"]
            olddate = datetime.fromisoformat(thefile["date"])
            if data == "o":
                return olddate
            elif data == "p":
                return previousrevenue
    elif action == "w":
        if n == True:
            print("no previous data found. a new json file will be created")
        with open("previousrev.json", "w") as json_file:
            curdate = datetime.now().replace(microsecond=0)
            tosave = {
                "revenue": reve,
                "date": curdate.isoformat()
            }
            json.dump(tosave, json_file, indent=4)
def datefinddif(prevdate):
    curdate = datetime.now().replace(microsecond=0)
    datedif = curdate-prevdate
    return datedif
def getcur():
    response = get("https://api.gamalytic.com/game/2073850?fields=revenue")
    rev = response.json()
    revenue = rev["revenue"]
    return revenue
reven = getcur()
nopreviousfile = False
try:
    print(f"the current revenue made by the finals is ${reven}. it has been {datefinddif(jsonmagic("r", "o", "", ""))} since you last checked, and the revenue has increased by ${reven-jsonmagic("r", "p", "", "")}")
except:
    if path.exists("previousrev.json"):
        print("your file (displaying the previous revenue) appears to have been corrupted.")
        nopreviousfile = False
    else:
        nopreviousfile = True
    print(f"the current revenue made by the finals is ${reven}.")
validInput = False
while validInput != True:
    nextaction = input("would you like to save this value to compare it later? (y/n) ").lower()
    if nextaction == "y":
        jsonmagic("w", "", getcur(), nopreviousfile)
        print("the revenue has been saved in previousrev.json within this folder.")
        print("now exiting...")
        validInput = True
    elif nextaction == "n":
        print("exiting...")
        validInput = True
    else:
        print("invalid input, please try again")