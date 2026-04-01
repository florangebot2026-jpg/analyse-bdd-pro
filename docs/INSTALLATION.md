# Guide d'Installation

Ce guide vous explique comment installer et configurer le projet d'analyse de bases de données professionnelles.

## Prérequis

### Système

- **OS** : macOS, Linux, Windows
- **Python** : 3.9 ou supérieur
- **pip** : 20.3 ou supérieur

### Bases de données

- **PostgreSQL** : 17 ou supérieur
- **MySQL** : 8.0 ou supérieur
- **SQL Server** : 2019 ou supérieur

## Installation sous macOS

### 1. Installer PostgreSQL

```bash
# Installer PostgreSQL via Homebrew
brew install postgresql@17

# Démarrer PostgreSQL
brew services start postgresql@17

# Créer un utilisateur
createuser -s postgres

# Créer une base de données
createdb ma_base_de_donnees
```

### 2. Installer MySQL

```bash
# Installer MySQL via Homebrew
brew install mysql

# Démarrer MySQL
brew services start mysql

# Sécuriser l'installation
mysql_secure_installation
```

### 3. Installer Python et les dépendances

```bash
# Installer Python (si nécessaire)
brew install python@3.11

# Installer les dépendances du projet
cd ~/bdd-pro
pip3 install -r requirements.txt
```

## Installation sous Linux

### 1. Installer PostgreSQL

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install postgresql postgresql-contrib

# Démarrer PostgreSQL
sudo systemctl start postgresql
sudo systemctl enable postgresql

# Créer un utilisateur
sudo -u postgres createuser -s postgres

# Créer une base de données
sudo -u postgres createdb ma_base_de_donnees
```

### 2. Installer MySQL

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install mysql-server

# Démarrer MySQL
sudo systemctl start mysql
sudo systemctl enable mysql

# Sécuriser l'installation
sudo mysql_secure_installation
```

### 3. Installer Python et les dépendances

```bash
# Installer Python (si nécessaire)
sudo apt install python3.11 python3-pip

# Installer les dépendances du projet
cd ~/bdd-pro
pip3 install -r requirements.txt
```

## Installation sous Windows

### 1. Installer PostgreSQL

1. Télécharger PostgreSQL depuis https://www.postgresql.org/download/windows/
2. Suivre l'assistant d'installation
3. Créer un mot de passe pour l'utilisateur postgres
4. Configurer le port (par défaut: 5432)

### 2. Installer MySQL

1. Télécharger MySQL depuis https://dev.mysql.com/downloads/mysql/
2. Suivre l'assistant d'installation
3. Créer un mot de passe pour l'utilisateur root
4. Configurer le port (par défaut: 3306)

### 3. Installer Python et les dépendances

1. Télécharger Python depuis https://www.python.org/downloads/
2. Cocher "Add Python to PATH" lors de l'installation
3. Ouvrir une invite de commande et installer les dépendances

```cmd
cd C:\Users\VotreNom\bdd-pro
pip install -r requirements.txt
```

## Configuration

### Variables d'environnement

Créer un fichier `.env` dans le dossier du projet :

```bash
# PostgreSQL
POSTGRES_DB=ma_base_de_donnees
POSTGRES_USER=postgres
POSTGRES_PASSWORD=votre_mot_de_passe
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

# MySQL
MYSQL_DB=ma_base_de_donnees
MYSQL_USER=root
MYSQL_PASSWORD=votre_mot_de_passe
MYSQL_HOST=localhost
MYSQL_PORT=3306
```

### Chaînes de connexion

**PostgreSQL :**
```
postgresql://postgres:votre_mot_de_passe@localhost:5432/ma_base_de_donnees
```

**MySQL :**
```
mysql://root:votre_mot_de_passe@localhost:3306/ma_base_de_donnees
```

## Vérification de l'installation

Tester la connexion à votre base de données :

```bash
# PostgreSQL
psql -U postgres -d ma_base_de_donnees

# MySQL
mysql -u root -p ma_base_de_donnees
```

## Problèmes courants

### PostgreSQL ne démarre pas

```bash
# Vérifier l'état
brew services list

# Redémarrer
brew services restart postgresql@17
```

### MySQL ne démarre pas

```bash
# Vérifier l'état
brew services list

# Redémarrer
brew services restart mysql
```

### Erreur de connexion

Vérifier que :
1. Le service est démarré
2. Le mot de passe est correct
3. Le port est accessible
4. Le pare-feu ne bloque pas la connexion

## Support

Si vous rencontrez des problèmes, consultez la documentation ou contactez l'équipe de support.

---

**Dernière mise à jour : 2026-04-01**