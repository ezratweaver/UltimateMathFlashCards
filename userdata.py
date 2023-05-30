from os import listdir, path, getenv, mkdir
from json import loads, dumps
from assets import userlist_banners

USERDATA_PATH = path.join(getenv('APPDATA'), "ultimate-mfc")

def create_data_directory():
    mkdir(USERDATA_PATH)

def check_for_users():
    all_users = []
    try:
        for file in listdir(USERDATA_PATH):
            if file.endswith(".json"):
                file_path = path.join(USERDATA_PATH, file)
                with open(file_path) as file:
                    all_users.append(loads(file.read()))
    except FileNotFoundError:
        create_data_directory()
        check_for_users()
    return sorted(all_users, key=lambda x: x['creationlevel'])

def get_user_count():
    return len(check_for_users())

def get_userlist_banner():
    user_count = get_user_count()
    if user_count >= 6:
        return userlist_banners.get(6)
    else:
        return userlist_banners.get(user_count + 1)

def get_highest_creationlevel():
    return check_for_users()[::-1][0]["creationlevel"]

