class Student:
    def __init__(self, first_name=None, last_name=None, grades=None):
        self.first_name = first_name
        self.last_name = last_name
        if grades is None:
            self.grades = []
        else:
            self.grades = grades
        
    def add_grade(self, grade):
        self.grades.append(grade)
        
    
    def get_average(self):
        return sum(self.grades) / len(self.grades)