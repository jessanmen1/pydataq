import psycopg2
import pandas as pd
import os

class DataQuality(object):
    def __init__(self,source_query,target_query):
        self.source_query=source_query
        self.target_query=target_query
        source_conn_string=os.environ.get('SOURCE_CONN')
        target_conn_string=os.environ.get('TARGET_CONN') #if they cannot be found, raise exception
        self.source_conn = psycopg2.connect(source_conn_string)
        self.target_conn = psycopg2.connect(target_conn_string)


    def run_source_query(self):
        return pd.read_sql_query(self.source_query,self.source_conn)
    
    def run_target_query(self):
        return pd.read_sql_query(self.target_query,self.target_conn)
aaaa
bbbb