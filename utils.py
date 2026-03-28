import json

def load_data():
    try:
        with open("data.json", "r") as file:
            return json.load(file)
    except:
        return []

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def calculate_score(planned, studied):
    if planned <= 0:
        return 0
    score = (studied / planned) * 100
    if score > 100:
        score = 100
    if score < 0:
        score = 0
    return round(score, 2)