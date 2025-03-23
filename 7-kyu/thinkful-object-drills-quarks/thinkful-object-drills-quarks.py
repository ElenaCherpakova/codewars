class Quark(object):
    baryon_number = 1/3
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    
    def interact(self, quark2):
        self.color, quark2.color = quark2.color, self.color
       