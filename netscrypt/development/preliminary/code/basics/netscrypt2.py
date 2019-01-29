class Proxy:
    ''' A general proxy class
    '''
    def __init__ (self, exchange, region, url):
        self.__ns_exchange__ = exchange
        self.__ns_region__ = region
        self.__ns_url__ = url
        
    def __ns_get__ (self, attributeName):
        self.__ns_send__ ('get', attributeName)
        return self.__ns_recv__ ()

    def __ns_set__ (self, attributeName, value):
        self.__ns_send__ ('set', attributeName, value)
        self.__ns_recv__ ()
        
    def __ns_call__ (attributeName, args, kwargs):
        self.__ns_send__ ('call', attributeName, args, kwargs)
        return self.__ns_recv__ ()
        
    def __ns_send__ ():
        pass
    
    def __ns_receive__ ():
        pass

remote = Remote ('localhost:8000')
dogs = remote.dogs

for dog in dogs:
    print (dog.name)
    print (dog.speak ('wraff'))