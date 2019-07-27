'''
tag:
class,method
'''

#answer1.0 by april
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        print(draft,crew)
    def is_worth_it(self):
        return self.draft -20 > self.crew*1.5
        
#answer2.0 
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew  = crew
        self.worth = 20 < draft - 1.5 * crew
        
    def is_worth_it(self): 
        return self.worth

#answer3.0 
class Ship:
    def __init__(self, draft, crew):
        self.draft = draft
        self.crew = crew
        self.is_worth_it = lambda: self.draft - self.crew * 1.5 > 20


