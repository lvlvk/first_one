"""
存储二进制文件
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='123456',
                     database='stu', charset='utf8')

# 生成游标对象，用于操作数据库数据，获取sql执行结果的对象
cur = db.cursor()

# 打开文件
# with open('./timg.jpeg', 'rb') as file_var:
#     data = file_var.read()
# try:
#     sql = "update class1 set img=%s where id=1"
#     cur.execute(sql, [data])
#     db.commit()
# except Exception as e:
#     print(e)
#     db.rollback()

sql = "select img from class1 where id=1"
cur.execute(sql)
data = cur.fetchone()
with open('id_one_img.jpeg','wb') as f:
    f.write(data[0])

# 关闭游标和数据库
cur.close()
db.close()
