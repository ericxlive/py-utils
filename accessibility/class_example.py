
from accessibility.decorators import private_access

'''The class Computer will represent a computer where info related to year of release, model and
   brand will be displayed if its __str__ method is called.'''
class Computer:
    
    '''It is expected the computer will have a brand, model and the year of release. The params
       are to be mantatory for this example.'''
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        
    '''The function will return the identification for a computer. The private_access decorator
       will hide the function.'''
    @private_access
    def identification(self):
        return f'{self.brand} - {self.model}, {self.year}'
    
    def __str__(self):
        # The identification function won't be visible outside of this class.
        return self.identification()
    
