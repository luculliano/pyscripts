import os
import json

keys = ("name", "surname", "age", "nationality", "education")
values = ("John", "Johns", 33, "USA", "software engineer")
my_obj = dict(zip(keys, values))
path = os.path.join("/home", os.getenv("USER"), "Desktop")


with open(os.path.join(path, "data.json"), "w", encoding="utf-8") as file:
    for i in range(1400000):
        json.dump(my_obj, file, indent=3)
        file.write("\n\n")

os.system(f"du -bh {os.path.join(path, 'data.json')}")
