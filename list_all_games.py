import json
import os

with open("all_games.json", "w") as f:
    json.dump(os.listdir("./games"), f)