import pymongo
from src.config.env import MONGODB_HOST, MONGODB_PORT

# DB engine
conn = pymongo.MongoClient(MONGODB_HOST,port=MONGODB_PORT)

# Documents
logsdb = conn.dsi.logs
membersdb = conn.dsi.members
devicesdb = conn.dsi.devices
logsrawdb = conn.dsi.logs_raw
#projectsdb = conn.dsi.projects
projectsdb = conn.dsi.os