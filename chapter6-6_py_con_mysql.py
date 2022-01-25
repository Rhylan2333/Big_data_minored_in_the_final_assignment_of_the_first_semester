import pymysql

dbhost0 = "202.205.91.153"
dbuser0 = "s2019319010229"
dbpass0 = "caiyuhao"
dbname0 = "s2019319010229db"

dbhost = "localhost"
dbuser = "root"
dbpass = "123456"
dbname = "pyconnmysql"


def conn_test(dbhost, dbuser, dbpass, dbname):
    """测试连接用"""
    try:
        conn = pymysql.connect(host=dbhost,
                               user=dbuser,
                               password=dbpass,
                               database=dbname)
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION()')
        db_version = cursor.fetchone()
        print("MySQL数据库连接成功，版本号: %s" % db_version)
        print("\thost: {} user: {} password: {} database: {}".format(
            dbhost, dbuser, dbpass, dbname))
        conn.close()
    except pymysql.Error as e:
        print("MySQL数据库连接失败：" + str(e))
        print("\thost: {} user: {} password: {} database: {}".format(
            dbhost, dbuser, dbpass, dbname))


conn_test(dbhost0, dbuser0, dbpass0, dbname0)
conn_test(dbhost, dbuser, dbpass, dbname)