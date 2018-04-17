#!/usr/bin/env python
import time
from core import Session, STREAM_KEY, STEAM_64_ID, DISCORD_CLIENT_ID, UPDATE_INTERVAL
from discoIPC import ipc

if __name__ == "__main__":
    print("Starting Nuclear Throne RPC")

    if input("Please confirm that your Stream Key is %s, type Y to continue\n" % STREAM_KEY).lower() != "y":
        exit()
    if input("Please confirm that your Steam64ID is %s, type Y to continue\n" % STEAM_64_ID).lower() != "y":
        exit()

    s = Session(STREAM_KEY, STEAM_64_ID)
    client = ipc.DiscordIPC(DISCORD_CLIENT_ID)
    client.connect()

    print("Started Nuclear Throne RPC")

    while True:
        try:
            s.update()
            client.update_activity(s.generate_presence())
            time.sleep(UPDATE_INTERVAL)
            print("[%s]: Updated Discord" % time.strftime("%X"))
        except KeyboardInterrupt:
            print("Exiting Nuclear Throne RPC")
            client.disconnect()
            exit()
