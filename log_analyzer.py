import sys
import os
import re
import argparse
from datetime import datetime
from collections import Counter
import random

class LogAnalyzer:
    def __init__(self, log_file="log.txt", output_file="rapport.txt"):
        self.log_file = log_file
        self.output_file = output_file
        self.stats = {'ERROR': 0, 'WARNING': 0, 'INFO': 0, 'total_lines': 0}
        
    def parse_log_file(self):
        """Parse le fichier log et compte les différents niveaux"""
        try:
            with open(self.log_file, 'r') as f:
                for line in f:
                    self.stats['total_lines'] += 1
                    if re.search(r'ERROR', line):
                        self.stats['ERROR'] += 1
                    elif re.search(r'WARNING', line):
                        self.stats['WARNING'] += 1
                    elif re.search(r'INFO', line): # Assuming INFO is another level to count
                        self.stats['INFO'] += 1
        except FileNotFoundError:
            print(f"Erreur: Le fichier log '{self.log_file}' n'a pas été trouvé.")
            sys.exit(1)
        
    def generate_report(self):
        """Génère le rapport dans rapport.txt avec statistiques"""
        with open(self.output_file, 'w') as f:
            f.write(f"Rapport d'analyse du fichier log: {self.log_file}\n")
            f.write(f"Date de génération: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("="*30 + "\n")
            f.write(f"Nombre total de lignes analysées: {self.stats['total_lines']}\n")
            f.write(f"Nombre d'erreurs (ERROR): {self.stats['ERROR']}\n")
            f.write(f"Nombre d'avertissements (WARNING): {self.stats['WARNING']}\n")
            f.write(f"Nombre d'informations (INFO): {self.stats['INFO']}\n")
            f.write("="*30 + "\n")
            
            if self.stats['total_lines'] > 0:
                error_percentage = (self.stats['ERROR'] / self.stats['total_lines']) * 100
                warning_percentage = (self.stats['WARNING'] / self.stats['total_lines']) * 100
                info_percentage = (self.stats['INFO'] / self.stats['total_lines']) * 100
                f.write(f"Pourcentage d'erreurs: {error_percentage:.2f}%\n")
                f.write(f"Pourcentage d'avertissements: {warning_percentage:.2f}%\n")
                f.write(f"Pourcentage d'informations: {info_percentage:.2f}%\n")
            else:
                f.write("Aucune ligne à analyser pour calculer les pourcentages.\n")
            
            print(f"Rapport généré avec succès dans '{self.output_file}'")

    def check_error_threshold(self, threshold=5):
        """Vérifie si le nombre d'erreurs dépasse le seuil"""
        if self.stats['ERROR'] > threshold:
            print(f"Le nombre d'erreurs ({self.stats['ERROR']}) dépasse le seuil de {threshold}.")
            sys.exit(1)  # Échec pour Jenkins
        else:
            print(f"Le nombre d'erreurs ({self.stats['ERROR']}) est dans la limite acceptable (seuil={threshold}).")

def create_sample_log_file(filename="log.txt", lines=100):
    """Crée un fichier log simulé."""
    log_levels = ["ERROR", "WARNING", "INFO"]
    with open(filename, 'w') as f:
        for i in range(lines):
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            level = random.choice(log_levels)
            # Simulate some more errors for testing threshold
            if i % 10 == 0 and level != "ERROR": # ensure some errors
                 level = "ERROR"
            message_type = random.choice(["connexion utilisateur", "mise à jour système", "requête BDD", "erreur de script"])
            user_id = random.randint(1000, 9999)
            f.write(f"{timestamp} [{level}] Message {i+1}: {message_type} par user_{user_id}. Détails supplémentaires.\n")
    print(f"Fichier log simulé '{filename}' créé avec {lines} lignes.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyseur de fichiers log.")
    parser.add_argument("--log_file", default="log.txt", help="Chemin vers le fichier log à analyser.")
    parser.add_argument("--output_file", default="rapport.txt", help="Chemin vers le fichier de rapport de sortie.")
    parser.add_argument("--error_threshold", type=int, default=5, help="Seuil d'erreurs pour la sortie avec échec (pour Jenkins).")
    parser.add_argument("--create_dummy_log", action="store_true", help="Crée un fichier log.txt de démonstration.")

    args = parser.parse_args()

    if args.create_dummy_log:
        create_sample_log_file(args.log_file, lines=random.randint(50,150)) # Create a log with random number of lines

    if not os.path.exists(args.log_file):
        print(f"Le fichier log '{args.log_file}' n'existe pas. Créez-le ou utilisez --create_dummy_log.")
        # Optionally create a default one if it doesn't exist and not asked to create dummy
        if not args.create_dummy_log: # Check if dummy log creation was already handled
            print(f"Création d'un fichier log par défaut: {args.log_file}")
            create_sample_log_file(args.log_file, lines=20) # Default small log
            print("Un fichier log par défaut a été créé.")
        else:
            sys.exit(1) # Exit if --create_dummy_log was specified but file still not found (should not happen)

    analyzer = LogAnalyzer(log_file=args.log_file, output_file=args.output_file)
    analyzer.parse_log_file()
    analyzer.generate_report()
    analyzer.check_error_threshold(args.error_threshold)
