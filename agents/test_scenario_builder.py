from ollama_utils import appeler_ollama

def run_test_scenario_build(test_cases: str, feedback: str = "") -> str:
    prompt = f"""
Tu es un générateur de fichiers de tests unitaires C# utilisant NUnit 3.

Voici les cas de test générés (à utiliser sans changer leur intention) :

{test_cases}

Ta mission :

Générer une classe de tests propre et compilable.

Utiliser le framework NUnit 3 ([TestFixture], [Test], [TestCase], Assert...).

Organiser les cas normaux et limites en méthodes de test séparées.

Respecter strictement la logique et les signatures des méthodes existantes.

Ne jamais inventer de nouvelles méthodes ou nouveaux paramètres.

Si un feedback est fourni, l'utiliser pour améliorer encore la génération.

{f"Voici un feedback à appliquer pour améliorer :\n{feedback}" if feedback else ""}

Format attendu :

Une seule classe de tests

Code C# compilable directement

Aucun commentaire ou explication

Important :

Utilise exactement les méthodes telles qu'elles sont définies.

Pas de changement de signature, pas d'ajout de paramètres inexistants. """
    return appeler_ollama(prompt, modele="codegemma:7b-instruct-v1.1-q8_0")