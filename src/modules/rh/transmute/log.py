import pandas as pd
from src.config.db import logsdb
from src.utils.process_dates import *
from src.modules.rh.schemas.log import absCountEntity, latesCountEntity

def query_month_log_count(sdate, edate):

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
                '_id': '$log_member_id', 
                'log_member_name': {
                    '$first': '$log_member_name'
                }, 
                'log_month_count': {
                    '$sum': 1
                }
            }
        }
    ]

    return absCountEntity(logsdb.aggregate(query))

def query_month_late_count(sdate, edate):

    query = [
        {
            '$match': {
                'log_date': {
                    '$gte': create_timestamp_from_YMD(sdate),
                    '$lte': create_timestamp_from_YMD(edate),
                }, 
                '$expr': {
                    '$or': [
                        {
                            '$gt': [
                                {
                                    '$hour': {
                                        '$toDate': '$log_checkin'
                                    }
                                }, 8
                            ]
                        }, {
                            '$and': [
                                {
                                    '$eq': [
                                        {
                                            '$hour': {
                                                '$toDate': '$log_checkin'
                                            }
                                        }, 8
                                    ]
                                }, {
                                    '$gte': [
                                        {
                                            '$minute': {
                                                '$toDate': '$log_checkin'
                                            }
                                        }, 10
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        }, {
            '$group': {
                '_id': '$log_member_id', 
                'log_member_name': {
                    '$first': '$log_member_name'
                }, 
                'log_month_late_count': {
                    '$sum': 1
                }
            }
        }
    ]

    return latesCountEntity(logsdb.aggregate(query))

def process_month_log_count(sdate, edate):
    df_abs = query_month_log_count(sdate, edate)
    df_late = query_month_late_count(sdate, edate)
    df = pd.merge(pd.DataFrame(df_abs), pd.DataFrame(df_late), how="left", on="log_member_id", suffixes=('', '_y'))
    df = df.filter(regex='^(?!.*_y)').fillna(0).sort_values(by=["log_month_late_count"], ascending=False)
    df['log_month_count'] = df.log_month_count.map(lambda x: int(x))
    df['log_month_late_count'] = df.log_month_late_count.map(lambda x: int(x))
    return df.to_dict(orient='records')