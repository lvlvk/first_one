"""
write


"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='123456',
                     database='stu', charset='utf8')

# 生成游标对象，用于操作数据库数据，获取sql执行结果的对象
cur = db.cursor()

# 执行各种数据库sql操作
try:
    # execute直接传入命令
    # sql = 'insert into class1(name,age,sex,score) ' \
    #       'values("Dave",16,"m",92);'

    # name = input("name:")
    # age = input("age:")
    # sex = input("sex('m','f','o'):")
    # score = input("score:")
    # sql = 'insert into class1(name,age,sex,score) values("%s",%s,"%s",%s)'%(name,age,sex,score)
    # print(sql)
    # cur.execute(sql)
    # sql = 'insert into class1(name,age,sex,score) values(%s,%s,%s,%s)'
    # cur.execute(sql, [name, age, sex, score])

    # sql = "insert into class1(name,age,score) values('Lily',18,89.5);"
    # cur.execute(sql)
    #
    # sql = "update class1 set age=26 where id=5;"
    # cur.execute(sql)
    #
    # sql = "delete from class1 where sex is null;"
    # cur.execute(sql)

    value_list = []
    for i in range(3):
        name = input("name:")
        age = input("age:")
        score = input("score:")
        value_list.append((name, age, score))
    sql = 'insert into class1(name,age,score) values(%s,%s,%s)'
    cur.executemany(sql, value_list)

    db.commit()
except Exception as e:
    print(e)
    db.rollback()

# 关闭游标和数据库
cur.close()
db.close()
