class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        
    def is_worth_it(self):
        return True if 20 < self.draft - (self.crew * 1.5) else False
​
            
        