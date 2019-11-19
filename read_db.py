"""
pymysql

"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='123456',
                     database='stu', charset='utf8')

# 生成游标对象，用于操作数据库数据，获取sql执行结果的对象
cur = db.cursor()

# select操作
sql = "select * from class1;"
cur.execute(sql)

# cur是可迭代对象，可通过遍历获取select结果
# for item in cur:
#     print(item)

print("---------------------")

print(cur.fetchone())

print(cur.fetchmany(3))

print(cur.fetchall())

# 关闭游标和数据库
cur.close()
db.close()