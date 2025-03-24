class Menu:
    def __init__(self, items=[]):
        self.items = items
        self.position = 0 if self.items else None
    def to_the_right(self):
        self.position = self.position + 1
        if self.position >= len(self.items):
            self.position = 0
        
    def to_the_left(self):
        self.position = self.position - 1
        if self.position < 0:
            self.position = len(self.items) - 1
        
    def display(self):
        result = self.items.copy()
        result[self.position] = [result[self.position]]
        return str(result)