import netscrypt

dogs = netscrypt.resolve ('server.dogs')

for dog in dogs:
    print (dog.name)
    print (dog.speak ('wraff'))
