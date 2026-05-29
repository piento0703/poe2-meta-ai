import json
from pathlib import Path
from pprint import pprint

DATA_PATH = Path("data/passive/data.json")

with DATA_PATH.open("r", encoding="utf-8") as f:
    data = json.load(f)

nodes = data["nodes"]

print("nodes 타입:", type(nodes))
print("노드 개수:", len(nodes))
print("=" * 80)

for node_id, node in nodes.items():
    # 이름/효과/스탯이 있을 가능성이 있는 노드만 찾기
    keys = set(node.keys())
    if {"name", "stats", "sd", "dn", "skill"}.intersection(keys):
        print("찾은 노드 ID:", node_id)
        print("키 목록:", node.keys())
        print("전체 구조:")
        pprint(node)
        break
else:
    print("name/stats/sd/dn/skill 키를 가진 노드를 못 찾음")