"""
练习
    使用数据库完成注册登录功能，数据表自己拟定
    注册方法，收集用户信息，将用户信息存储到数据库，用户名不能重复
    登录方法，获取用户名密码，与数据库信息比对，判定是否允许登录
"""
import pymysql


class Database:
    def __init__(self, host='localhost', port=3306,
                 user='root', password='123456',
                 database='login', charset='utf8'):
        self.db = pymysql.connect(host=host, port=port,
                                  user=user, password=password,
                                  database=database, charset=charset)
        self.cur = self.db.cursor()

    # 注册,数据用户名，密码，并且用户名不能有重复
    def sign_up(self, name: str, password: str) -> bool:
        try:
            sql = "select name from users where name=%s"
            self.cur.execute(sql, [name])
            self.db.commit()
        except Exception as e:
            print(e)
            return False
        else:
            try:
                sql = "insert into users(name,password) values(%s,%s)"
                self.cur.execute(sql, [name, password])
                self.db.commit()
            except Exception as e:
                print(e)
                return False
            else:
                return True

    # 登录
    def login(self, name: str, password: str) -> bool:
        try:
            sql = "select * from users where name=%s and password=%s"
            self.cur.execute(sql, [name, password])
            self.db.commit()
        except Exception as e:
            print(e)
            return False
        else:
            return True


def main():
    the_database = Database()

    # print(the_database.sign_up("lvlvk", "123456"))

    print(the_database.login("lvlvk", "123456"))
    print(the_database.cur.fetchone())

    # 关闭游标和数据库
    the_database.cur.close()
    the_database.db.close()


if __name__ == '__main__':
    main()
