from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from utils import id_search

# Flaskアプリの準備
app = Flask(__name__)

# SQLAlchemyの準備
engine = create_engine('sqlite:///flask_memo.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# モデル定義
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)

Base.metadata.create_all(engine)

# ルートにアクセスしたときの処理
@app.route('/')
def index():
    users = session.query(User).all()
    return render_template('index.html', users=users, notecount=len(users))

# メモの追加
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST' and request.form['addnote'] != "":
        name = request.form['addnote']
        user = User(name=name)
        session.add(user)
        session.commit()

        users = session.query(User).all()
        return render_template('index.html', users=users, notecount=len(users))
               
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    users = session.query(User).all()
    return render_template('index.html', users=users, notecount=len(users))

# メモの削除
@app.route('/del', methods=['GET', 'POST'])
def del_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
        
    if len(session.query(User).all()) == 0:
        return render_template('index.html', users=session.query(User).all(), notecount=len(session.query(User).all()))
    
    session.delete(id_search(session, request.form['delid'], User, request.method))
    session.commit()
    users = session.query(User).all()

    return render_template('index.html', users=users, notecount=len(users))

# メモの更新
@app.route('/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    users = session.query(User).all()
    if len(users) == 0:
        return render_template('index.html', users=users, notecount=len(users))

    return render_template('update.html', users=id_search(session, request.form['upnote'], User, request.method))

# メモ更新の完了
@app.route('/update_comp', methods=['GET', 'POST'])
def updatecomp_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    user = id_search(session, request.form['upid'], User, request.method)
    user.name = request.form['upnote']
    session.commit()

    users = session.query(User).all()
    return render_template('index.html', users=users, notecount=len(users))

if __name__ == '__main__':
    app.run(debug=True)