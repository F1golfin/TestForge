from ollama_utils import appeler_ollama

def run_test_code_review(test_code: str, class_code: str) -> str:
    prompt = f"""
Tu es un expert en qualité logicielle et en tests unitaires C# utilisant NUnit 3.

Voici le fichier de tests généré :

{test_code}

Et voici la définition complète de la classe à tester :

{class_code}

Ta mission d'expert :

Vérifier que toutes les méthodes appelées dans les tests correspondent exactement aux méthodes publiques de la classe.

Vérifier que le nombre et le type des paramètres sont respectés.

Signaler toute méthode inventée, tout paramètre incohérent ou tout comportement improbable.

Évaluer la qualité générale des tests (couverture, cas limites, robustesse).

Format obligatoire de réponse :

Évaluation générale :

[résumé des points positifs et négatifs]

Problèmes détectés :

[liste des erreurs techniques repérées : méthodes inexistantes, mauvais types, mauvaise signature, etc.]

(Si aucun problème technique, écrire "Aucun problème technique détecté.")

Suggestions générales :

[liste d'améliorations possibles même si techniquement correct]

Ne pas ajouter de commentaire hors structure demandée. Retourne uniquement les sections demandées. """
    return appeler_ollama(prompt, modele="codegemma:7b-instruct-v1.1-q8_0")