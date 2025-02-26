import json

file_path = "../data/AllCards.json"

# Read first few lines to inspect structure
with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Print first record (if it's a list) or entire structure
# if isinstance(data, list):
#     print(json.dumps(data[0], indent=2))
# else:
#     print(json.dumps(data, indent=2))

data_list = list(data.values())

# Save back to a new JSON file
with open("../data/AllCards_list.json", "w", encoding="utf-8") as f:
    json.dump(data_list, f, indent=2)

print('Format Change Complete!')