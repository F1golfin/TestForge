from crewai import Agent
from ollama_utils import appeler_ollama

# Agent pour générer des tests NUnit 3 en C#
unit_test_writer = Agent(
    role="Rédacteur de tests NUnit",
    goal="Générer un fichier de tests unitaires NUnit 3 complet pour une méthode C#.",
    backstory=(
        "Tu es un assistant IA spécialisé en test logiciel. Tu prends une méthode et des cas d'entrée pour écrire "
        "des tests clairs, bien structurés, en utilisant NUnit 3. Tu formates tout dans un fichier .cs propre."
    ),
    verbose=True,
    allow_delegation=False
)

def run_test_writer(class_name: str, signature: str, test_cases: str, feedback: str = "") -> str:
    prompt = f"""
Tu es un générateur de tests C# utilisant NUnit 3.

Nom de la classe à tester : {class_name}
Signatures et cas de test :

{test_cases}

{"Voici un retour d'un reviewer sur ta première version :" if feedback else ""}
{feedback}

Consignes strictes :
- Si la classe est `static`, n'instancie jamais d'objet. Appelle les méthodes directement avec `NomClasse.Methode(...)`.
- Utilise `[TestCase(..., ExpectedResult = ...)]` quand c’est possible.
- Évite les champs privés ou `[SetUp]` si la classe est statique.
- Une seule classe de test nommée `Test{class_name}` dans le namespace `Tests`.
- Pas de commentaires, pas de texte explicatif, uniquement le code C#.

Retourne uniquement un fichier compilable en C#, sans fioritures.
"""
    return appeler_ollama(prompt)