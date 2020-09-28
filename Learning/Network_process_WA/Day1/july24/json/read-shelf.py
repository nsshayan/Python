import shelve
store = shelve.open("data.dat")

for k, v in store.items():
    print k, "=", v

store.close()

#name = store['n']
#info = store['info']
#scores = store['marks']
#print "name: ", name
#print "info: ", info
#print "scores: ", scores
#store.close()


