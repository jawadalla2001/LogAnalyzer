# Log Analyzer Project

**Auteur:** Alla Jawad /Pseudo GitHub

## Description

Ce projet est un outil CLI (Command Line Interface) développé en Python pour analyser des fichiers journaux (logs) générés par des serveurs. L'outil compte les occurrences de différents niveaux de logs (ERROR, WARNING, INFO) et génère un rapport statistique.

Ce projet a été développé dans le cadre d'un exercice DevOps visant à mettre en pratique les concepts de développement, de versionnement avec Git et GitHub, d'intégration continue avec GitHub Actions, et de déploiement et gestion avec Jenkins.

## Fonctionnalités

*   Lecture d'un fichier `log.txt` (ou un fichier spécifié).
*   Comptage des lignes totales, des erreurs (ERROR), des avertissements (WARNING), et des informations (INFO).
*   Génération d'un fichier `rapport.txt` (ou un fichier spécifié) avec les statistiques et pourcentages.
*   Option pour créer un fichier `log.txt` simulé avec des données aléatoires.
*   Sortie avec un code d'erreur si le nombre d'erreurs dépasse un seuil configurable (utile pour l'intégration CI/CD).

## Instructions d'utilisation

### Prérequis

*   Python 3.x

### Installation

Aucune installation spécifique de package n'est requise pour le script de base, car il utilise uniquement les bibliothèques Python standard.

Clonez le dépôt (ou téléchargez les fichiers) :
```bash
git clone [URL_DU_DEPOT_GIT]
cd [NOM_DU_DOSSIER_PROJET]
```

### Exécution du script

Pour exécuter le script, utilisez la commande suivante dans votre terminal :

```bash
python log_analyzer.py [OPTIONS]
```

**Options disponibles :**

*   `--log_file CHEMIN_FICHIER_LOG`: Spécifie le chemin vers le fichier log à analyser. Par défaut : `log.txt`.
*   `--output_file CHEMIN_FICHIER_RAPPORT`: Spécifie le chemin vers le fichier de rapport de sortie. Par défaut : `rapport.txt`.
*   `--error_threshold NOMBRE`: Définit le seuil d'erreurs. Si le nombre d'erreurs détectées dépasse ce seuil, le script se terminera avec un code d'erreur 1 (échec). Par défaut : `5`.
*   `--create_dummy_log`: Si cette option est utilisée, un fichier `log.txt` (ou celui spécifié par `--log_file`) sera créé avec des entrées de log simulées avant l'analyse.

**Exemples :**

1.  **Analyser le fichier `log.txt` par défaut et générer `rapport.txt` :**
    ```bash
    python log_analyzer.py
    ```

2.  **Créer un fichier `log.txt` simulé puis l'analyser :**
    ```bash
    python log_analyzer.py --create_dummy_log
    ```

3.  **Analyser un fichier log spécifique `server.log` et définir un seuil d'erreur à 10 :**
    ```bash
    python log_analyzer.py --log_file server.log --error_threshold 10
    ```

## Structure du projet

*   `log_analyzer.py`: Le script Python principal contenant la logique de l'analyseur.
*   `log.txt`: Fichier log d'exemple (peut être généré par le script).
*   `rapport.txt`: Fichier de rapport généré par le script.
*   `README.md`: Ce fichier.
*   `.github/workflows/ci.yml`: Fichier de configuration pour GitHub Actions (CI).
*   `Jenkinsfile`: Fichier de configuration pour le pipeline Jenkins.

## Étapes du projet DevOps

1.  **Développement initial & GitHub:**
    *   Création du projet CLI (Python).
    *   Initialisation du dépôt Git local et distant (GitHub).
    *   Création du `README.md`.
    *   Utilisation de branches (`dev`) et Pull Requests.
2.  **Planification Agile - Trello:** Organisation des tâches.
3.  **CI/CD - GitHub Actions:** Mise en place d'un workflow pour vérifier le script.
4.  **Jenkins - build automatique:** Création d'un job freestyle et d'un pipeline scripté.
5.  **Sécurité et gestion des rôles Jenkins:** Configuration des utilisateurs et des rôles. 