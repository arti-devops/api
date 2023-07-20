# Utilisez une image de base adaptée à votre application Python avec FastAPI
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de l'API dans le conteneur
COPY . .

# Installer les dépendances de l'API
RUN pip install --no-cache-dir -r requirements.txt

# Copier le fichier .env dans le conteneur
COPY .env .

# Exposer le port sur lequel votre API écoute (port 81 dans cet exemple)
EXPOSE 81

# Lancer l'API à l'aide de votre script run.sh
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "81"]

