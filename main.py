from agents.function_mapper import run_function_mapping
from agents.edge_case_agent import run_edge_case_generation

def read_file(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erreur : le fichier {path} est introuvable.")
        exit(1)

def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage : python3 main.py <fichier.cs>")
        exit(1)

    fichier = sys.argv[1]
    code = read_file(fichier)

    print("\n Code analysé :\n")
    print(code)

    resultat_inter = run_function_mapping(code)
    print("\n Résultat intérmédiaire :")
    print(resultat_inter)

    resultat = run_edge_case_generation(resultat_inter)
    print("\n Résultat final :")
    print(resultat)

if __name__ == "__main__":
    main()