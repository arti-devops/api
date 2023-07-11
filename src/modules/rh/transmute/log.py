from src.config.db import logsdb
from src.utils.process_dates import *
from src.modules.rh.schemas.log import latesCountEntity

def process_month_log_count(sdate, edate):

    query = [
        {
            '$match': {
                'log_date': {
                    '$gte': create_timestamp_from_YMD(sdate),
                    '$lte': create_timestamp_from_YMD(edate),
                }
            }
        }, {
            '$group': {
                '_id': '$log_member_name', 
                'log_member_name': {
                    '$first': '$log_member_name'
                }, 
                'log_member_id': {
                    '$first': '$log_member_id'
                }, 
                'log_month_count': {
                    '$sum': 1
                }
            }
        }
    ]

    return latesCountEntity(logsdb.aggregate(query))