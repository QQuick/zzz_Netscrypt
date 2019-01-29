import netscrypt

class Dog:
    def __init__ (self, name):
        self.name = name
        
    def speak (self, sound):
        return (f'I am {self.name} and I say {sound}')
        
dogs = (Dog ('Lassie'), Dog ('Rintintin'))

netscrypt.register (dogs, 'server.dogs')    # Don't automatically name after module, since it may run in multiple places
