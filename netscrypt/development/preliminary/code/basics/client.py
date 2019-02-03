import netscrypt

with netscrypt.Client ('localhost', 6666) as client:
	dogs = client ('dogs')
	
	for dog in dogs:
		print (dog.name)
		print (dog.speak ('wraff'))
