from flask import Flask, request, render_template
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

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
    return render_template('index.html', users=users, notecount=len(session.query(User).all()))

# 名前を追加する
@app.route('/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST' and request.form['addnote'] != "":
        name = request.form['addnote']
        user = User(name=name)
        session.add(user)
        session.commit()

        users = session.query(User).all()
        return render_template('index.html', users=users, notecount=len(session.query(User).all()))
               
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    users = session.query(User).all()
    return render_template('index.html', users=users, notecount=len(session.query(User).all()))

@app.route('/del', methods=['GET', 'POST'])
def del_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    if len(session.query(User).all()) == 0:
        return render_template('index.html', users=session.query(User).all(), notecount=len(session.query(User).all()))
    if request.method == 'POST' and request.form['delnote'] != "":
        delname = request.form['delnote']
        user = session.query(User).filter_by(id=delname[0]).first()
        session.delete(user)
        session.commit()

        users = session.query(User).all()
        return render_template('index.html', users=users, notecount=len(session.query(User).all()))
    
    
    return "エラー4"
if __name__ == '__main__':
    app.run(debug=True)