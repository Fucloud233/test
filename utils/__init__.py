import sys

# incorrect
# sys.path.append("./utils")
# from config import Config

# correct
sys.path.append(".")
from utils.config import Config

Config.load_info("config.json")