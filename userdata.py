from os import listdir, path, getenv, mkdir, remove
from json import loads, dump
from assets import userlist_banners

USERDATA_PATH = path.join(getenv('APPDATA'), "ultimate-mfc")


def create_user_directory():
    mkdir(USERDATA_PATH)
    return True

def check_for_users():
    all_users = []
    try:
        for file in listdir(USERDATA_PATH):
            if file.endswith(".json"):
                file_path = path.join(USERDATA_PATH, file)
                with open(file_path) as file:
                    all_users.append(loads(file.read()))
    except FileNotFoundError:
        create_user_directory()
        check_for_users()
    return sorted(all_users, key=lambda x: int(x['id']))

def get_user_count():
    return len(check_for_users())

def get_userlist_banner():
    user_count = get_user_count()
    if user_count >= 6:
        return userlist_banners.get(6)
    else:
        return userlist_banners.get(user_count + 1)

def get_highest_id():
    try:
        return int(check_for_users()[::-1][0]["id"])
    except IndexError:
        return 0

def create_json_directory(id):
    return path.join(USERDATA_PATH, f"{id}.json")

def create_user(displayname):
    new_id = get_highest_id() + 1
    user_template = {"id": new_id, 
                     "displayname": displayname, "highscore": {},
                     "gamehistory": []}
    with open(create_json_directory(new_id), "w") as file:
        dump(user_template, file)
        return True

def delete_user(id):
    file = create_json_directory(id)
    if path.exists(file):
        remove(file)
        return True
    return False

