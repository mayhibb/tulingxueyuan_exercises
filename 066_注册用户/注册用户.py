users_passwords = {"qqq":123456789,"www":123456}

user_names = users_passwords.keys()

def create_user_name():

    # 全局化变量，下面要用到存储
    global username
    username = str(input("请输入用户名： "))

    # 判断用户名是否存在
    if username in user_names or username == "":
        print("用户名已存在！请重试...")
        return create_user_name()
    else:
        return create_user_password()

def create_user_password():

    # 确认密码
    user_password_first = str(input("请输入密码："))
    user_password_second = str(input("请再次输入，确认密码："))

    if user_password_first != user_password_second:
        print("两次输入不相同，请重试！")
        return create_user_password()
    else:
        # 存入字典
        users_passwords[username] = user_password_first
        print("注册成功！  为您跳转登入界面...")
        return loginUser()

def loginUser():

    global login_username
    login_username = str(input("请输入登入账户："))

    if login_username not in user_names:
        print("该用户名还未被注册！！！")
        return loginUser()
    else:
        return loginPassword()

times = 5    
def loginPassword():
    global times
    while times:
        login_password = str(input("请输入密码："))
        if login_password != users_passwords[login_username]:
            print("密码输入错误，请重试！","还剩(",times-1,")","次")
            times -= 1
            return loginPassword()
        else:
            print("登入成功！")
            break
        
        

create_user_name()
