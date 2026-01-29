from flask import abort
def id_search(session, search_id, Notepad, current_id): 
        return session.query(Notepad).filter_by(userid=current_id, noteid=search_id).first()
    
def method_judge(method):
    if method == 'POST':
        return
    else:
         abort(405)
