class Person:
    def __init__(self, name, age, city):
        self.name, self.age, self.city = name, age, city

    def greet(self):
        print self.name, "says Hello"

