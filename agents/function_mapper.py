from crewai import Agent
from ollama_utils import appeler_ollama

# Déclaration de l'agent
function_mapper = Agent(
    role="Explorateur de code C#",
    goal="Analyser une classe C# et identifier ses méthodes publiques avec leurs signatures.",
    backstory=(
        "Tu es un assistant IA expert en C#. Tu aides à extraire proprement les signatures des méthodes pour générer des tests unitaires."
    ),
    verbose=True,
    allow_delegation=False
)

# Fonction d'analyse utilisée dans main.py
def run_function_mapping(code: str) -> str:
    prompt = f"""
Voici une classe C# :

{code}

Liste uniquement les signatures des méthodes publiques sous forme : nom(paramètres), par exemple :
Add(int a, int b)
Multiply(int a, int b)
"""
    return appeler_ollama(prompt)
