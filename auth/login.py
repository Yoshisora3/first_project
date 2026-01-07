from flask_login import UserMixin

# 　UserMixinを継承したクラスに更にSqlAlchemyのModelを継承させてもOK
class User(UserMixin):
   def __init__(self,id):
#　最低限IDがあれば問題ないが普通はユーザ名称などを入れると思われる
      #　詳しくは公式サイトのサンプル参照（https://flask-login.readthedocs.io/）
      self.id = id