import subprocess

def appeler_ollama(prompt: str, modele: str = "codellama") -> str:
    """Envoie un prompt au modèle Ollama et retourne la réponse texte."""
    try:
        result = subprocess.run(
            ["ollama", "run", modele],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode("utf-8").strip()
    except subprocess.CalledProcessError as e:
        return f"❌ Erreur Ollama : {e.stderr.decode('utf-8')}"