import json

info = {
    "name"  : "john",
    "city"  : "delhi",
    "age"   : 30,
    "owns"  : { "car" : "ferrari", "bike" : "yamaha" },
    "visited" : ["mumbai", "kolkatta", "bengaluru"]
}


with open("data.json", "w") as out:
    json.dump(info, out)


