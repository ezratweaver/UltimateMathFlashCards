import os
import platform
import json
from typing import List
from cryptography.fernet import InvalidToken
from encryption import fernet_instance

MAX_USERS = 6
USERDATA_TEMPLATE = {"id": "",
                     "displayname": "", "highscore": {},
                     "gamehistory": []}
USERDATA_FOLDER_NAME = ".ultimate-mfc"
ENCRYPTION_STATE = False


if platform.system() == "Windows": 
    USERDATA_PATH = os.path.join(os.getenv('APPDATA'), USERDATA_FOLDER_NAME)
elif platform.system() == "Linux":
    USERDATA_PATH = os.path.join(os.path.expanduser("~"), USERDATA_FOLDER_NAME)
else:
    USERDATA_PATH = "./"


class TamperError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class EncryptionError(Exception):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def check_for_users(encryption=ENCRYPTION_STATE) -> List[dict]:
    """
    Checks USERDATA_PATH for JSON files and returns all JSON files
        as a list of dictionaries.

    Args:
        encryption (bool): Flag indicating whether data is encrypted.

    Returns:
        List[Dict]: List of dictionaries representing the JSON files found

    Raises:
        EncryptionError: if encryption bool does not match the state of encryption of json files
        TamperError: if files have been tampered or are syntaxically incorrect
        ValueError: if user count is greater then MAX_USERS constant

    """ 
    all_users = []
    try:
        for file in os.listdir(USERDATA_PATH):
            if file.endswith(".json"):
                file_path = os.path.join(USERDATA_PATH, file)
                with open(file_path) as file:
                    file = file.read()
                    if file == "":
                        continue
                    if encryption is True:
                        try:
                            file = fernet_instance.decrypt(file.encode())
                        except InvalidToken:
                            try:
                                dictionary = json.loads(file)
                            except json.JSONDecodeError:
                                raise TamperError(
                                    f"{file_path} is has been tampered")
                            raise EncryptionError(f"userfile {file_path} is decrypted; "
                        f"\n                 ENCRYPTION_STATE = {ENCRYPTION_STATE}; "
                        "Expected: ENCRYPTION_STATE = False")
                        try:
                            dictionary = json.loads(file)
                        except json.JSONDecodeError:
                                raise TamperError(f"JSON file {file_path} "
                                "has been tampered or are sytaxically incorrect")
                    if encryption is False:
                        try:
                            file = fernet_instance.decrypt(file.encode())
                            raise EncryptionError(f"userfile {file_path} is encrypted; "
                        f"\n                 ENCRYPTION_STATE = {ENCRYPTION_STATE}; "
                        "Expected: ENCRYPTION_STATE = True")
                        except InvalidToken:
                            try:
                                dictionary = json.loads(file)
                            except json.JSONDecodeError:
                                raise TamperError(f"JSON file {file_path} "
                                "has been tampered or is sytaxically incorrect")
                    if check_dictionary(dictionary) is False:
                        raise TamperError(f"JSON file {file_path} "
                                            "has been tampered")
                    all_users.append(dictionary)
    except FileNotFoundError:
        os.mkdir(USERDATA_PATH)
        return all_users
    if len(all_users) > MAX_USERS:
        raise ValueError(f"Total users: {len(all_users)} exceeds maximum allowed "
                         f"users: {MAX_USERS}")
    return sorted(all_users, key=lambda x: int(x['id']))


def dump_user(user_dictionary: dict, encryption=ENCRYPTION_STATE) -> bool:
    """
    Dumps the user dictionary to a JSON file.

    This function takes a dictionary representing a user and writes it to a JSON
    file. The user dictionary should contain the necessary information for the user,
    such as their ID, display name, high scores, and game history.

    Args:
        user_dictionary (dict): The dictionary representing the user.

    Returns:
        bool: True if the user dictionary is successfully dumped to the JSON file,
                False otherwise.

    Calls:
        - mk_json_directory_string: Constructs the directory path for the user's
                                        JSON file.
        - check_dictionary: Checks if dictionary conforms to dictionary template
    """
    if not isinstance(user_dictionary, dict):
        raise TypeError(
            f"Expected dictionary type, but received {type(user_dictionary).__name__}")
    if not check_dictionary(user_dictionary):
        raise SyntaxError(
            "Recieved dictionary does not conform the set template")
    dir = mk_json_directory_string(user_dictionary["id"])
    with open(dir, "w") as file:
        if encryption:
            user_json = json.dumps(user_dictionary)
            encrypted_data = fernet_instance.encrypt(user_json.encode()).decode()
            file.write(encrypted_data)
        else:
            json.dump(user_dictionary, file, indent=4)
        return True


def create_user(displayname: str, encryption=ENCRYPTION_STATE) -> bool:
    """
    Creates a new user with the provided display name.

    Args:
        displayname (str): The display name of the user.

    Returns:
        bool: True if the user is successfully created.

    Calls:
        check_username: checks validity of name used.
        get_highest_id: Retrieves the highest ID among existing users.
        mk_json_directory_string: Constructs the directory path for the 
                                user's JSON file.
    """
    check_username(displayname)
    new_id = (get_highest_id() + 1)
    user_template = USERDATA_TEMPLATE.copy()
    user_template["id"] = new_id
    user_template["displayname"] = displayname
    with open(mk_json_directory_string(new_id), "w") as file:
        if encryption:
            user_json = json.dumps(user_template)
            encrypted_data = fernet_instance.encrypt(user_json.encode()).decode()
            file.write(encrypted_data)
        else:
            json.dump(user_template, file, indent=4)
        return True


def remove_user(user_dictionary: dict) -> bool:
    """
    Remove user from the system.

    Args:
        user_dictionary (dict): Dictionary containing user information.

    Returns:
        bool: True if the user was successfully removed, False otherwise.

    Calls:
        mk_json_directory_string: To create a directory of the user file.
    """
    file = mk_json_directory_string(user_dictionary["id"])
    if os.path.exists(file):
        os.remove(file)
        return True
    return False


def get_user_count() -> int:
    """
    Returns the count of users by retrieving the length of the list of users.

    Returns:
        int: The count of users.

    Calls:
        check_for_users: to grab the length of the total users found

    """
    return len(check_for_users())


def get_userlist_banner(usercount, banner_dictionary) -> object:
    """
    Retrieves the appropriate user list banner based on the count of users.

    Args:
        usercount (int): Total number of users for which the proper banner is needed.
        banner_dictionary (dict): A dictionary mapping the number of users to the
                                    corresponding banner image.

    Returns:
        object: A Tkinter PhotoImage object representing the banner
                                    image with the proper size.

    """
    if usercount >= 6:
        return banner_dictionary.get(6)
    else:
        return banner_dictionary.get(usercount + 1)


def get_highest_id() -> int:
    """
    Retrieves the highest ID among the users.

    Returns:
        int: The highest ID value.

    Raises:
        IndexError: Handles the case when no users are found. Returns integer 0

    Calls:
        check_for_users: to sift through the users to find highest id
    """
    try:
        return int(check_for_users()[::-1][0]["id"])
    except IndexError:
        return 0


def mk_json_directory_string(id: int) -> str:
    """
    Creates the JSON file directory path for a given ID.

    Args:
        id (int): The ID used to generate the JSON file directory path.

    Returns:
        str: The JSON file directory path.

    """
    return os.path.join(USERDATA_PATH, f"{int(id)}.json")


def rename_user(user_dictionary: dict, displayname: str) -> dict:
    """
    Renames the display name of a user within the provided user dictionary.

    Args:
        user_dictionary (dict): The dictionary representing the user.
        displayname (str): The new display name for the user.

    Returns:
        dict: The updated user dictionary with the new display name.

    Calls:
        check_username: checks if username falls under set standards

    """
    check_username(displayname)
    user_dictionary["displayname"] = displayname
    return user_dictionary


def check_dictionary(dictionary: dict) -> bool:
    """
    Check if all keys from USERDATA_TEMPLATE are present in the given dictionary.

    Args:
        dictionary (dict): The dictionary to be checked.

    Returns:
        bool: True if all keys are present, False otherwise.
    """
    for key, _ in USERDATA_TEMPLATE.items():
        if key not in dictionary:
            return False
    return True


def check_username(displayname: str):
    """
    Checks the validity of a display name.

    Args:
        displayname (str): The display name to be checked.

    Raises:
        TypeError: If the display name is not a string.
        ValueError: If the display name length exceeds 14 characters.
    """
    if not isinstance(displayname, str):
        raise TypeError("Expected string type for display name, "
                        f"but received {type(displayname).__name__} instead")
    if len(displayname) > 14:
        raise ValueError("Expected length of display name to be <= 14, "
                        f"actual name length: {len(displayname)}")


if __name__ == "__main__":
    print(check_for_users())

