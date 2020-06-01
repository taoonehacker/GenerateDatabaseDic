import os
import time
import pymysql


class DataDict(object):
    def __init__(self, connect_info):
        # 数据库连接配置
        self.host_name = connect_info[0]
        self.user_name = connect_info[1]
        self.pwd = connect_info[2]
        self.db_name = connect_info[3]
        self.folder_name = 'mysql_dict'

    def run(self, table_str):
        """脚本执行入口"""
        try:
            # 创建一个连接
            conn = pymysql.connect(self.host_name, self.user_name, self.pwd, self.db_name)
            # 用cursor()创建一个游标对象
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        except Exception:
            print('数据库连接失败，请检查连接信息！')
            exit(1)
        table_list = []
        if table_s == '*':
            sql = "select table_name from information_schema.tables where table_schema='%s' " % (self.db_name,)
            cursor.execute(sql)
            for row in cursor.fetchall():
                print(row['TABLE_NAME'])
                table_list.append(row['TABLE_NAME'])
        else:
            table_list = table_str.split(',')

        # 文件夹和文件处理
        file_path = self.folder_name + os.sep + self.db_name + '.md'
        self.deal_file(file_path)
        # 打开文件，准备写入
        dict_file = open(file_path, 'a', encoding='UTF-8')

        for table_name in table_list:
            # 判断表是否存在
            sql = "SHOW TABLES LIKE '%s'" % (table_name,)
            cursor.execute(sql)
            result_count = cursor.rowcount
            if result_count == 0:
                print('%s数据库中%s表名不存在，无法生成……' % (self.db_name, table_name))
                continue
            # 表注释获取
            print('开始生成表%s的数据字典' % (table_name,))
            sql = "show table status WHERE Name = '%s'" % (table_name,)
            cursor.execute(sql)
            result = cursor.fetchone()
            table_comment = result['Comment']
            dict_file.write('#### %s %s' % (table_name, table_comment))
            dict_file.write('\n | 序号 | 字段名称 | 字段类型 | 默认值 | 字段注释 |')
            dict_file.write('\n | --- | --- | --- | --- | --- |')

            # 表结构查询
            field_str = "ORDINAL_POSITION,COLUMN_NAME,COLUMN_TYPE,COLUMN_DEFAULT,COLUMN_COMMENT"
            sql = "SELECT %s FROM information_schema.COLUMNS WHERE table_schema='%s' AND table_name='%s' ORDER BY ORDINAL_POSITION ASC" % (
                field_str, self.db_name, table_name)
            cursor.execute(sql)
            fields = cursor.fetchall()
            for field in fields:
                ordinal_position = field['ORDINAL_POSITION']
                column_name = field['COLUMN_NAME']
                column_type = field['COLUMN_TYPE']
                column_default = str(field['COLUMN_DEFAULT'])
                column_comment = field['COLUMN_COMMENT']
                info = ' | ' + str(
                    ordinal_position) + ' | ' + column_name + ' | ' + column_type + ' | ' + column_default + ' | ' + column_comment + ' | '
                dict_file.write('\n ' + info)
            # 关闭连接
            print('完成表%s的数据字典' % (table_name,))
            dict_file.write('\n ')
        dict_file.close()
        cursor.close()
        conn.close()

    def deal_file(self, file_name):
        """处理存储文件夹和文件"""
        # 不存在则创建文件夹
        if not os.path.exists(self.folder_name):
            os.mkdir(self.folder_name)
        # 删除已存在的文件
        if os.path.isfile(file_name):
            os.unlink(file_name)

    def test_conn(self, conn_info):
        """测试数据库连接"""
        try:
            # 创建一个连接
            pymysql.connect(conn_info[0], conn_info[1], conn_info[2], conn_info[3])
            return True
        except Exception:
            return False


if __name__ == '__main__':
    # 数据数据连接信息
    conn_info = input('请输入mysql数据库连接信息(格式为：主机IP,用户名,登录密码,数据库名)，逗号分隔且输入顺序不能乱，例如：192.168.0.1,root,root,test_db：')
    conn_list = conn_info.split(',')
    while conn_info == '' or len(conn_list) != 4:
        conn_info = input(
            '请正确输入mysql数据库连接信息(格式为：主机IP,用户名,登录密码,数据库名)，逗号分隔且输入顺序不能乱，例如：192.168.0.1,root,root,test_db：')
        conn_list = conn_info.split(',')
    # 测试数据库连接问题
    dd_test = DataDict(conn_list)
    db_conn = dd_test.test_conn(conn_list)
    while db_conn == False:
        conn_info = input(
            '请正确输入mysql数据库连接信息(格式为：主机IP,用户名,登录密码,数据库名)，逗号分隔且输入顺序不能乱，例如：192.168.0.1,root,root,test_db：')
        conn_list = conn_info.split(',')
        if len(conn_list) != 4:
            continue
        dd_test = DataDict(conn_list)
        db_conn = dd_test.test_conn(conn_list)
    # 输入数据表名称
    table_s = input('请输入数据库表名(例如：t_order)，如需输入多个表名请用英文逗号分隔(例如：t_order,t_goods)，结束使用请输入q：')
    dd = DataDict(conn_list)
    while table_s != 'q':
        dd.run(table_s)
        table_s = input('继续使用请输入数据库表名（例如t_order），如需输入多个表名请用英文逗号分隔（例如t_order,t_goods），结束使用请输入q）：')
    else:
        print('谢谢使用，再见……')
        time.sleep(1)
