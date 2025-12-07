import os
import json

ROOT = "assets/coins"
DB_FILE = "data.json"
EXT = ('.jpg', '.png', '.jpeg', '.webp')
data = []

if not os.path.exists(ROOT):
    os.makedirs(ROOT)

for folder in os.listdir(ROOT):
    path = os.path.join(ROOT, folder)
    if os.path.isdir(path):
        imgs = [f for f in os.listdir(path) if f.lower().endswith(EXT)]
        imgs.sort()
        if imgs:
            data.append({
                "id": folder,
                "name": folder.replace("-", " ").title(),
                "base_path": f"{ROOT}/{folder}/",
                "files": imgs
            })

with open(DB_FILE, 'w') as f:
    json.dump(data, f, indent=2)

print("SUCCESS! Database updated.")