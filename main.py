#!/usr/bin/env python
import time
import sys
from core import *
from discoIPC import ipc

if __name__ == "__main__":
    print("Starting Nuclear Throne RPC")

    if RUN_TUTORIAL:
        if input("Please confirm that your Stream Key is %s, type Y to continue\n" % STREAM_KEY).lower() != "y":
            sys.exit()
        if input("Please confirm that your Steam64ID is %s, type Y to continue\n" % STEAM_64_ID).lower() != "y":
            sys.exit()

    s = Session(STREAM_KEY, STEAM_64_ID)
    client = ipc.DiscordIPC(DISCORD_CLIENT_ID)
    client.connect()

    print("Started Nuclear Throne RPC")

    while True:
        try:
            s.update()
            client.update_activity(s.generate_presence())
            time.sleep(UPDATE_INTERVAL)
            print("[%s]: Updated Discord with game info" % time.strftime("%X"))
        except KeyboardInterrupt:
            print("Exiting Nuclear Throne RPC")
            client.disconnect()
            sys.exit()
