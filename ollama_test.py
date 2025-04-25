import subprocess

def appeler_ollama(prompt: str, modele: str = "codellama") -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", modele],
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True
        )
        return result.stdout.decode("utf-8")
    except subprocess.CalledProcessError as e:
        return f"Erreur : {e.stderr.decode('utf-8')}"

if __name__ == "__main__":
    prompt = """Voici une méthode C# : public int Add(int a, int b) { return a + b;} Écris un test unitaire NUnit 3 pour cette méthode."""
    print(appeler_ollama(prompt))