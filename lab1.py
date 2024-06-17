# Brandon Martinez
# Erika Rosales
import redis
r=redis.StrictRedis(host='localhost',port=6379,db=0)

#r.flushall()
file1 = open("entrada.in", "r") 
lines=file1.read().split('\n')
for l in lines:
    data=l.split('\t')
    if(data.__len__()>1):
        r.set(data[0],data[1])
        r.zadd("OrderSet",{data[0]:int(data[1])})
file1.close() 

consult=["ARIEL", "Bastard", "extra-ordinary","Caesar's", "Menelaus", "Achilles!", "Warwick", "WORKS--WILLIAM", "destroy'd?", "epitaph!"]
print("\n1) Numeros de frecunecia:\n")
for c in consult:
    data=r.get(c)
    print(c+': '+data.decode())
print("2) Primeras 10 palabras ordenadas por frecuencia:\n")
for c in r.zrange("OrderSet",0,10,desc=True):
    print(c.decode())
print("3)1. Palabras con 100 ocurrencias exactas:\n")
for c in r.zrangebyscore("OrderSet",100,100):
    print(c.decode())
print("3)2. Palabras con mas de 1000 ocurrencias:\n")
for c in r.zrangebyscore("OrderSet",1000,float('inf')):
    print(c.decode())
print("3)2. Palabras con entre 320 y 330 ocurrencias:\n")
for c in r.zrangebyscore("OrderSet",320,330):
    print(c.decode())
