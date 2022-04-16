# 需要根据自己的mysql配置这些（主要是用户名和密码）
# 部署到云服务器上时按那上面的环境来
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask'
USERNAME = 'root'
PASSWORD = '123456'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME,password=PASSWORD, host=HOST,port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
SQLALCHEMY_COMMIT_ON_TEARDOWN = True