import redis
r=redis.StrictRedis(host='localhost',port=6379,db=0)


# Opening and Closing a file "MyFile.txt" 
# for object name file1. 
file1 = open("entrada.in", "r") 
lines=file1.read().split('\n')
for l in lines:
    data=l.split('\t')
    if(data.__len__()>1):
        r.set(data[0],data[1])
    else:
        r.set(data[0],data[0])
file1.close() 

