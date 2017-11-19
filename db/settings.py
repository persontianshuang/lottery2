# mysql
MQ_HOST = 'localhost'
MQ_PORT = 6379
MQ_USER = 'root'
MQ_PASSWORD = 'root'
MQ_COLL = 'lottery'

# mongo
# MG_HOST = '108.61.203.110'
MG_HOST = 'localhost'
MG_PORT = 27017
MG_PASSWORD = None
MG_COLL = 'lottery'


import pymongo


class Mg():
    def __init__(self,host,port,password=None,coll=None):
        if password:
            self.client = pymongo.MongoClient(host, port,password=password)
        else:
            self.client = pymongo.MongoClient(host, port)

mg_lottery = Mg(MG_HOST,MG_PORT,password=MG_PASSWORD).client[MG_COLL]['log']
