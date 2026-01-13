from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from utils import id_search, method_judge
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from auth.login import User, TestUser, user_check

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
class Notepad(Base):
    __tablename__ = 'notes'
    noteid = Column(Integer, primary_key=True)
    note = Column(String)

Base.metadata.create_all(engine)

login_manager.login_view = 'login'

# 引数user_idにセッション内に登録されているIDが入ります
@login_manager.user_loader
def load_user(user_id):
   #認証情報さえかえせればいいので、別に新規作成しても問題なし
    return User(user_id)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/login_check", methods=['GET', 'POST'])
def login_check():
    test_user = TestUser("user1", "testuser")
    if user_check(test_user, request.form['userid'], request.form['pass']):
        login_user(User(1))
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    logout_user()
    return "Logout完了"

# ルートにアクセスしたときの処理
@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    notes = session.query(Notepad).all()
    return render_template('index.html', notes=notes, notecount=len(notes))

# メモの追加
@app.route('/add', methods=['GET', 'POST'])
def add_note():
    method_judge(request.method)

    if request.form['addnote'] != "":
        addnote = Notepad(note=request.form['addnote'])
        session.add(addnote)
        session.commit()
    
    return redirect(url_for('index'))

# メモの削除
@app.route('/del', methods=['GET', 'POST'])
def del_note():
    method_judge(request.method)
        
    if len(session.query(Notepad).all()) == 0:
        return redirect(url_for('index'))
    session.delete(id_search(session, request.form['delid'], Notepad))
    session.commit()
    return redirect(url_for('index'))

# メモの更新
@app.route('/update', methods=['GET', 'POST'])
def update_note():
    method_judge(request.method)

    notes = session.query(Notepad).all()
    if len(notes) == 0:
        return redirect(url_for('index'))
        
    return render_template('update.html', notes=id_search(session, request.form['upnote'], Notepad))

# メモ更新の完了
@app.route('/update_comp', methods=['GET', 'POST'])
def updatecomp_note():
    method_judge(request.method)
    
    upnote = id_search(session, request.form['upid'], Notepad)
    upnote.note = request.form['upnote']
    session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)