#!/usr/bin/env python
class Person(object):
    def __init__(self, name):
        self.name = name

    def reveal_identity(self):
        print "My name is {}".format(self.name)

class SuperHero(Person):
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name

    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print " ... And I am {}".format(self.hero_name)

# kleiton = Person("Kleiton Silva")
# kleiton.reveal_identity()

oak = SuperHero("Kleiton Silva", "OAK")
oak.reveal_identity()
