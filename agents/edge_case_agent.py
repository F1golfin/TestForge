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

def run_edge_case_generation(signature: str, feedback: str = "") -> str:
    prompt = f"""
Tu es un générateur de cas de test pour une méthode C#.

Signature :
{signature}

Ta mission :
- Générer des cas normaux et des cas limites/extrêmes
- Ne proposer que des appels à la méthode, pas de texte explicatif
- Si un retour de review est fourni, prends-en compte pour améliorer ou corriger les cas

{"Voici un retour d'un reviewer à prendre en compte :" if feedback else ""}
{feedback}

Format attendu :

Cas normaux :
- Méthode(...)

Cas limites :
- Méthode(...)
"""
    return appeler_ollama(prompt)
