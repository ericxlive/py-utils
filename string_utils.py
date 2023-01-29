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
        self.content = [content]
        if(content):
            self.content.append(delimiter)
        self.delimiter = delimiter
        
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

    

