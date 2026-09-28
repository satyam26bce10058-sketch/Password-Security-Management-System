import os
FILE_NAME = "data/users.txt"
def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")
def save_user(username, password):
    create_data_folder()
    with open(FILE_NAME, "w") as file:
        file.write(username + "|" + password)
def load_user():
    create_data_folder()
    if not os.path.exists(FILE_NAME):
        return None, None
    with open(FILE_NAME, "r") as file:
        data = file.read().strip()
    if data == "":
        return None, None
    parts = data.split("|")
    if len(parts) == 2:
        return parts[0], parts[1]
    return None, None
def update_user(username, password):
    save_user(username, password)
