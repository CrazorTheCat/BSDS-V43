import cProfile, pstats, sys
import time
import threading
import traceback

from Discord import Discord
from Discord.enum import *
from Discord.model import *

def callback(result):
    if result == Result.Ok:
        print("Successfully set the activity!")
    else:
        raise Exception(result)

class DiscordCore(threading.Thread):
    def __init__(self):
        super().__init__()
        self.app = Discord(952269444405682207, CreateFlags.NoRequireDiscord)
        self.activityManager = self.app.GetActivityManager()
        self.userManager = self.app.GetUserManager()

        self.currentUser = None

        def onCurrUserUpdate():
            self.currentUser = self.userManager.GetCurrentUser()
            print(f"Current user : {self.currentUser.Username}#{self.currentUser.Discriminator}")
    
        self.userManager.OnCurrentUserUpdate = onCurrUserUpdate

        self.activity = Activity()
        self.activity.State = "Playing BSDS"
        self.activity.Secrets.Join = "my_super_secret"
        
        self.activityManager.UpdateActivity(self.activity, callback)

    def run(self):
        try:
            while 1:
                time.sleep(1/10)
                self.app.RunCallbacks()

        except Exception:
            print(traceback.format_exc())