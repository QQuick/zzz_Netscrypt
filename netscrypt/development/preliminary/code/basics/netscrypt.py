class Remote:
    def __init__ (self, url):
        self.url = url
        
    def call (self, name, args, kwargs):
        self.socket.send (
            'call',
            name,
            [self.getUrl (arg) for arg in args],
            {(kwarg, self.getUrl) (kwargs [kwarg]) for kwarg in kwargs}
        ) 
        return self.socket.recv ()
        
    def get (self, name):
        self.socket.send ('get', name)
        return self.socket.recv ()
    
    def set (self, name, value):
        self.socket.send ('set', name, value)
        socket.recv
        
    def send (self, *args):
        self.socket.send.json.encode (args)
    
    def recv (self):
        success, payload =  json.decode (self.socket.recv)
        if success:
            return payload
        else:
            raise Exception ()
            return 0