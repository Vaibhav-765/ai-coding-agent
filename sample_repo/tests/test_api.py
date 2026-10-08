from user_service import create_user

def test_create_user():
    result = create_user("john", "john@example.com")

    assert result["user"]["username"] == "john"