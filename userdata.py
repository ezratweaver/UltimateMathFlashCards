from os import listdir, path, getenv, mkdir, remove
from typing import List, Optional
from json import loads, dump
from assets import userlist_banners

USERDATA_PATH = path.join(getenv('APPDATA'), "ultimate-mfc")

def create_user_directory() -> Optional[bool]:
    """
    Creates the user directory for storing userdata.

    Returns:
        Optional[bool]: Returns True if the directory is created successfully. 
        Otherwise, returns None.

    """
    try:
        mkdir(USERDATA_PATH)
        return True
    except FileExistsError:
        return None

def check_for_users() -> List[dict]:
    """
    Checks USERDATA_PATH for JSON files and returns all JSON files
    as a list of dictionaries.

    Returns:
        List[Dict]: List of dictionaries representing the JSON files found

    Raises:
        FileNotFoundError: If USERDATA_PATH does not exist

    """
    all_users = []
    try:
        for file in listdir(USERDATA_PATH):
            if file.endswith(".json"):
                file_path = path.join(USERDATA_PATH, file)
                with open(file_path) as file:
                    all_users.append(loads(file.read()))
    except FileNotFoundError:
        create_user_directory()
        return all_users
    return sorted(all_users, key=lambda x: int(x['id']))

def get_user_count() -> int:
    """
    Returns the count of users by retrieving the length of the list of users.

    Returns:
        int: The count of users.

    """
    return len(check_for_users())

def get_userlist_banner() -> object:
    """
    Retrieves the appropriate user list banner based on the count of users.

    Returns:
        object[PhotoImage]: Tkinter Image with proper banner size

    """
    user_count = get_user_count()
    if user_count >= 6:
        return userlist_banners.get(6)
    else:
        return userlist_banners.get(user_count + 1)

def get_highest_id() -> int:
    """
    Retrieves the highest ID among the users.

    Returns:
        int: The highest ID value.

    Raises:
        IndexError: Handles the case when no users are found. Returns integer 0

    """
    try:
        return int(check_for_users()[::-1][0]["id"])
    except IndexError:
        return 0

def create_json_directory(id: int) -> str:
    """
    Creates the JSON file directory path for a given ID.

    Args:
        id (int): The ID used to generate the JSON file directory path.

    Returns:
        str: The JSON file directory path.

    """
    return path.join(USERDATA_PATH, f"{id}.json")

def create_user(displayname: str) -> bool:
    """
    Creates a new user with the provided display name.

    Args:
        displayname (str): The display name of the user.

    Returns:
        bool: True if the user is successfully created.

    """
    new_id = get_highest_id() + 1
    user_template = {"id": new_id, 
                     "displayname": displayname, "highscore": {},
                     "gamehistory": []}
    with open(create_json_directory(new_id), "w") as file:
        dump(user_template, file, indent=4)
        return True

def delete_user(id: int) -> bool:
    """
    Deletes the user with the specified ID.

    Args:
        id (int): The ID of the user to delete.

    Returns:
        bool: True if the user is successfully deleted, False otherwise.

    """
    file = create_json_directory(id)
    if path.exists(file):
        remove(file)
        return True
    return False

def rename_user(user_dictionary: dict, displayname: str) -> dict:
    """
    Renames the display name of a user within the provided user dictionary.

    Args:
        user_dictionary (dict): The dictionary representing the user.
        displayname (str): The new display name for the user.

    Returns:
        dict: The updated user dictionary with the new display name.

    """
    user_dictionary["displayname"] = displayname
    return user_dictionary

def dump_user_file(user_dictionary: dict) -> bool:
    """
    Dumps the user dictionary to a JSON file.

    Args:
        user_dictionary (dict): The dictionary representing the user.

    Returns:
        bool: True if the user dictionary is successfully dumped to the JSON file, 
        False otherwise.

    """
    file = create_json_directory(user_dictionary["id"])
    if path.exists(file):
        with open(file,"w") as json:
            dump(user_dictionary, json, indent=4)
            return True
    return False
