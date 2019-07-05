# On interval:
# Get notifs
# clear notifs
# spin off thread for each comment with valid request
# respond to ewpratten's status command

import time

from devrant.api import dr_api
from queryctl.dispatcher import dispatch

while True:
    print("Running loop")
    notifs = dr_api.getNotifs()
    dr_api.clearNotifs()

    for notif in notifs["data"]["items"]:
        if notif["type"] == "comment_mention" and notif["read"] == 0:
            dispatch(notif).start()
    
    time.sleep(10)