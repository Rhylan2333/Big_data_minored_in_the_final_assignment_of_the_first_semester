# 定义模型 Flask一SQLALchemy 使用继承至 db.Model 的类来定义模型，如:
class User(db.Model):
    __tablename__ = 'users'
    #每个属性定义一个字段
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '< User %r>' % self.user_name