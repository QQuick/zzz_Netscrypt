import json
import asyncio
import websockets

hostName = 'localhost'
portNr = 6666

class JsonSocket:
	def __init__ (self, socket):
		self.socket = socket
		
	async def send (self, anObject):
		return await socket.send (json.dumps (anObject))
		
	async def recv (self):
		return json.loads (await socket.recv ())
		
class Client:
    def __init__ (self):
        asyncio.run (self.clientLoop ())

    async def clientLoop	(self):
		'''
		- Called once
		- Runs forever
		'''
        async with websockets.connect (f'ws://{centralHostName}:{centralPortNr}') as socket:
			jsonSocket = JsonSocket  (socket)
			while True:
				await jsonSocket.send (self.command ())
				self.handleCommand ()
				self.reply = await jsonSocket.recv ()
 
class Server:
	def __init__ (self):
		async def serverLoop (socket):
			'''
			- Called once for each client
			- Handles the socket belonging to the client that it's called for
			- Remains looping for that client until connection is closed
			- So several calls of this coroutine run concurrently, one per client
			'''  
			try:
				jsonSocket = JsonSocket (socket) 
				while True:
					self.command = await jsonSocket.recv ()
					self.handleCommand ()
					await jsonSocket.send (self.reply ())                            
			except websockets.exceptions.ConnectionClosed:
				print (f'Error: connection closed by client')
			except Exception as exception:
				print (f'Error: {exception}')
				
		# Start server loop creator and keep it running forever, waiting for new clients
        serverFuture = websockets.server (self.serverLoop, hostName, portNr)
        asyncio.get_event_loop () .run_until_complete (serverFuture)
        
        # Prevent termination of event loop, since server loops are subscribed to it
        syncio.get_event_loop () .run_forever ()
	
class Proxy:
    ''' A generalized proxy class
    
    Proxies locally represent remote objects.
    Any attribute (method or data) access on them is passed on to the remote object.
    If the remote object doesn't support the attribute, a local exception is raised.
    
    Remote objects are never locally instantiated directly.
    They just are obtained from the exchange.
    While they seem to have a class identical to the remote one,
    this local proxy class is a mere dummy (for now).
    
    It's not yet completely clear where this may make the ship strand.
    Things like 'isinstance' are bound to be influenced by it.
    This bridge will be crossed when experiments or practical demands take us there.
    '''  

	class Incomplete (Exception):
		pass
	
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
			
class Client:
            
class Server:



    ''' A server deals with requests from a Proxy
    
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
    