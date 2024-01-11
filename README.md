# Open-Source-it
<img src="https://img.shields.io/badge/version%20%3A%201.0.0-blue" height="20">
<img src="https://img.shields.io/badge/Built%20with-Python-blue" height="20">
<img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray" height="20">
<img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white" height="20">
<img src="https://img.shields.io/badge/CI-Passing-brightgreen" height="20">
<img src="https://img.shields.io/github/last-commit/DjouaherRachid/Open-Source-it?style=flat-square&color=purple&labelColor=white" height="20">

Dans ce projet, nous avons "open-sourcé" le projet de développement Web API du 1er semestre de 2I à l'ESGI, intitulé "RESTpasTrop".

Il s'agit d'un API web pour la solution logicielle d'une entreprise.
L'entreprise en question gère des locations d'appartement à court terme, généralement quelque jours.
Plusieurs clients terminaux peuvent se connecter à l'API: Un backoffice pour les administrateurs, une application mobile pour les propriétaires, un site web publique pour les clients.

### Comment installer notre programme ou le mettre en production

Pour installer et utiliser le programme, il suffit simplement de suivre cette étape très simple

1. **Cloner le Dépôt :**
   - Ouvrez un terminal et exécutez la commande suivante pour cloner le dépôt :

     ```bash
     git clone https://github.com/DjouaherRachid/Open-Source-it.git
     ```

## Tester les APIs et Accéder à l'Interface Django Administration

Avant de commencer à tester les fonctionnalités de l'API et d'accéder à l'interface Django Administration, assurez-vous d'installer les dépendances nécessaires en suivant ces étapes :

1. **Configuration de l'environnement virtuel :**

   Il est recommandé d'utiliser un environnement virtuel pour isoler les dépendances de ce projet. Suivez les étapes ci-dessous pour créer et activer un environnement virtuel Python (venv) :

   - Ouvrez un terminal dans le répertoire du projet.
   - Tapez les commandes suivantes pour créer un nouveau environnement virtuel et l'activer :

     ```bash
     python -m venv venv
     ```

     ```bash
     venv\bin\activate
     ```

2. **Installer les Dépendances :**
   - Ouvrez un terminal dans le répertoire du projet.
   - Tapez la commande suivante pour installer les dépendances requises :

     ```bash
     pip install -r requirements.txt
     ```

   Cela garantira que toutes les bibliothèques nécessaires sont installées.

3. **Lancer le Serveur Django :**
   - Toujours dans le terminal du projet, tapez la commande suivante pour démarrer le serveur Django :

     ```bash
     python manage.py runserver
     ```

   Cela lancera le serveur local à l'adresse http://127.0.0.1:8000/.

4. **Importer la Collection Postman :**
   - Ouvrez Postman.
   - Cliquez sur "Import" dans le coin supérieur gauche.
   - Sélectionnez "Importer le fichier" et choisissez le fichier YAML fourni.
   - La collection et les requêtes associées seront importées dans votre environnement Postman.

5. **Créer un Super Utilisateur :**
   - Dans le même terminal que précédemment, tapez la commande suivante pour créer un super utilisateur :

     ```bash
     python manage.py createsuperuser
     ```

   Suivez les instructions pour fournir les informations requises.

6. **Accéder à l'Interface Django Administration :**
   - Ouvrez votre navigateur web et accédez à l'URL http://127.0.0.1:8000/admin/.
   - Connectez-vous en utilisant les données du super utilisateur que vous venez de créer. Par exemple :
     - Nom d'utilisateur : admin
     - Mot de passe : admin

   Vous aurez ainsi accès à l'interface Django Administration pour gérer les données de l'application.

### Comment contribuer au projet

Maintenant que vous pouvez correctement utiliser et tester notre API, vous pouvez commencer àcontribuer à notre projet ! Suivez ces étapes simples pour participer au développement et améliorer notre application :

1. **Fork du projet :**
   - Sur la page principale du [dépôt GitHub](https://github.com/DjouaherRachid/Open-Source-it), cliquez sur le bouton "Fork" en haut à droite de la page. Cela créera une copie du projet sur votre propre compte GitHub.

2. **Clonez votre fork :**
   - Ouvrez votre fork sur GitHub.
   - Cliquez sur le bouton vert "Code" et copiez l'URL du dépôt.
   - Ouvrez une invite de commande ou un terminal et exécutez la commande suivante pour cloner votre fork localement :

     ```bash
     git clone https://github.com/VOTRE_UTILISATEUR/Open-Source-it.git
     ```

3. **Créez une branche de fonctionnalité :**
   - Avant de commencer à travailler, créez une nouvelle branche pour votre fonctionnalité ou correction :

     ```bash
     git checkout -b nom-de-votre-branche
     ```

4. **Effectuez les modifications :**
   - Faites les modifications nécessaires dans le code. N'oubliez pas de suivre les meilleures pratiques de codage et les conventions du projet.

5. **Testez vos modifications :**
   - Assurez-vous que vos modifications ne provoquent pas d'erreurs. Vous pouvez exécuter les tests existants en utilisant la commande :

     ```bash
     python manage.py test
     ```

6. **Commit et poussez les modifications :**
   - Une fois satisfait des modifications, effectuez un commit et poussez les changements vers votre fork :

     ```bash
     git add .
     git commit -m "Description de vos modifications"
     git push origin nom-de-votre-branche
     ```

7. **Soumettez une demande de tirage (Pull Request) :**
   - Rendez-vous sur la page de votre fork sur GitHub.
   - Cliquez sur le bouton "Compare & pull request" à côté de votre nouvelle branche.
   - Remplissez le formulaire de demande de tirage en fournissant des informations claires sur vos modifications.

8. **Attendez la revue :**
   - Votre demande de tirage sera examinée par les mainteneurs du projet. Soyez prêt à répondre aux commentaires et apporter des modifications si nécessaire.

En suivant ces étapes, vous contribuerez efficacement à notre projet. Merci pour votre engagement et vos efforts pour améliorer notre application !



