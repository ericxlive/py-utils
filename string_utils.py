__author__ = "Eric de Sousa"
__email__ = "eric@codeonthego.dev"
__maintainer__ = "Eric de Sousa"

void = ''
empty_space = ' '

'''The StringMaker will provide the ability to concatenate string content and
   it will index every entry.'''
class StringMaker:
    
    '''It starts the object with or without specific content. If content not
       informed it will add an empty space to the first index of string.'''
    def __init__(self, content:'str'='', delimiter=void):
        self.content = []
        if(content):
            if(content.index(empty_space)):
                words = content.split(delimiter)
                for word in words:
                    self.content.append(word)
        
    '''It will return the entry related to the index informed. The valid entries
       range from 1 to length. If invalid index is entered the method will return
       None.'''
    def get(index=None):
        if(index):
            if(self.content):
                if(index >= len(self.content)):
                    return self.content[index-1]
        return None
    
    '''If the first index of StringMaker content is empty. It will append the param
       as the first position.'''
    def append(self, content: 'str'=void):
        if(self.content[0]==''):
            self.content[0] = content
        else:
            self.content.append(content)
        self.content.append(self.delimiter)
        return self
        
    '''It will enforce line break. If will show up when the object is converted to 
       string.'''
    def new_line(self):
        self.content.append('\n')
        return self
        
    '''The routine will join all content from self.content and return a string with 
       all entries as a single string output.'''
    def __str__(self):
        return ''.join(self.content)

'''The StringChain will connect strings and add gaps between every entry. '''
class StringChain(StringMaker):
    
    def __init__(self, content:'str'=void):
        StringMaker.__init__(self, content, delimiter=' ')

'''Internal communication protocol.'''
class ICP:
    
    '''The internal communication protocol will encapsulate all user entries to
       the communication system. It will include the current state for the user
       and values informed in last interaction.'''
    def __init__(self, uri=None):
        self.uri = uri
        self.__map()
        
    '''The routine should return the state which comes before every ?. If
       no sign (?) is present the state will be the string itself as long as
       its length is not 0.'''
    def get_header(self):
        pass
    
    '''It will return a value related to a param part of the uri. For example:
       home.members.shifts.selected?username=eric&shift=2023-01-01. If the key
       is equals to "shift" the routine should return in this case 2023-01-01
       and the return MUST be a string.
       
       Sometimes the param will hold values of distinct types. Another example:
       uri: home.members.shifts?username=eric&shift=3. The key=shift would return 
       in this case the number 3, but as string.
       '''
    def get(self, key=None):
        pass
    
    '''The routine return all available params in uri. If no param it will return 
       None.'''
    def params(self):
        pass
    
    '''The routine returns the number of params within the uri informed. If no param
       within the uri the routine will return False.'''
    def has_params(self):
        pass
    
    '''The __map() routine will map params and values related. This routine is private.
       and must NOT be visible from outside this context.'''
    def __map(self):
        pass
    