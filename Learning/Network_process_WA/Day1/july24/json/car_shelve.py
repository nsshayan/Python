import shelve

class Car:

    def __init__(self, name):
        self.__dict__['data'] = shelve.open(name + ".dat")
        self.__dict__['data']['name'] = name
        print "Car object created..."
        
    def drive(self):
        print "Driving car", self.name

    def __getattr__(self, attr):
        return self.__dict__['data'][attr] 
       
    def __setattr__(self, attr, value):
        self.__dict__['data'][attr] = value

    def __del__(self):
        self.__dict__['data'].close()

