from flask import abort
def id_search(session, search_id, User):
    
        
        user = session.query(User).filter_by(id=search_id).first()

        return user
    
def method_judge(method):
    if method == 'POST':
        return
    else:
         abort(405)
