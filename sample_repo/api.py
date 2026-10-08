from user_service import create_user

def create_user_api(username, email):
    return create_user(username, email)