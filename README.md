# DevOps TP2 - Réalisation d’une pipeline de CI/CD

## But du TP
Ce TP est une étude de  la solution CI/CD (Intégration Continue et Déploiement Continu) avec Flask, GitHub Actions et Azure Web Apps. Il inclut un pipeline d'automatisation pour tester, construire et déployer une application web Python basique.

## Contenu

1. [Fonctionnalités](#fonctionnalités)
2. [Mise en place](#mise-en-place)
3. [Configuration](#configuration)
4. [Déploiement](#déploiement)


## Fonctionnalités
- **Flask Web App** : Un serveur web simple fonctionnant sous Python.
- **Tests Automatisés** : Utilisation de `pytest` pour exécuter des tests automatisés lors de chaque `push`.
- **GitHub Actions** : Workflow configuré pour l'intégration et le déploiement continus.
- **Azure Web Apps** : Hébergement du service web Flask sur Azure.

## Mise en place

1. Ajouter ```requirements.txt```, ```app.py``` et ```test_app.py``` :
     1. ```requirements.txt``` est la liste des applications importantes pour la manipulation.
     2. ```app.py``` est le site web Flask que nous allons ajouter sur WebApp.
     3. ```test_app.py``` est un script de vérification de bonne conformitée du script ```app.py```, il s'appliquera dans le ```WORKFLOW```.
2. Lier votre machine à votre GitHub.
     1. Aller dans votre dossier, ```git init``` pour initialiser le dossier à ```commit```.
     3. Ajouter les éléments du dossier dans le prochain ```commit``` avec ```git add .```. (
     4. Vérifier les dossiers séléctionnés avec ```git status``` en rouge les suppression à syncroniser/en vert les ajouts et modifications
     5. Une fois les modifications ajoutées créer votre commit, ```git commit -m "version 1"```
     6. Ensuite, créer le lien distant : ```git remote add origin https://github.com/votre-url.git```
     7. Maintenant, envoyer votre commit vers votre lien distant, ```git push origin main```. ( Par la suite vous devrez [Continuer les commits](#continuer-les-commits) pour faire évoluer votre sites) 
     8.Retrouver le contenu de votre dossier sur votre GitHub.
3. 

## Continuer les commits


## Configuration
La configuration du CI/CD est gérée via `.github/workflows/main.yml`, qui définit les étapes du pipeline :

1. Installation des dépendances.
2. Exécution des tests unitaires.
3. Construction d'un artefact zippé.
4. Déploiement sur Azure Web App.

## Déploiement
Les modifications poussées sur la branche `main` déclenchent le workflow CI/CD qui déploie automatiquement l'application sur Azure.




