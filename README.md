# Journal de Chantier 🏗️

Application web Django permettant le suivi quotidien des activités de chantier :
- Saisie et consultation des rapports quotidiens (météo, effectifs, travaux réalisés, observations, incidents).
- Ajout de photos de chantier horodatées avec galerie d'aperçu.
- Recherche et filtrage par mot-clé et conditions météorologiques.

## Prérequis

- Python 3.10+
- `pip`

## Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/seexumar/journal-chantier.git
   cd journal-chantier
   ```

2. **Créer et activer un environnement virtuel** :
   ```bash
   # Sous Windows
   python -m venv env
   .\env\Scripts\activate

   # Sous Linux / macOS
   python3 -m venv env
   source env/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Appliquer les migrations de base de données** :
   ```bash
   python manage.py migrate
   ```

5. **Lancer le serveur de développement** :
   ```bash
   python manage.py runserver
   ```

L'application sera accessible sur [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
