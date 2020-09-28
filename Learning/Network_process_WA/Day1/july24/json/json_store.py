import json

a = {
    "name" : "John",
    "scores" : (23, 44, 55, [22, 33, 44], [55, 66, 77]),
    "a1" : {
            "x": 10,
            "y": "this is a test string"
    },
    "pass": True,
    "visited": None
}


print(json.dumps(a))
with open("a.json", "w") as out:
    json.dump(a, out, indent=1)

