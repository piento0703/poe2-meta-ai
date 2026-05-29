import json

with open("data/passive/data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("최상위 키:")
print(data.keys())

print()

print("노드 개수:")
print(len(data["nodes"]))