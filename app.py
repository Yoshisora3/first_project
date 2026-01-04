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
    return render_template('index.html', users=users, notecount=len(users))

# 名前を追加する
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

@app.route('/del', methods=['GET', 'POST'])
def del_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    if len(session.query(User).all()) == 0:
        return render_template('index.html', users=session.query(User).all(), notecount=len(session.query(User).all()))
    if request.method == 'POST' and request.form['delnote'] != "":
        delname = request.form['delnote']
        delid = delname[0]

        #メモが10個以上あるとうまく消せないので処理を追加
        flag = 0
        for i in  delname:
            if i == ":":
                break
            if flag == 1:
                delid += i
            else:
                flag = 1
        
        user = session.query(User).filter_by(id=delid).first()
        session.delete(user)
        session.commit()

        users = session.query(User).all()
        return render_template('index.html', users=users, notecount=len(users))
    
    
    return "エラー4"

@app.route('/update', methods=['GET', 'POST'])
def update_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    users = session.query(User).all()
    if len(users) == 0:
        return render_template('index.html', users=users, notecount=len(users))
    if request.method == 'POST' and request.form['upnote'] != "":
        upname = request.form['upnote']
        upid = upname[0]

        #メモが10個以上あるとうまく消せないので処理を追加
        flag = 0
        for i in  upname:
            if i == ":":
                break
            if flag == 1:
                upid += i
            else:
                flag = 1
            
        user = session.query(User).filter_by(id=upid).first()

    return render_template('update.html', users=user)

@app.route('/update_comp', methods=['GET', 'POST'])
def updatecomp_user():
    if request.method == 'GET':
        return "エラー GET送信されました"
    
    upname = request.form['upnote']
    
    upid = request.form['upid']
    user = session.query(User).filter_by(id=upid).first()
    user.name = upname
    session.commit()

    users = session.query(User).all()
    return render_template('index.html', users=users, notecount=len(users))

if __name__ == '__main__':
    app.run(debug=True)