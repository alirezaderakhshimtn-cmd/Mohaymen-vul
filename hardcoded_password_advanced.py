import os, configparser
config = configparser.ConfigParser()
config.read('settings.ini')
DB_PASS = os.getenv("DB_PASS", config.get("database", "password"))  # fallback if env missing
