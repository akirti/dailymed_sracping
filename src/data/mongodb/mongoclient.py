from pymongo import MongoClient

class MongoDBClient:
    def __init__(self, db_hostname=None,db_port=None, db_name=None):
        if db_hostname is None:
            self.hostname =DB_HOST
        else:
            self.hostname = db_hostname
        if db_port is None:
            self.port = DB_PORT
        else:
            self.port = db_port
        if db_name is None:
            self.dbName = DB_NAME
        else:
            self.dbName = db_name
    
    def create_client(self):
        client = MongoClient(self.hostname,self.port)        
        self.client = client
        return client
    
    def get_list_databases(self):
        if self.client is None:
            self.client = self.create_client()
            
        return self.client.list_databases()
        
    def get_dailymed_db(self,dbName=None):
        client = self.create_client()
        db = None
        if dbName is None:
            db = client[self.dbName]
        else:
            db = client[dbName]
        return db
    
    def get_list_collection(self, dbName=None):
        if self.client is None:
            self.client = self.create_client()
            
        db = self.get_dailymed_db(dbName)
        clxns = None
        if db is not None:
            clxns = db.list_collection_names()
        return clxns