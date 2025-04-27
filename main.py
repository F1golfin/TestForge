from agent_manager import AgentManager

def main():
    input_path = "samples/GameCharacter.cs" # Fichier d'entrée
    manager = AgentManager(input_path)
    manager.start()

if __name__ == "__main__":
    main()