
import inspect

def attributes(entity):
    
    members = []
    for member in inspect.getmembers(entity):
        if not member[0].startswith('_'):
            if not inspect.ismethod(member[1]):
                members.append(member)
                
    return members

class Car:
    
    color = 'Gray'
    
    def brand(self):
        return 'brand'

car = Car()
print(attributes(car))