from flask_login import UserMixin

class User(UserMixin):
   def __init__(self, id):
#　最低限IDがあれば問題ないが普通はユーザ名称などを入れると思われる
      self.id = id

def user_check(user, check_pass):
   if user.pw == check_pass:
      return True
   else:
      return False

