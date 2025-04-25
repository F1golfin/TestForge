from agents.edge_case_agent import run_edge_case_generation
from agents.unit_test_writer import run_test_writer
from agents.test_review_agent import run_test_case_review, run_test_code_review
from parsers.csharp_parser import extract_public_signatures

import re
import sys
import os


def charger_code_source() -> str:
    if len(sys.argv) < 2:
        print("Usage : python3 main.py <fichier.cs>")
        exit(1)

    fichier = sys.argv[1]
    if not os.path.exists(fichier):
        print(f"Erreur : le fichier {fichier} est introuvable.")
        exit(1)

    with open(fichier, "r", encoding="utf-8") as f:
        return f.read()

def detect_class_name(code: str) -> str:
    match = re.search(r'class\s+(\w+)', code)
    return match.group(1) if match else "UnknownClass"

def main():
    code = charger_code_source()

    # Détection du nom de la classe
    class_name = detect_class_name(code)
    print(f"\n Classe détectée : {class_name}")

    print("\n Étape 1 : Extraction des méthodes\n")
    signatures = extract_public_signatures(code, class_name)
    print("\n Signatures détectées :", signatures)

    # Construction du prompt pour UnitTestWriter
    """prompt_structure = ""
    for signature in signatures:
        print(f"\n Génération initiale des cas pour : {signature}")
        test_cases = run_edge_case_generation(signature)
        print(f"\n Cas initiaux :\n{test_cases}")

        # Relecture IA des cas
        review = run_test_case_review(signature, test_cases)
        print(f"\n Retour du reviewer :\n{review}")

        # Reprise des cas avec retour IA
        test_cases = run_edge_case_generation(signature, feedback=review)

        prompt_structure += f"- {signature}\n{test_cases}\n\n"

    

    # Génération des tests
    print("\n Génération du fichier de test...")
    test_code = run_test_writer(class_name, "Méthodes multiples", prompt_structure)

    # Relecture IA du code généré (2e boucle)
    print("\n Relecture IA du code de test généré...")
    review_code = run_test_code_review(test_code)
    print(f"\n Suggestions IA :\n{review_code}")

    # Réécriture finale des tests
    print("\n Réécriture finale avec suggestions...")
    test_code_improved = run_test_writer(class_name, "Méthodes multiples", prompt_structure, feedback=review_code)

    # Écriture dans un fichier
    output_path = f"output/Tests{class_name}.cs"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(test_code_improved)

    print(f"\n✅ Fichier final généré : {output_path}")"""


if __name__ == "__main__":
    main()
