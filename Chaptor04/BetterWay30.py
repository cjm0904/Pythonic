import psycopg2
from psycopg2.extras import RealDictCursor
import extConfig
from flask_restful import Resource
import json


class Database:
    def __init__(self, host=extConfig.dbHost, port=extConfig.dbPort, dbName=extConfig.dbName, user=extConfig.dbUser,
                 password=extConfig.dbPassword):
        self.conn = psycopg2.connect(host=host, port=port, user=user, password=password, dbname=dbName)
        self.cursor = self.conn.cursor(cursor_factory=RealDictCursor)

    def query(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def using_yield_query(self, query):
        try:
            self.cursor.execute(query)
            for row in self.cursor:
                result = row['deviceName']
                yield result
        except Exception as e:
            print(e)

    def close(self):
        self.cursor.close()
        self.conn.close()


class getCasDbData(Resource):
    def get(selfs):
        pass

    def post(self):
        qry = 'select * from table'  # 데이터를 가져오는 쿼리
        result = Database.query(qry)
        Database.close()
        return json.dumps(result)


class getLatestCasDbData(Resource):
    def post(self):
        latestQry = 'select * from table where '  # 마지막 데이터를 가져오는 쿼리
        result = Database.query(latestQry)
        Database.close()
        return json.dumps(result)