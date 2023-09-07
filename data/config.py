import configparser
import json

config = configparser.ConfigParser()
config.read("settings.ini")

BOT_TOKEN = config["settings"]["token"]