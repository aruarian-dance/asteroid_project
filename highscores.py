import json
from pathlib import Path

HIGHSCORES_FILE = Path("highscores.json")
MAX_SCORES = 5

def load_highscores():
    if not HIGHSCORES_FILE.exists():
        return []
    try:
        with HIGHSCORES_FILE.open("r") as f:
            return json.load(f)
    except Exception:
        return []
    
def save_highscores(scores):
    scores = sorted(scores, reverse=True)[:MAX_SCORES]
    with HIGHSCORES_FILE.open("w") as f:
        json.dump(scores, f)
    
def add_score(score):
    scores = load_highscores()
    scores.append(score)
    save_highscores(scores)