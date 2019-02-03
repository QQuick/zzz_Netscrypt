import netscrypt

with netscrypt.Server ('localhost', 6666) as server:
	class Dog:
		def __init__ (self, name):
			self.name = name
			
		def speak (self, sound):
			return (f'I am {self.name} and I say {sound}')
			
	dogs = (Dog ('Lassie'), Dog ('Rintintin'))

	server (dogs, 'dogs')
