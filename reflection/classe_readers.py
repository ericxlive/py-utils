
import inspect

'''Return class objects attribute names. Only the attributes/members including the 
   instance attributes.__annotations__'''
def attributes(entity):
    
    attributes = []
    for member in inspect.getmembers(entity):
        if not member[0].startswith('_'):
            if not inspect.ismethod(member[1]):
                attributes.append(member)
                
    return attributes

def instance_attributes(entity):
    attributes = []
    for attribute in entity.__dict__.keys():
        attributes.append(attribute)
    
    return attributes

def attributes_with_values(entity):
    attributes = {}
    for attribute in entity.__dict__.keys():
        if attribute[:2] != '__':
            value = getattr(entity, attribute)
            if not callable(value):
                attributes[attribute] = value
    return attributes

class Car:
    
    color = 'Gray'
    
    def __init__(self):
        self.brand = self.Brand()
    
    def change_color(self, new_color):
        color = new_color
        
    class Brand:
        pass

car = Car()
print(instance_attributes(car))