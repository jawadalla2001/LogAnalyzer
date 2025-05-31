# Log Analyzer - DevOps Project

## 📋 Description
Outil CLI d'analyse automatique de fichiers journaux développé dans le cadre d'un exercice DevOps.

## 🚀 Fonctionnalités
- Analyse automatique des fichiers log.txt
- Comptage des niveaux ERROR, WARNING, INFO
- Génération de rapport.txt avec statistiques
- Condition d'échec si plus de 5 erreurs détectées
- Générateur de logs d'exemple pour tests

## 🛠️ Installation
```bash
git clone https://github.com/[votre-username]/log-analyzer.git
cd log-analyzer
pip install -r requirements.txt
```

## 📖 Utilisation

### Analyse d'un fichier de log
```bash
python log_analyzer.py log.txt
```

### Génération d'un fichier de test
```bash
python log_analyzer.py sample_log.txt --generate-sample
```

### Spécifier un fichier de rapport personnalisé
```bash
python log_analyzer.py log.txt -o mon_rapport.txt
```

## 🔧 Options
- `log_file`: Chemin vers le fichier de log à analyser
- `-o, --output`: Fichier de sortie pour le rapport (défaut: rapport.txt)
- `--generate-sample`: Génère un fichier de log d'exemple

## 📊 Format de sortie
Le script génère un rapport détaillé avec:
- Statistiques de comptage par niveau
- Évaluation des risques
- Code de sortie (0: succès, 1: échec si >5 erreurs)

## 🏗️ Architecture DevOps
- **Versionnement**: Git/GitHub avec branches main/dev
- **CI/CD**: GitHub Actions pour tests automatisés
- **Automatisation**: Jenkins avec jobs freestyle et pipeline
- **Planification**: Trello pour gestion Agile
- **Sécurité**: Rôles et permissions Jenkins

## 🧪 Tests
```bash
# Génération d'un log de test
python log_analyzer.py test_log.txt --generate-sample

# Analyse du log de test
python log_analyzer.py test_log.txt
```

## 👥 Collaboration
Pour contribuer au projet:
1. Fork le repository
2. Créer une branche feature
3. Commit les modifications
4. Créer une Pull Request

## 📝 Licence
MIT License

## 👨‍💻 Auteur
[Votre Nom] - Exercice DevOps LogAnalyzer
