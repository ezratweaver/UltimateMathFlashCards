from cryptography.fernet import Fernet, InvalidToken

encryption_key = b'ncp8-C_CMnbIGbPc6Tp8IorVNHuRojhPggWg-l0-ltI='

fernet_instance = Fernet(encryption_key)