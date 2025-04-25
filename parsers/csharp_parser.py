import re

def extract_public_signatures(csharp_code: str, class_name: str) -> list[str]:
    """
    Extrait toutes les signatures publiques (et publiques statiques) d'un code C# donné.
    Retourne une liste de signatures sous forme : NomMethode(parametres)
    """
    signatures = []

    # Constructeur (public uniquement)
    constructor_pattern = rf'public\s+{class_name}\s*\(([^)]*)\)'
    for params in re.findall(constructor_pattern, csharp_code):
        clean_params = ' '.join(params.split())
        signatures.append(f"{class_name}({clean_params})")

    # Méthodes publiques normales
    method_pattern = r'public\s+(?:static\s+)?(?:[\w<>,\s\[\]]+)\s+(\w+)\s*\(([^)]*)\)'
    for method_name, params in re.findall(method_pattern, csharp_code):
        clean_params = ' '.join(params.split())
        signatures.append(f"{method_name}({clean_params})")

    return signatures