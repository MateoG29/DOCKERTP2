# DevOps TP2 - Continuous Integration and Deployment

## Overview
Ce projet est une démonstration simple du processus de CI/CD (Intégration Continue et Déploiement Continu) utilisant Flask, GitHub Actions et Azure Web Apps. Il inclut un pipeline d'automatisation pour tester, construire et déployer une application web Python basique.

## Fonctionnalités
- **Flask Web App** : Un serveur web simple affichant un message de bienvenue.
- **Tests Automatisés** : Utilisation de `pytest` pour exécuter des tests automatisés lors de chaque `push`.
- **GitHub Actions** : Workflow configuré pour l'intégration et le déploiement continus.
- **Azure Web Apps** : Hébergement du service web Flask sur Azure.

## Configuration
La configuration du CI/CD est gérée via `.github/workflows/main.yml`, qui définit les étapes du pipeline :

1. Installation des dépendances.
2. Exécution des tests unitaires.
3. Construction d'un artefact zippé.
4. Déploiement sur Azure Web App.

## Déploiement
Les modifications poussées sur la branche `main` déclenchent le workflow CI/CD qui déploie automatiquement l'application sur Azure.

## Contributions
Les contributions sont les bienvenues. Pour proposer des modifications, veuillez créer une `pull request`.

## License
Ce projet est distribué sous la License MIT. Voir le fichier `LICENSE` pour plus d'informations.
