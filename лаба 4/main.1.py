import json


def task() -> float:
    with open("input.json", 'r', encoding='utf-8') as f:
        data = json.load(f)

    total = 0.0

    for item in data:
        score = item.get("score", 0)
        weight = item.get("weight", 0)
        total += score * weight

    return round(total, 3)


print(task())