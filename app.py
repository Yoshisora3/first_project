from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from utils import id_search, method_judge

# Flaskアプリの準備
app = Flask(__name__)

# SQLAlchemyの準備
engine = create_engine('sqlite:///flask_memo.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# モデル定義
class Notepad(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    note = Column(String)

Base.metadata.create_all(engine)

# ルートにアクセスしたときの処理
@app.route('/', methods=['GET', 'POST'])
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