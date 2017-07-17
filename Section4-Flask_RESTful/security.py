from werkzeug.security import safe_str_cmp
from user import User

# In-memory table of our users
users = [
    User(1, 'bob', 'asdf')
]

# Username Mapping
username_mapping = {u.username: u for u in users}

# User ID Mapping
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)