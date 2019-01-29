class DogProxy:
    def __init__ (self, url):
        self.__remote__ = Remote (url)
        
    name = property (getName, setName)
    
    def getName (self):
        return self.__remote__.get (self, 'name')
    
    def setName (self, value):
        self.__remote__.set (self, 'name', value)
        
    def speak (self, sound):
        return self.__remote__.call ('intro', sound)

remote = Remote ('localhost:8000')
dogs = remote.dogs

for dog in dogs:
    print (dog.name)
    print (dog.speak ('wraff'))



        