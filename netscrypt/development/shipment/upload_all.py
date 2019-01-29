import os

shipDir = os.path.dirname (os.path.abspath (__file__)) .replace ('\\', '/')
appRootDir = '/'.join  (shipDir.split ('/')[ : -2])
distributionDir = '/'.join  (appRootDir.split ('/')[ : -1])
dynWebRootDir, statWebRootDir = eval (open ('upload_all.nogit') .read ())

os.chdir (distributionDir)
os.system ('uploadPython')

os.system ('git add .')
os.system ('git commit -m"{}"'.format (input ('Description of commit: ')))
os.system ('git push origin master')

os.chdir (shipDir)
