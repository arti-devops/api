import pymongo
from src.config.env import MONGODB_HOST, MONGODB_PORT

# DB engine
conn = pymongo.MongoClient(MONGODB_HOST,port=MONGODB_PORT)

# Documents
logsdb = conn.dsi.logs
logsrawdb = conn.dsi.logs_raw
devicesdb = conn.dsi.devices
projectsdb = conn.dsi.projects