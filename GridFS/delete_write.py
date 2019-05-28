import pymongo

#MONGODB ATLAS URL
DB_URI = 'mongodb+srv://fyp_admin:fyp_pwd@cluster0-oov30.mongodb.net/test?retryWrites=true'
import gridfs
client = pymongo.MongoClient(DB_URI)
db = client.testing
fs=gridfs.GridFS(db)
####################################################deleting image#########################################
collection = db.fs.files
result = collection.find_one({"filename":"influenza"})
files_id=result['_id']
fs.delete(files_id)
collection = db.fs.files
result = collection.find_one({"filename":"gastro"})
files_id=result['_id']
fs.delete(files_id)
collection = db.fs.files
result = collection.find_one({"filename":"conjunctivitis"})
files_id=result['_id']
fs.delete(files_id)
collection = db.fs.files
result = collection.find_one({"filename":"respiratoryinfection"})
files_id=result['_id']
fs.delete(files_id)
####################################################writing image##########################################
data=open("flu.png","rb")
thedata=data.read()
stored=fs.put(thedata,filename="influenza")
data=open("gastro.png","rb")
thedata=data.read()
stored=fs.put(thedata,filename="gastro")
data=open("conjunctivitis.png","rb")
thedata=data.read()
stored=fs.put(thedata,filename="conjunctivitis")
data=open("respiratoryinfection.png","rb")
thedata=data.read()
stored=fs.put(thedata,filename="respiratoryinfection")
