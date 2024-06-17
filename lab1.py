# Brandon Martinez
# Erika Rosales
import redis

#conectando a la base de datos local
r=redis.StrictRedis(host='localhost',port=6379,db=0)

#r.flushall()

#Lectura de archivo
file1 = open("entrada.in", "r") 
#separando por lineas
lines=file1.read().split('\n')
for l in lines:
    #separando por tab
    data=l.split('\t')  
    #guardando solo las claves validas 
    if(data.__len__()>1): 
        #guardando clave valor
        r.set(data[0],data[1])
        #guardando set para ordenamiento
        r.zadd("OrderSet",{data[0]:int(data[1])})
#cerrando archivo
file1.close() 

#Consultas simples
consult=["ARIEL", "Bastard", "extra-ordinary","Caesar's", "Menelaus", "Achilles!", "Warwick", "WORKS--WILLIAM", "destroy'd?", "epitaph!"]
print("\n1) Numeros de frecunecia:")
for c in consult:
    data=r.get(c)
    print(c+': '+data.decode())

#consultas ordenadas
print("\n2) Primeras 10 palabras ordenadas por frecuencia:")
rank=1
for c in r.zrange("OrderSet",0,9,desc=True):
    print(str(rank)+". '"+c.decode()+"'")
    rank+=1

#consultas por rango
print("\n3)1. Palabras con 100 ocurrencias exactas:")
for c in r.zrangebyscore("OrderSet",100,100):
    print("'"+c.decode()+"'")
print("\n3)2. Palabras con mas de 1000 ocurrencias:")
for c in r.zrangebyscore("OrderSet",1000,float('inf')):
    print("'"+c.decode()+"'")
print("\n3)2. Palabras con entre 320 y 330 ocurrencias:")
for c in r.zrangebyscore("OrderSet",320,330):
    print("'"+c.decode()+"'")
