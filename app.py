from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from utils import id_search
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from auth.login import User, user_check

# Flaskアプリの準備
app = Flask(__name__)
app.secret_key = "test"

login_manager = LoginManager()
login_manager.init_app(app)

# SQLAlchemyの準備
engine = create_engine('sqlite:///flask_memo.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# モデル定義
class UserModel(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    pw = Column(String)

class Notepad(Base):
    __tablename__ = 'notes'
    noteid = Column(Integer, primary_key=True)
    note = Column(String)

Base.metadata.create_all(engine)

login_manager.login_view = 'login'

# 引数user_idにセッション内に登録されているIDが入ります
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/login_check", methods=['POST'])
def login_check():
    user = session.query(UserModel).filter_by(id=request.form['userid']).first()
    if user is not None and user_check(user, request.form['pass']):
        login_user(User(user.id))
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('login'))

# ルートにアクセスしたときの処理
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    notes = session.query(Notepad).all()
    return render_template('index.html', notes=notes, notecount=len(notes))

# メモの追加
@app.route('/add', methods=['POST'])
@login_required
def add_note():
    if request.form['addnote'] != "":
        addnote = Notepad(note=request.form['addnote'])
        session.add(addnote)
        session.commit()
    
    return redirect(url_for('index'))

# メモの削除
@app.route('/del', methods=['POST'])
@login_required
def del_note():
    if len(session.query(Notepad).all()) == 0:
        return redirect(url_for('index'))
    session.delete(id_search(session, request.form['delid'], Notepad))
    session.commit()
    return redirect(url_for('index'))

# メモの更新
@app.route('/update', methods=['POST'])
@login_required
def update_note():
    notes = session.query(Notepad).all()
    if len(notes) == 0:
        return redirect(url_for('index'))
        
    return render_template('update.html', notes=id_search(session, request.form['upnote'], Notepad))

# メモ更新の完了
@app.route('/update_comp', methods=['POST'])
@login_required
def updatecomp_note():
    upnote = id_search(session, request.form['upid'], Notepad)
    upnote.note = request.form['upnote']
    session.commit()

    return redirect(url_for('index'))

@app.route("/register", methods=['POST'])
def register():
    return render_template('register.html')

@app.route("/register_comp", methods=['POST'])
def register_comp():
    if session.query(UserModel).filter_by(id=request.form['userid']).first() is None:
        adduser = UserModel(id=request.form['userid'], pw=request.form['pass'])
        session.add(adduser)
        session.commit()
        return redirect(url_for('login'))
    else:
        return "すでに同じユーザーIDが登録されています"
if __name__ == '__main__':
    app.run(debug=True)