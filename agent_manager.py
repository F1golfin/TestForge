from parsers import extract_public_signatures
from agents import run_test_case_design, run_test_scenario_build, run_test_code_review
from utils.logger import log_review

import os
import re

class AgentManager:
    def __init__(self, input_path: str, output_path: str = "output/"):
        self.input_path = input_path
        self.output_path = output_path
        self.code = ""
        self.class_name = ""
        self.signatures = []
        self.prompt_structure = ""
        self.test_code = ""

    def load_code(self):
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"❌ Fichier introuvable : {self.input_path}")
        with open(self.input_path, "r", encoding="utf-8") as f:
            self.code = f.read()
        print("Code chargé.")

    def detect_class_name(self, code: str) -> str:
        match = re.search(r'class\s+(\w+)', code)
        return match.group(1) if match else "UnknownClass"

    def analyze_signatures(self):
        self.class_name = self.detect_class_name(self.code)
        self.signatures = extract_public_signatures(self.code, self.class_name)
        print(f"Classe détectée : {self.class_name}")
        print(f"Signatures détectées : {self.signatures}")

    def design_test_cases(self):
        print("\nGénération des cas de test...")
        for signature in self.signatures:
            print(f"Cas pour {signature}")
            cases = run_test_case_design(signature, self.code)
            print(f"Cas générés :\n{cases}\n")
            self.prompt_structure += f"- {signature}\n{cases}\n\n"

    def build_test_file(self, feedback: str = ""):
        print("\nConstruction du fichier de test...")
        self.test_code = run_test_scenario_build(
            self.prompt_structure,
            feedback=feedback
        )

    def review_and_improve(self):
        print("\nDébut de la phase de relecture/amélioration...")
        max_iterations = 3
        iteration = 0

        while iteration < max_iterations:
            iteration += 1
            print(f"Relecture itérative {iteration}...")

            feedback = run_test_code_review(self.test_code, self.code)
            log_review(feedback, prefix=f"review_iter{iteration}")

            print(f"Feedback reçu :\n{feedback}\n")

            print("\nAMELIORATION DU FICHIER DE TEST\n")
            self.build_test_file(feedback=feedback)

    def save_file(self):
        os.makedirs(self.output_path, exist_ok=True)
        file_path = os.path.join(self.output_path, f"Tests{self.class_name}.cs")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.test_code)
        print(f"\n✅ Fichier final sauvegardé : {file_path}")

    def start(self):
        print("Démarrage du processus TestForge...")
        self.load_code()
        print("--------------")
        self.analyze_signatures()
        print("--------------")
        self.design_test_cases()
        print("--------------")
        self.build_test_file()
        print("--------------")
        self.review_and_improve()
        print("--------------")
        self.save_file()
        print("\nProcessus terminé avec succès.")
