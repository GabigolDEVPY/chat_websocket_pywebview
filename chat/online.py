ONLINE_USERS = {}

def add_user(user_id):
    ONLINE_USERS[user_id] = ONLINE_USERS.get(user_id, 0) + 1
    
def remove_user(user_id):
    if user_id in ONLINE_USERS:
        ONLINE_USERS[user_id] -= 1
        if ONLINE_USERS[user_id] <= 0:
            del ONLINE_USERS[user_id]
            
def is_online(user_id):
    return user_id in ONLINE_USERS