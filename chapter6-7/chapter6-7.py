import os


def is_first_run():
    """判断是否首次使用系统"""
    flag = open("flag.txt")
    word = flag.read()
    if word == "0":
        print("首次启动该系统")
        flag.close()
        is_flag()  # 这个函数在下面
        init()  # 这个函数在下面
        print_menu()  # 这个函数在下面
        user_login_select()  # 这个函数在下面
    elif word == "1":
        print("欢迎使用会员管理系统")
        print("==选择角色登录系统==")
        print_menu()  # 这个函数在下面
        user_login_select()  # 这个函数在下面
    else:
        print("初始化参数错误！")
    return None


def is_flag():
    """用于修改flag.txt的内容"""
    f = open("flag.txt", "w")
    f.write("1")
    f.close()
    return None


def init():
    """写和创建"""
    file = open("admin.txt", "w")
    root = {"rname": "admin", "rpwd": "abc123"}
    file.write(str(root))
    file.close()
    os.mkdir("usersinfo")  # 写入文件
    return None


def print_menu():
    """用于打印菜单的两个选项"""
    print("1-管理员登录")
    print("2-普通用户登录")
    print("----------------")
    return None


def user_login_select():
    """接收输入，判选择登录"""
    while True:
        user_type_select = input("选择用户类型为：")
        if user_type_select == "1":
            admin_login()
            break
        elif user_type_select == "2":
            while True:
                select = input("是否需要注册？(y/n)")
                if select == "y" or select == "Y":
                    print("--用户注册--")
                    user_register()
                    break
                elif select == "n" or select == "N":
                    print("--用户登录--")
                    break
                else:
                    print("输入有误，请重新选择。")
            user_login()
            break
        else:
            print("输入有误，请重新选择。")


def admin_login():
    """用于管理员登录"""
    while True:
        print("***管理员登录***")
        root_name = input("请输入登录名：")
        root_password = input("请输入密码：")
        file_root = open("admin.txt")
        root = eval(file_root.read())
        if root_name == root['rname'] and root_password == root['rpwd']:
            print("登录系统成功！")
            break
        else:
            print("验证失败！")


def user_register():
    """用于普通用户登录"""
    user_id = input("请输入账户名：")
    user_pwd = input("请输入密码：")
    user_name = input("请输入昵称：")
    user = {"u_id": user_id, "u_pwd": user_pwd, "u_name": user_name}  # 书中这里错了，他在变量名外面加引号！
    user_path = "./usersinfo/" + user_id
    file_user = open(user_path, "w")
    file_user.write(str(user))
    file_user.close()


def user_login():
    """实现普通用户登录"""
    while True:
        print("***普通用户登录***")
        user_id = input("请输入账户名：")
        user_pwd = input("请输入密码：")
        user_list = os.listdir("./usersinfo")
        flag = 0
        for user in user_list:
            if user == user_id:
                flag = 1
                print("登录中……")
                file_name = "./usersinfo/" + user_id #  书里没有加后缀名
                file_user = open(file_name)
                user_info = eval(file_user.read()) #  书里没有加后缀名，其实不用加
                if user_pwd == user_info['u_pwd']:
                    print("系统登录成功！")
                    break
        if flag == 1:
            break
        elif flag == 0:
            print("查无此人，请先注册用户")
            break


is_first_run()