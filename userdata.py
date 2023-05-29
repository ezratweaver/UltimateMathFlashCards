from os import listdir, path, getenv, mkdir
from json import loads, dumps

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
    return all_users

all_users = check_for_users()
