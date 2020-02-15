from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 建立MySQL与app的连接
from const import DatabaseConst
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DatabaseConst.MYSQL_USERNAME, DatabaseConst.MYSQL_PASSWORD,
                                                          DatabaseConst.MYSQL_HOST, DatabaseConst.MYSQL_PORT,
                                                          DatabaseConst.MYSQL_DBNAME)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 通过命令行 "flask initdb" 创建数据库
import click
from mysql import Administrator, Notice, Room, Apply, Timetable
@app.cli.command()
def initdb():
    db.create_all()
    click.echo('Initialized database.')


@app.route('/')
def hello_world():
    return 'Hello World!'
  
  
# 注册所有蓝本的视图函数
from register import register_all
register_all(app)

if __name__ == '__main__':
    app.run()
