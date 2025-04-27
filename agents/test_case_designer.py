from ollama_utils import appeler_ollama

def run_test_case_design(signature: str, class_code: str) -> str:
    prompt = f"""
Tu es un expert en conception de cas de test pour C# (framework NUnit 3).

Voici la définition de la classe complète sur laquelle tu travailles :

{class_code}

Et voici la méthode spécifique à tester :

Signature : {signature}

Ta mission :

Générer des cas de test normaux ET des cas limites
Respecter strictement la logique et le comportement attendu de la méthode
Utiliser uniquement des paramètres valides
Ne jamais inventer de nouveaux paramètres ou comportements
Si un paramètre est une chaîne, entoure-la de guillemets.
Respecte les types exacts de la signature.

Format attendu :

Cas normaux :

NomMethode(...)

Cas limites :

NomMethode(...)

Aucun commentaire, aucun texte explicatif. Retourne uniquement ce format strict.
"""
    return appeler_ollama(prompt, modele="codegemma:7b-instruct-v1.1-q8_0")