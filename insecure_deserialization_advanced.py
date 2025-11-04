def load_session(token):
    import pickle, base64
    session = base64.b64decode(token)
    return pickle.loads(session)
