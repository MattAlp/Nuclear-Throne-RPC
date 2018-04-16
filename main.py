#!/usr/bin/env python
import time
from core import Session, STREAM_KEY, STEAM_64_ID, DISCORD_CLIENT_ID, UPDATE_INTERVAL
from discoIPC import ipc

if __name__ == "__main__":
    print("Starting Nuclear Throne RPC")
    client = ipc.DiscordIPC(DISCORD_CLIENT_ID)
    client.connect()
    if STREAM_KEY != "" and STEAM_64_ID != "":
        s = Session(STREAM_KEY, STEAM_64_ID)
    else:
        print("[IMPORTANT]: Either your stream key or your Steam64ID are not set, please update config.py")
        exit()

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
