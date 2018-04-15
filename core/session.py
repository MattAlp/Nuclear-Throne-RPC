#!/usr/bin/env python
import requests


class Session:
    """Represents a Nuclear Throne game session"""

    characters = ("", "Fish", "Crystal", "Eyes", "Melting", "Plant", "Y.V.", "Steroids",
                  "Robot", "Chicken", "Rebel", "Horror", "Rogue", "Skeleton", "Frog")

    crowns = ("", "No Crown", "Crown of Death", "Crown of Life", "Crown of Haste", "Crown of Guns",
              "Crown of Hatred", "Crown of Blood", "Crown of Destiny", "Crown of Love", "Crown of Risk",
              "Crown of Curses", "Crown of Luck", "Crown of Protection")

    worlds = {100: "Crown Vault", 1: "Desert", 101: "Oasis", 2: "Sewers", 102: "Pizza Sewers", 3: "Scrapyard",
              103: "Y.V's Mansion", 4: "Crystal Caves", 104: "Cursed Crystal Caves", 5: "Frozen City", 105: "Jungle",
              6: "Labs", 7: "The Palace", 0: "Campfire", 107: "Y.V's Crib", 106: "I.D.P.D. Headquarters"}

    api_url = "https://tb-api.xyz/stream/get"

    def __init__(self, key, steam64ID):
        self.key = key
        self.steam64ID = steam64ID
        self.health = 0
        self.character = 0
        self.crown = 0
        self.gameType = 0
        self.loops = 0
        self.timestamp = 0
        self.world = 0
        self.level = 0
        self.skin = 0
        self.kills = 0
        self.characterLevel = 1


    def update(self):
        try:
            info = requests.get(self.api_url, (("s", self.steam64ID), ("key", self.key))).json()
            current = info["current"]
            if current is not None:
                self.character = current["char"]
                self.world = current["world"]
                self.level = current["level"]
                self.crown = current["crown"]
                self.skin = current["skin"]
                self.characterLevel = current["charlvl"]
                self.loops = current["loops"]
                self.kills = current["kills"]
                self.health = current["health"]
                self.gameType = current["type"]
                self.timestamp = current["timestamp"]
            else:
                self.health = 0
                self.character = 0
                self.crown = 0
                self.gameType = 0
                self.loops = 0
                self.timestamp = 0
                self.world = 0
                self.level = 0
                self.skin = 0
                self.kills = 0
                self.characterLevel = 1
        except Exception:
            pass

    def getWorldInfo(self):
        return self.worlds[self.world] + ", Level " + str(self.level) + ", Loop " + str(self.loops)

    def getCharacter(self):
        return self.characters[self.character]

    def getCrown(self):
        return self.crowns[self.crown]

    def isBSkin(self):
        if self.skin == 0:
            return False
        else:
            return True