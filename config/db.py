import pymongo
conn = pymongo.MongoClient(port=5001)

# Documents
devicesdb = conn.dsi.devices