from models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and user.password == password:
        return user

def identity(payload):
    user_id=payload.get('identity', None)
    return UserModel.find_by_id(user_id)
