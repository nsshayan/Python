class Car:
    def __init__(self, name, owner):
        print "Created car object: name = %s, owner = %s" % (name, owner)
        self.name = name
        self.owner = owner

    def drive(self):
        print "%s is driving %s" % (self.owner, self.name)

