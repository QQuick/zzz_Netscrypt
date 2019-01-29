class Local:
    def call (self, anObject, name, args, kwargs):
        try:
            self.send (True, getattr (anObject, name) (*args, **kwargs))
        except:
            self.send (False)
        
    def get (self, name):
        try:
            self.send (True, getattr (anObject, name))
        except:
            self.send (False)
    
    def set (self, name, value):
        try:
            setattr (anObject, name, value)
            self.send (True)
        except:
            self.send (False)
    
class Dog:
    def __init__ (self, name):
        self.name = name
        
    def speak (self, sound):
        return (f'I am {self.name} and I say {sound}')
        
dogs = (Dog ('Lassie'), Dog ('Rintintin'))

local = Local ()
local.register (dogs)
        