import pandas as pd
from src.utils.process_dates import *
from src.config.db import logsdb, logsrawdb
from src.utils.process_dates import create_is_late_flag
from src.modules.rh.schemas.log import absCountEntity, latesCountEntity, dailyLogsEntity
from src.utils.response.response import response_builder_log

def query_month_log_count(sdate, edate) -> list:

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

def query_month_late_count(sdate, edate) -> list:

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

def query_daily_logs(ddate) -> list:

    query = [
        {
            '$match': {
                'log_date': {
                    '$eq': create_timestamp_from_YMD(ddate),
                }, 
                'log_gate': {
                    '$eq': 'IN'
                }
            }
        }, {
            '$sort': {
                'log_time': 1
            }
        }, {
            '$group': {
                '_id': '$log_member_name', 
                'log_member_id': {
                    '$first': '$log_member_name'
                }, 
                'log_member_name': {
                    '$first': '$log_member_name'
                }, 
                'log_time': {
                    '$first': '$log_time'
                }, 
                'log_count': {
                    '$count': {}
                }
            }
        }, {
            '$sort': {
                'log_time': -1
            }
        }
    ]
    return dailyLogsEntity(logsrawdb.aggregate(query))

def query_month_working_days(sdate, edate):

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
                '_id': '$log_date'
            }
        }, {
            '$count': 'count'
        }
    ]
    return [x["count"] for x in logsrawdb.aggregate(query)][0]

def process_month_log_count(sdate, edate) -> list:
    df = pd.DataFrame()
    df_abs = query_month_log_count(sdate, edate)
    df_late = query_month_late_count(sdate, edate)
    try:
        df = pd.merge(pd.DataFrame(df_abs), pd.DataFrame(df_late), how="left", on="log_member_id", suffixes=('', '_y'))
        df = df.filter(regex='^(?!.*_y)').fillna(0).sort_values(by=["log_month_late_count"], ascending=False)
        df['log_month_count'] = df.log_month_count.map(lambda x: int(x))
        df['log_month_late_count'] = df.log_month_late_count.map(lambda x: int(x))
        df['log_month_working_days'] = query_month_working_days(sdate, edate)
        df['log_month_absence_count'] = df.log_month_working_days - df.log_month_count
        return response_builder_log(df.to_dict(orient='records'), f'{sdate}:{edate}')
    except Exception:
        return response_builder_log(df, f'{sdate}:{edate}')

def process_daily_logs(ddate) -> list:
    df = pd.DataFrame(query_daily_logs(ddate))
    try:
        df['log_time_islate'] = df.log_time.map(lambda x: create_is_late_flag(x))
        return response_builder_log(df.to_dict(orient='records'), ddate)
    except AttributeError:
        return response_builder_log(df, ddate)
