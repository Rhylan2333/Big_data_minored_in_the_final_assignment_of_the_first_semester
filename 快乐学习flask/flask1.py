from flask import Flask, request
from flask import url_for  # 例8-5
from flask import render_template  # 例8-6，见 @app.route('/') 的return

app = Flask(__name__)


# 例8-1 一般路由
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello')
def hello():
    return 'Hello 菜菜. '


# 例8-2 在路径中添加参数
@app.route('/welcome/<username>')
def welcome(username):
    return 'Hello %s. ' % username


# 例8-3 指定变量的类型
@app.route('/add/<int:num>')  # 不指定默认为path
def add(num):
    num += 1
    return '输入进url的数，自增一为：%d' % num


# 例8-4 路径最后分隔符有无的区别
@app.route('/caicai/')  # 不指定默认为path
def show_caicai():
    return 'This is CaiCai.'


@app.route('/yuhaocai')  # 末尾加“/”则不通
def show_yuhaocai():
    return 'This is Yuhao Cai.'


# 第169页
@app.route('/login1', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':  # 从flask导入request
        return "POST方法，因此登录。"
    else:
        return "这是GET方法，因此显示登录页面。"


# 将“/login”这个 URL 映射到不同函数中
@app.route('/login2', methods=['POST'])
def do_the_login():
    return "POST方法。"


@app.route('/login2', methods=['GET'])
def do_the_login_form():
    return "GET方法。"


# 例8-5 url_for()的使用
@app.route('/user/<username>')
def profile(username):
    pass
# 例8-6 使用
@app.route('/user8-6/<name>')
def user(name):
    return render_template('user.html', name='name')# 这里与url、参数中的那么对应

# 告知解析器在其作用域内模拟一个 HTTP 请求上下文。
# HTTP 请求上下文是调用 url_for 的必须环境。
with app.test_request_context():
    print(url_for('index'))  # 这里面的是该url下映射的def函数名
    print(url_for('hello'))
    print(url_for('welcome', username='蔡雨豪（例8-5 测试）'))
    print(url_for('add', num='887'))
    print(url_for('show_yuhaocai', next='/'))
if __name__ == '__main__':
    app.run()