import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.cooxupe.com.br')

##print (response)
###dir (response)

##cod = response.fileno()
##print (cod)
##print ("#####################")
#cod1 = response.fp()
#print (cod1)
##cod2 = response.getcode()
##print (cod2)
##print ("#####################")
##cod3 = response.geturl()
##print (cod3)
##print ("#####################")
##cod4 = response.info()
##print (cod4)
##print ("#####################")
##cod5 = response.next()
##print (cod5)
##print ("#####################")
##cod6 = response.read()
##print (cod6)
##print ("#####################")
##cod7 = response.url
##print (cod7)
##print ("#####################")
##cod8 = response.readline()
##print (cod8)
##print ("#####################")
##cod9 = response.readlines()
##print(cod9)
##print ("#####################")
##cod10 = response.headers.keys()
##print (cod10)
##print ("#####################")
##cod11 = response.headers.values()
##print (cod11)
##print ("#####################")
#for header, value in response.headers.items():
##    print (header + " : " + value)