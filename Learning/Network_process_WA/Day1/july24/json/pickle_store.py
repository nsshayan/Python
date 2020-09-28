import pickle

a = {
    "name" : "John",
    "scores" : (23, 44, 55),
    "pass": True,
    "visited": None
}


print pickle.dumps(a)
with open("a.pickle", "w") as out:
    pickle.dump(a, out)

