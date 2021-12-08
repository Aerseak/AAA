import pymysql

host = "localhost"
user = "root"
password = ""
database = "中国工商银行帐户管理库"

def update(sql,param):#增、删、改
    con = pymysql.connect(host=host,
                          user=user,
                          password=password,
                          database=database)#链接数据库
    cursor = con.cursor()#创建控制台
    cursor.execute(sql,param)#执行sql语句
    con.commit()#提交到数据库
    cursor.close()#关闭控制台
    con.close()#关闭数据库

def select(sql,param,mode="many",size=1):
    con = pymysql.connect(host=host,
                          user=user,
                          password=password,
                          database=database)  # 链接数据库
    cursor = con.cursor()  # 创建控制台
    cursor.execute(sql, param)  # 执行sql语句
    if mode == "all":
        return cursor.fetchall()#mode=all时查询所有数据
    elif mode == "one":
        return cursor.fetchone()#mode=one时，查询一条数据
    elif mode == "many":
        return cursor.fetchmany(size)#mode=many时，查询size条数据
    con.commit()  # 提交到数据库
    cursor.close()  # 关闭控制台
    con.close()  # 关闭数据库