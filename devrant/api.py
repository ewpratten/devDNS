import requests
import os
from devrant.authtoken import AuthToken


class API:

    def __init__(self, username, password, app_id: int = 3):
        self.app_id = app_id

        data = requests.post("https://devrant.com/api/users/auth-token", data={
                             "username": username, "password": password, "app": self.app_id}).json()

        # Set a new token
        self.token = AuthToken()
        self.token.auth_id = data["auth_token"]["id"]
        self.token.auth_key = data["auth_token"]["key"]
        self.token.user_id = data["auth_token"]["user_id"]

    def isValidUser(self, username: str) -> bool:
        # Query the DB
        data = requests.get("https://devrant.com/api/get-user-id",
                            params={"username": username, "app": self.app_id}).json()

        # Return the success
        return data["success"]

    def getUserID(self, username: str) -> int:
        # Query the DB
        data = requests.get("https://devrant.com/api/get-user-id",
                            params={"username": username, "app": self.app_id}).json()

        # Check success, and return
        if not data["success"]:
            return 00
        else:
            return data["user_id"]

    def getNotifs(self):
        data = requests.get("https://devrant.com/api/users/me/notif-feed", params={"app": self.app_id, "user_id": self.token.user_id, "token_id": self.token.auth_id, "token_key": self.token.auth_key}).json()
        return data
    
    def clearNotifs(self):
        data = requests.delete("https://devrant.com/api/users/me/notif-feed", params={"app": self.app_id, "user_id": self.token.user_id, "token_id": self.token.auth_id, "token_key": self.token.auth_key}).json()
        # print(data)
    
    def postComment(self, rant_id, message):
        requests.post("https://devrant.com/api/devrant/rants/" + str(rant_id) + "/comments", data={"app": self.app_id, "user_id": self.token.user_id, "token_id": self.token.auth_id, "token_key": self.token.auth_key, "comment": message, "plat": 2})
        
    def getComment(self, comment_id):
        return requests.get("https://devrant.com/api/comments/" + str(comment_id), params={"app": self.app_id, "user_id": self.token.user_id, "token_id": self.token.auth_id, "token_key": self.token.auth_key, "plat": 2}).json()
        
password: str
with open(os.path.expanduser("~") + "/.devdnspasswd", "r") as fp:
    password = fp.read().strip()
    fp.close()

dr_api = API("devDNS", password)