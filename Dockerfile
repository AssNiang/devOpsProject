# Utilisez une image Python officielle en tant qu'image de base
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez les fichiers requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez tout le reste du code dans le conteneur
COPY . .

# Exécutez la commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
