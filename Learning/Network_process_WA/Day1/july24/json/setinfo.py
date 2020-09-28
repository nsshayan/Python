import pickle

info = { }

info['name'] = raw_input("Enter name: ")
info['age']  = raw_input("Enter age: ")
info['city'] = raw_input("Enter city: ")

print "Gathered info: ", info

#pickle.dump(info, open("info.dat", "w"))

with open("info.dat", "w") as out:
    pickle.dump(info, out)



