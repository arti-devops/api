import pymongo
from src.config.env import MONGODB_HOST, MONGODB_PORT

# DB engine
conn = pymongo.MongoClient(MONGODB_HOST,port=MONGODB_PORT)

# Documents
#logsdb = conn.dsi.nlogs
logsdb = conn.dsi.logs
membersdb = conn.dsi.members
devicesdb = conn.dsi.devices
#logsrawdb = conn.dsi.nlogs_raw
logsrawdb = conn.dsi.logs_raw
#projectsdb = conn.dsi.projects
projectsdb = conn.dsi.os

nlogsdb = conn.dsi.nlogs
nlogsrawdb = conn.dsi.nlogs_raw