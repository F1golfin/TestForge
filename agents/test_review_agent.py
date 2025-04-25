from crewai import Agent
from ollama_utils import appeler_ollama

test_review_agent = Agent(
    role="Critique IA des cas de test",
    goal="Relire les cas de test proposés et suggérer des améliorations utiles et exploitables.",
    backstory=(
        "Tu es un expert en validation logicielle. Tu relis les cas de test pour évaluer leur qualité, détecter des manques et proposer des cas plus pertinents ou extrêmes."
    ),
    verbose=True,
    allow_delegation=False
)

def run_test_case_review(signature: str, test_cases: str) -> str:
    prompt = f"""
Tu es un expert en validation logicielle. Voici une méthode C# :

Signature :
{signature}

Et les cas de test générés automatiquement :

{test_cases}

Ta mission :
1. Évaluer la qualité des cas de test proposés : sont-ils pertinents, variés, suffisants ?
2. Identifier les cas absents ou mal choisis (ex : 0, null, max/min, égalités)
3. Expliquer brièvement les points forts et les manques
---

Évaluation :
- [ta remarque sur les cas existants]

Recommandations :
- [liste d'idées ou corrections utiles]


Sois clair et utile.
"""
    return appeler_ollama(prompt)

def run_test_code_review(test_code: str) -> str:
    prompt = f"""
Tu es un expert en qualité logicielle et en tests unitaires C# avec NUnit 3.

Voici un fichier de tests généré automatiquement :

{test_code}

Ta mission :
1. Évaluer sa clarté, sa cohérence, et la couverture des cas testés.
2. Indiquer les bonnes pratiques suivies ou manquantes.
3. Proposer des corrections ou suggestions d’amélioration précises.

Retourne ta réponse dans ce format :

📝 Évaluation :
- [tes remarques sur le fichier]

📌 Suggestions :
- [recommandations concrètes pour améliorer le fichier]
"""
    return appeler_ollama(prompt)