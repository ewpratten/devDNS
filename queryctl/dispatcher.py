from queryctl.commentthread import CommentThread
from devrant.api import dr_api

count = 0

class Dummy:

    def start(self):
        pass

def dispatch(notif):
    global count

    notif["comment"] = dr_api.getComment(notif["comment_id"])["comment"]

    if notif["comment"]["body"].split(" ")[1] == "status" and notif["comment"]["user_username"] == "ewpratten":
        dr_api.postComment(notif["rant_id"], f"@ewpratten \nI have served {count} requests since last reboot")
        return Dummy()

    if len(notif["comment"]["body"].split(" ")) > 1:
        count += 1
        return CommentThread(notif)
    else:
        return Dummy()