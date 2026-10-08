def create_user(username, email):
    user = {
        "username": username,
        "email": email
    }

    return {
        "message": "User created successfully",
        "user": user
    }