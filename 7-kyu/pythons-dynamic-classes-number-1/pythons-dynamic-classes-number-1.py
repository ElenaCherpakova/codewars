class MyClass:
    def __init__(self, name):
        self.name = name
        
​
def class_name_changer(cls, new_name):
    if (not new_name or 
        new_name[0].islower() or 
        new_name[0].isdigit() or 
        not new_name.isalnum()):
        raise Exception("Invalid class name")
    cls.__name__ = new_name
    return cls
​
​