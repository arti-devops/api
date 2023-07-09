from pymongo import MongoClient
conn = MongoClient(port=5001)

# Documents
devicesdb = conn.dsi.devices