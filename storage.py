import os
FILE_NAME = "data/users.txt"
def create_data_folder():
    if not os.path.exists("data"):
        os.makedirs("data")
def save_user(username, password):
    create_data_folder()
    with open(FILE_NAME, "w") as file:
        file.write(username + "|" + password)
