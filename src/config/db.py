import pymongo
#TODO in dev, adapt this link
#conn = pymongo.MongoClient("mongodb://192.168.0.9",port=27017)
conn = pymongo.MongoClient("mongodb://localhost",port=27017)

# Documents
logsdb = conn.dsi.logs
logsrawdb = conn.dsi.logs_raw
devicesdb = conn.dsi.devices