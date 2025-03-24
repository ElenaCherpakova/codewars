class ReNameAbleClass(object):
    def __init__(self, name=None):
        self.name = name
    @classmethod
    def change_class_name(cls, new_name):
        if (not new_name or 
            new_name[0].islower() or 
            new_name[0].isdigit() or 
            not new_name.isalnum()):
            raise Exception("Invalid class name")
        cls.__name__ = new_name
        return cls
        
        
​
    def __str__(self):
         return f"Class name is: {self.__class__.__name__}"
​