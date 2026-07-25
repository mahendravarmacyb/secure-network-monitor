from utils.config import Config

config = Config()

print("Default Network:", config.get("default_network"))
print("Database:", config.get("database"))
print("Log File:", config.get("log_file"))
