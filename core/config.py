import configparser

config = configparser.ConfigParser()
config.read("config.ini")

STREAM_KEY = config.get("USER_SETTINGS", "STREAM_KEY")
STEAM_64_ID = config.get("USER_SETTINGS", "STEAM_64_ID")
DISCORD_CLIENT_ID = config.get("DEVELOPER_SETTINGS", "DISCORD_CLIENT_ID")
UPDATE_INTERVAL = config.getint("DEVELOPER_SETTINGS", "UPDATE_INTERVAL")
RUN_TUTORIAL = config.getboolean("USER_SETTINGS", "RUN_TUTORIAL")