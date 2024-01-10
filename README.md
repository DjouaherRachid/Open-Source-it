# Open-Source-it

Dans ce projet, nous avons "open-sourcé" le projet de développement Web API du 1er semestre de 2I à l'ESGI, intitulé "RESTpasTrop".

Il s'agit d'un API web pour la solution logicielle d'une entreprise.
L'entreprise en question gère des locations d'appartement à court terme, généralement quelque jours.
Plusieurs clients terminaux peuvent se connecter à l'API: Un backoffice pour les administrateurs, une application mobile pour les propriétaires, un site web publique pour les clients.
## Les badges github :

![Static Badge](https://img.shields.io/badge/version%20%3A%201.0.0-blue)
![Build with Python](https://img.shields.io/badge/Built%20with-Python-blue)
[![Generic badge](https://img.shields.io/badge/test-test-<BLUE>.svg)](https://shields.io/)
![Last Commit](https://img.shields.io/github/last-commit/Mustapha/Open-source-it)

## Tester les APIs et Accéder à l'Interface Django Administration

Avant de commencer à tester les fonctionnalités de l'API et d'accéder à l'interface Django Administration, assurez-vous d'installer les dépendances nécessaires en suivant ces étapes :

1. **Installer les Dépendances :**
   - Ouvrez un terminal dans le répertoire du projet.
   - Tapez la commande suivante pour installer les dépendances requises :

     ```bash
     pip install -r requirements.txt
     ```

   Cela garantira que toutes les bibliothèques nécessaires sont installées.

2. **Lancer le Serveur Django :**
   - Toujours dans le terminal du projet, tapez la commande suivante pour démarrer le serveur Django :

     ```bash
     python manage.py runserver
     ```

   Cela lancera le serveur local à l'adresse http://127.0.0.1:8000/.

3. **Importer la Collection Postman :**
   - Ouvrez Postman.
   - Cliquez sur "Import" dans le coin supérieur gauche.
   - Sélectionnez "Importer le fichier" et choisissez le fichier YAML fourni.
   - La collection et les requêtes associées seront importées dans votre environnement Postman.

4. **Créer un Super Utilisateur :**
   - Dans le même terminal que précédemment, tapez la commande suivante pour créer un super utilisateur :

     ```bash
     python manage.py createsuperuser
     ```

   Suivez les instructions pour fournir les informations requises.

5. **Accéder à l'Interface Django Administration :**
   - Ouvrez votre navigateur web et accédez à l'URL http://127.0.0.1:8000/admin/.
   - Connectez-vous en utilisant les données du super utilisateur que vous venez de créer. Par exemple :
     - Nom d'utilisateur : admin
     - Mot de passe : admin

   Vous aurez ainsi accès à l'interface Django Administration pour gérer les données de l'application.


