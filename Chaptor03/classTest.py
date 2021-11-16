class CheckIndex:
    def __init__(self):
        pass

    def get_index(self):
        return self.index

    def plus_index(self):
        self.index += 1

    def minus_index(self):
        self.index -= 1

    def zero_index(self):
        self.index = 0


# chkIndex = CheckIndex(1)
# chkIndex.plus_index()
# print(chkIndex.get_index())
chkIndex = CheckIndex()
chkIndex.zero_index()
chkIndex.plus_index()
print(chkIndex.get_index())
# print(chkIndex)

# -----------------------

import time
import time
import pymysql as sql
from personInOutCheckConnection import sendMessage
from extConfig import inOutManageConfig as iomConfig

class PersonInOutCheck:
    def __init__(self):
        self.lastIndex = 0

    def getInitIndex(self):
        getMaxIndexQry = 'select max(lg_idx) as max_index from m_smart_log;'
        conn = sql.connect(host=iomConfig.iomHost, port=iomConfig.port, user=iomConfig.dbUserId,
                           password=iomConfig.dbUserPw, db=iomConfig.db, charset='utf8')
        conn.ping(reconnect=True)
        with conn.cursor(sql.cursors.DictCursor) as cursor:
            cursor.execute(getMaxIndexQry)
            row = cursor.fetchone()
            indexCnt = row['max_index']
            return indexCnt

    def check(self, index):
        getLatestLogQry = 'select a.lg_idx, ' \
                              'a.datetime as ftime, ' \
                              'a.evt as eventNo, ' \
                              'a.`inout`, ' \
                              'a.army_id, ' \
                              'a.location_id, ' \
                              'a.ac_user_id, ' \
                              'a.evt_nm as evt_name, ' \
                              'b.army_name, ' \
                              'b.location_name ' \
                          'from m_smart_log as a ' \
                          'inner join m_army as b ' \
                          'on a.location_id=b.location_id ' \
                          'where datetime = (SELECT max(datetime) FROM m_smart_log);'

        conn = sql.connect(host=iomConfig.iomHost, port=iomConfig.port, user=iomConfig.dbUserId,
                           password=iomConfig.dbUserPw, db=iomConfig.db, charset='utf8')
        conn.ping(reconnect=True)
        with conn.cursor(sql.cursors.DictCursor) as cursor:
            cursor.execute(getLatestLogQry)
            row = cursor.fetchone()
            now = int(time.time())

            print(row)
            rowNo = row['lg_idx']
            if row['eventNo'] not in iomConfig.authList:
                if index < row['lg_idx']:
                    conn.close()
                    return {"flag": True, "row": row, "index": rowNo}
                else:
                    conn.close()
                    return {"flag": False, "row": None, "index": rowNo}
            else:
                conn.close()
                return {"flag": False, "row": None, "index": rowNo}

    # 전역으로 쓰지말고, init에 변수를 선언하면 클래스 내에서 사용가능한 변수로 만들 수 있음.
    def run(self):
        index = self.getInitIndex()
        try:
            getData = self.check(index=index)
            self.lastIndex = getData["index"]
            if getData["flag"]:
                sendMessage.makeEventMsg(getData["row"])
            time.sleep(iomConfig.interval / 1000)
        except ValueError as ve:
            print(ve)
        pass