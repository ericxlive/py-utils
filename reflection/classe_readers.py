
import inspect

def methods(entity):
    
    members = []
    for member in inspect.getmembers(entity):
        if not member[0].startswith('_'):
            if not inspect.ismethod(member[1]):
                members.append(member)
                
    return members