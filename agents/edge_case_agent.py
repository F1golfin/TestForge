from crewai import Agent
from ollama_utils import appeler_ollama

# Déclaration de l’agent
edge_case_agent = Agent(
    role="Générateur de cas limites",
    goal="Créer des cas de test normaux et extrêmes pour une méthode donnée.",
    backstory=(
        "Tu es un assistant IA spécialisé en validation de code. Tu proposes des cas classiques et des cas limites "
        "pour tester la robustesse des méthodes C# en entrée, en respectant leurs types d'arguments."
    ),
    verbose=True,
    allow_delegation=False
)

# Fonction appelée depuis main.py ou une autre étape
def run_edge_case_generation(signature: str) -> str:
    prompt = f"""
Voici une signature de méthode C# :
{signature}

Propose des cas de test à utiliser avec cette méthode, dans deux catégories :
1. Cas normaux
2. Cas limites ou exceptionnels

Présente les résultats au format :
Cas normaux :
- Méthode(...)

Cas limites :
- Méthode(...)
"""
    return appeler_ollama(prompt)
