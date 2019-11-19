"""
练习
    使用数据库完成注册登录功能，数据表自己拟定
    注册方法，收集用户信息，将用户信息存储到数据库，用户名不能重复
    登录方法，获取用户名密码，与数据库信息比对，判定是否允许登录
"""
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost', port=3306,
                     user='root', password='123456',
                     database='login', charset='utf8')

# 生成游标对象，用于操作数据库数据，获取sql执行结果的对象
cur = db.cursor()


# 注册,数据用户名，密码，并且用户名不能有重复
def is_name_exists(name: str):
    sql = "select name from users where name=%s"
    cur.execute(sql, [name])
    db.commit()
    if cur.fetchone()[0] == name:
        return True
    return False


def sign_up() -> None:
    while True:
        name = input("user_name:")
        password = input("password:")
        if is_name_exists(name):
            print("用户名已存在！请重新输入")
            continue
        else:
            try:
                sql = "insert into users(name,password) values(%s,%s)"
                cur.execute(sql, [name, password])
                db.commit()
                print("注册成功！")
            except Exception as e:
                print(e)
                return
            return

def is_password_true(name:str, password:str)->bool:
    sql = "select password from users where name=%s and password=%s"
    cur.execute(sql, [name,password])
    db.commit()
    if cur.fetchone()[0] == password:
        return True
    return False

# 登录
def login()->None:
    while True:
        name = input("user_name:")
        password = input("password:")
        if not is_name_exists(name):
            print("用户名不存在！请重新输入")
            continue
        elif not is_password_true(name, password):
            print("密码输入错误！")
            continue
        else:
            try:
                sql = "select * from users where name=%s;"
                cur.execute(sql, [name])
                db.commit()
                print(cur.fetchone())
            except Exception as e:
                print(e)
                return
            return



# 关闭游标和数据库
cur.close()
db.close()
