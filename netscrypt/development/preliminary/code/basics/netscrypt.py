class Incomplete:
    pass

class Proxy:
    ''' A generalized proxy class
    
    Proxies locally represent remote objects.
    Any attribute access on them is passed on to the remote object.
    If the remote object doesn't support the attribute, a local exception is raised.
    
    Remote objects are never locally instantiated directly.
    They just are obtained from the exchange.
    While they seem to have a class identical to the remote one,
    this local proxy class is a mere dummy for now.
    
    It's not yet completely clear where this may make the ship strand.
    Things like 'isinstance' are bound to be influenced by it.
    This bridge will be crossed when experiments or practical demands take us there.
    '''    
    def __init__ (self, socket, uol):   # uol ('jewel') == universal object locator
        self.__ns_socket__ = socket
        self.__ns_uol__ = uol
        
    def __setattr__ (self, name, value):
        self.__ns_send__ ('set', name, value)
        self.__ns_recv__ ()
        
    def __getattr__ (self, name):
        self.__ns_send__ ('get', name)
        try:
            return self.__ns_recv__ ()
        except Incomplete:
            def bound (args, kwargs):
                self.__ns_send__ ('arg', args, kwargs)
                return self.__ns_recv__ ()
            return bound
        
    def __ns_send__ (self, *args):
        self.socket.send (json.dumps ([self.__ns_uol__] + args))    # Will raise any relevant exceptions
    
    def __ns_recv__ (self):
        args = json.loads (self.socket.recv (self))                 # Will raise any relevant exceptions
        if args [0]:
            return args [1:]
        else:
            raise Incomplete ()
            
class Delegator:
    ''' A Delegator deals with requests from a Proxy
    
    First it locates the object using the uol.
    Then it uses the object to set or get the attribute
    Then, if the attribute is a method, it will receive the arguments
    '''
    
    def __init__ (self):
        self.objects = {}   # Should become a remotely available dictionary
        self.listen ()      # Shouldn't block, of course...
        
    def register (self, anObject, qualifiedName):
        self.objects [qualifiedName]
        
    def resolve (self, qualifiedName):
        self.objects [qualifiedName]
        
    def listen (self):
        message = await self.recv ()
        anObject = self.resolve (message [0])
        if message [1] == 'set':
            setattr (anObject, message [2], message [3])
        elif message [1] == 'get':
            attribute = getattr (anObject, message [2]):
            if callable (attribute):
                await self.send (False, None)
            else:
                await self.send (True, attribute)
        elif message [1] == 'arg':
            await self.send (True, attribute (*args, **kwargs))

delegator = Delegator ()    # Class, despite singleton, for future flexibility a.o.

def register (*args, **kwargs):
    delegator.register (*args, **kwargs)

def resolve (*args, **kwargs):
    delegator.resolve (*args, **kwargs)
    