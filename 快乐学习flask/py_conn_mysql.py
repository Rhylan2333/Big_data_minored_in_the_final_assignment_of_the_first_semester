import pymysql

dbhost0 = "202.205.91.153"
dbuser0 = "s2019319010229"
dbpass0 = "caiyuhao"
dbname0 = "s2019319010229db"

dbhost = "localhost"
dbuser = "caicai"
dbpass = "123456"
dbname = "program0_caicai_20220131"

config = {
    'host': "localhost",
    'port': 3306,
    'user': "caicai",
    'password': "123456",
    'database': "program0_caicai_20220131",
    'charset': 'utf8',  # 这里很关键！！！不是“utf-8”
    'cursorclass': pymysql.cursors.DictCursor,
}


def conn_test(dbhost, dbuser, dbpass, dbname):
    """测试连接用"""
    try:
        conn = pymysql.connect(host=dbhost,
                               user=dbuser,
                               password=dbpass,
                               database=dbname)
        cursor = conn.cursor()  # 创建游标
        cursor.execute('SELECT VERSION()')
        db_version = cursor.fetchone()  #使用fetchone()获取单条数据
        print("MySQL数据库连接成功，版本号: %s" % db_version)
        print("\thost: {} user: {} password: {} database: {}".format(
            dbhost, dbuser, dbpass, dbname))
        conn.close()
    except pymysql.Error as e:
        print("MySQL数据库连接失败：" + str(e))
        print("\thost: {} user: {} password: {} database: {}".format(
            dbhost, dbuser, dbpass, dbname))


def conn_test_dc(config):
    """测试连接用，传入config字典"""
    try:
        conn = pymysql.connect(**config)
        cursor = conn.cursor()  # 创建游标
        cursor.execute('SELECT VERSION()')
        db_version = cursor.fetchone()
        print(
            "MySQL数据库连接成功，版本号: %s" % db_version['VERSION()']
        )  # 不用db_version['VERSION()']的话会返回一个字典 {'VERSION()': '5.7.17-log'}
        print("\thost: {} port:{} user: {} password: {} database: {}".format(
            config['host'], config['port'], config['user'], config['password'],
            config['database']))
        conn.commit()  # 提交，不然无法保存新建或者修改的数据
        cursor.close()  # 关闭游标
        conn.close()  # 关闭连接
    except pymysql.Error as e:
        print("MySQL数据库连接失败：" + str(e))
        print("\thost: {} user: {} password: {} database: {}".format(
            dbhost, dbuser, dbpass, dbname))


# conn_test(dbhost0, dbuser0, dbpass0, dbname0)
# conn_test(dbhost, dbuser, dbpass, dbname)
# conn_test_dc(config)


def dosth():
    db = pymysql.connect(host=dbhost,
                         user=dbuser,
                         password=dbpass,
                         database=dbname)
    print("连接成功")
    cursor = db.cursor()  # 创建游标
    #执行sql查询操作
    sql0 = """DROP TABLE IF EXISTS `user`"""
    sql_create_table = """CREATE TABLE IF NOT EXISTS `user`(`id` INT, `name` VARCHAR(20)) ENGINE=INNODB DEFAULT CHARSET=utf8"""
    sql_insert = """INSERT INTO `user`(`id`, `name`) VALUES (2, '李明')"""
    sql_select = """SELECT * FROM `user`"""
    try:
        """执行sql"""
        cursor.execute(sql0)  #如果user表存在，就删除
        cursor.execute(sql_create_table)  #创建表user
        cursor.execute(sql_insert)  # 插入操作
        cursor.execute(sql_select)  # 查询操作
        result = cursor.fetchall()  # 获取所有记录列表
        for row in result:
            id = row[0]
            name = row[1]
            print("id = %d, name = %s" % (id, name))
        db.commit()  # commit()方法提交所有的事务，不然无法保存新建或者修改的数据
    except:
        """发生异常"""
        db.rollback()  # rollback()方法回滚当前游标的所有操作
        print("Error: unable to fecth data or……")
    cursor.close()  # 关闭游标
    print("End.")
    db.close()  # 关闭连接


dosth()