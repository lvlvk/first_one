"""
练习
    创建数据库 dict 使用utf8编码
    在数据库中创建数据表 words 包含字段
    id word mean
    将单词本中的单词插入到数据库中，单词和解释分别插入记录的对应字段
"""
import pymysql
import re

# 连接数据库
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='123456',
                     database='dict', charset='utf8')

# 生成游标对象，用于操作数据库数据，获取sql执行结果的对象
cur = db.cursor()

# 打开文件
file_var = open('dict.txt', 'r')
index = 0
for data_line in file_var:
    data = re.findall(r"(\S+)\s+(.*)", data_line)[0]
    index += 1
    sql = "insert into words(id,word,mean) values(%s,%s,%s)"
    cur.execute(sql, [index, data[0], data[1]])
db.commit()

# 关闭游标和数据库
cur.close()
db.close()
