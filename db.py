import pymysql
# from TMS.common.handle_config import conf


class MySqlHander(object):
    # 操作数据库
    def __init__(self):
        # 连接数据库
        try:
            self.con = pymysql.connect(
                                       # host=conf['mysql']['host'],
                                       # user=conf['mysql']['user'],
                                       # password=conf['mysql']['password'],
                                       # db=conf['mysql']['db'],
                                       # charset="utf8",
                                       # cursorclass=pymysql.cursors.DictCursor
                host="localhost",
                user="root",
                password="123456",
                db="information_schema",
                charset="utf8",
                cursorclass=pymysql.cursors.DictCursor
                                       )

            # 创建一个游标对象
            self.cur = self.con.cursor()

        except Exception as e:
            print("数据库连接失败：", e)

    def find_all(self, sql):
        """查询语句",返回所有的数据"""
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchall()

    def find_one(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        return self.cur.fetchone()

    def update(self, sql):
        self.cur.execute(sql)
        self.con.commit()

    def find_count(self, sql):
        self.con.commit()
        res = self.cur.execute(sql)
        return res

    def db_close(self):
        # 关闭游标
        self.cur.close()
        # 关闭数据库
        self.con.close()


if __name__ == "__main__":
    tms = MySqlHander()
    sql = "select * from CHARACTER_SETS";
    res = tms.find_all(sql)
    print(res)