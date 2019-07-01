from threading import Thread
import dns.resolver
from devrant.api import dr_api

class CommentThread(Thread):

    def __init__(self, notif):
        self.notif = notif
        Thread.__init__(self)
        self.resolver = dns.resolver.Resolver()
    
    def run(self):
        rant_id = self.notif["rant_id"]
        if len(self.notif["comment"]["body"].split(" ")) == 2:
            domain = self.notif["comment"]["body"].split(" ")[1]
            record_type = "A"
        else:
            domain = self.notif["comment"]["body"].split(" ")[2]
            record_type = self.notif["comment"]["body"].split(" ")[1]
        user = self.notif["comment"]["user_username"]

        print(f"{user} requested lookup for {domain} in rant {rant_id}")

        try:
            records = self.resolver.query(domain, record_type)
        except:
            # Failed
            return

        record_str = ""
        for record in records:
            record_str += str(record) + "\n"

        dr_api.postComment(rant_id, f"@{user} \nThe {record_type} records for {domain} are: \n{record_str}")
        