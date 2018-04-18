#!/usr/bin/env python
import requests


class Session:
    """Represents a Nuclear Throne game session"""

    characters = ("", "Fish", "Chrystal", "Eyes", "Melting", "Plant", "Y.V.", "Steroids",
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
        except Exception as e:
            print("[ERROR]: " + str(e))
            print("[IMPORTANT]: Check if your stream key and steam ID are properly set in config.ini")

    def get_world_info(self):
        return "%s %i, Loop %i, %s Run" %(self.worlds[self.world], self.level, self.loops, self.gameType.capitalize())

    def get_character(self):
        return self.characters[self.character]

    def get_crown(self):
        return self.crowns[self.crown]

    def is_b_skin(self):
        if self.skin == 0:
            return False
        else:
            return True

    def generate_presence(self):
        if self.character != 0:
            game_activity = {
                'state': self.get_world_info(),
                'details': 'HP: ' + str(self.health) + ' / Kills: ' + str(self.kills),
                'timestamps': {
                    'start': self.timestamp
                },
                'assets': {
                    'large_image': ''.join(ch for ch in self.get_character() if ch.isalnum()).lower(),
                    'large_text': self.get_character() + ', level ' + str(self.characterLevel),
                    'small_image': self.get_crown().replace(" ", "_").lower(),
                    'small_text': self.get_crown()
                }
            }
            if self.is_b_skin():
                game_activity['assets']['large_image'] += '_b'
                if self.world == 5:  # Frozen City for 3rd Rebel Skin
                    game_activity['assets']['large_image'] += '_fc'
            if self.character == 9 and self.health == 0:  # Headless Chicken skin before death
                game_activity['assets']['large_image'] = 'chicken_x'

        else:
            game_activity = {
                'state': 'In Main Menu',
                'assets': {
                    'large_image': 'main',
                    'large_text': 'Fläshyn!'
                }
            }
        return game_activity
