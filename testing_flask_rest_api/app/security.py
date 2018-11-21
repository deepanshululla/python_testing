from werkzeug.security import safe_str_cmp
try:
    from models.user import UserModel
except ImportError:
    from testing_flask_rest_api.app.models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
