
import inspect

def attributes(entity):
    
    attributes = []
    for member in inspect.getmembers(entity):
        if not member[0].startswith('_'):
            if not inspect.ismethod(member[1]):
                attributes.append(member)
                
    return attributes

class Car:
    
    color = 'Gray'
    
    def brand(self):
        return 'brand'

car = Car()
print(attributes(car))