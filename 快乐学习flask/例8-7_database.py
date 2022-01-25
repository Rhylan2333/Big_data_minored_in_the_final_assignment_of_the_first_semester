from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql # 这个书里没讲
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'test.db')  # 在当前路径下创建test.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def db_init():
    db.create_all()


# P182 定义模型 Flask一SQLALchemy 使用继承至 db.Model 的类来定义模型，如:
class User(db.Model):
    __tablename__ = 'users'
    #每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '< User %r>' % self.user_name


db_init()  # 书 P182 改进
