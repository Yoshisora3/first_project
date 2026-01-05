def id_search(session, search_id, User, method):
    if method == 'POST':
        
        user = session.query(User).filter_by(id=search_id).first()

        return user