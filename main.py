# On interval:
# Get notifs
# clear notifs
# spin off thread for each comment with valid request
# respond to ewpratten's status command

import time

from devrant.api import dr_api
from queryctl.dispatcher import dispatch

# We create a lastCheckTime variable, which holds the time when we last checked the notifications...
lastCheckTime = time.time()

while True:
    print("Running loop")
    
    # ...and before we grab the notifications, we store our current lastCheckTime in checkTime and overwrite it with the current time
    checkTime = int(lastCheckTime)
    lastCheckTime = time.time()
    
    notifs = dr_api.getNotifs()
    # > Between these two function calls is a millisecond where notifications get abandoned! <
    dr_api.clearNotifs()

    for notif in notifs["data"]["items"]:
        if notif["type"] == "comment_mention" and notif["created_time"] > checkTime: # Now we only have check if the notification is a new one
            dispatch(notif).start()
        
    time.sleep(10)
