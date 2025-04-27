import os
from datetime import datetime

def log_review(content: str, prefix: str = "review"):
    # Crée le dossier logs/ si besoin
    os.makedirs("logs", exist_ok=True)

    # Nom du fichier basé sur la date/heure
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"logs/{prefix}_{timestamp}.txt"

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Log sauvegardé dans {filename}")