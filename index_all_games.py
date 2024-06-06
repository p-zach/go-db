import os

all_games = os.listdir("./games_named")

for i, game in enumerate(all_games):
    with open(f"./games_named/{game}", "r", encoding='utf-8') as og_file:
        with open(f"./games_indexed/{i}.sgf", "w", encoding='utf-8') as new_file:
            new_file.writelines(og_file.readlines())