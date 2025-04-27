#!/bin/bash

# Drapeau pour arrêter en cas d'erreur
set -e

echo "[1/4] Génération des tests avec TestForge..."
python3 main.py "$1"

echo "[2/4] Build du projet C# avec dotnet..."
dotnet build

echo "[3/4] Exécution des tests unitaires..."
dotnet test --logger "html;LogFileName=test-results.html"

echo "[4/4] Pipeline terminé avec succès !"