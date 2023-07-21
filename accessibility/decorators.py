
import re

def private_access(func):
    def inner(*args, **kwargs):
        name = func.__name__
        pattern = re.compile(fr'(.*)\.{name}')
        with open(__file__) as file:
            for line in file:
                lst = pattern.findall(line)
                if (lst and not line.strip().startswith('#')
                   and not all(g.strip() == 'self' for g in lst)):
                    raise Exception()
        return func(*args, **kwargs)
    return inner


