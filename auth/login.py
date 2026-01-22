from flask_login import UserMixin

class User(UserMixin):
   def __init__(self, id):
#　最低限IDがあれば問題ないが普通はユーザ名称などを入れると思われる
      self.id = id

class TestUser():
   def __init__(self, name, pw):
      self.name = name
      self.pw = pw

def user_check(user, check_user, check_pass):
   if user.name == check_user and user.pw == check_pass:
      return True
   else:
      return False

