# 🗄️ Analyse de Bases de Données Professionnelles

Outils et scripts pour analyser et gérer des bases de données professionnelles (SQL, PostgreSQL, MySQL).

## 🚀 Fonctionnalités

- ✅ Analyse de schémas de bases de données
- ✅ Génération de rapports SQL
- ✅ Optimisation de requêtes
- ✅ Documentation automatique
- ✅ Scripts de migration
- ✅ Tests de performance

## 📊 Bases de données supportées

- **PostgreSQL** - BDD relationnelle open-source
- **MySQL** - BDD relationnelle open-source
- **SQL Server** - BDD relationnelle Microsoft
- **Oracle** - BDD relationnelle propriétaire
- **SQLite** - BDD légère

## 🚀 Installation

### Prérequis

- Python 3.9+
- pip3
- PostgreSQL 17+ (pour PostgreSQL)
- MySQL 8.0+ (pour MySQL)

### Installer les dépendances

```bash
cd ~/bdd-pro
pip3 install -r requirements.txt
```

## 📁 Structure du Projet

```
~/bdd-pro/
├── README.md                 # Ce fichier
├── requirements.txt          # Dépendances Python
├── .gitignore               # Fichier .gitignore
├── scripts/                 # Scripts Python
│   ├── analyse_schema.py    # Analyse de schéma
│   ├── generate_report.py   # Génération de rapports
│   ├── optimize_query.py    # Optimisation de requêtes
│   └── migrate_db.py        # Scripts de migration
├── templates/               # Templates SQL
│   ├── report_template.sql  # Template de rapport
│   └── migration_template.sql # Template de migration
├── tests/                   # Tests
│   ├── test_schema.py       # Tests de schéma
│   └── test_query.py        # Tests de requêtes
└── docs/                    # Documentation
    ├── INSTALLATION.md      # Guide d'installation
    └── USAGE.md             # Guide d'utilisation
```

## 🛠️ Scripts Principaux

### `scripts/analyse_schema.py`
Analyse le schéma d'une base de données et génère un rapport détaillé.

### `scripts/generate_report.py`
Génère des rapports automatiques sur les performances de la BDD.

### `scripts/optimize_query.py`
Optimise les requêtes SQL en identifiant les problèmes de performance.

### `scripts/migrate_db.py`
Scripts de migration pour migrer entre différentes versions de BDD.

## ⚙️ Configuration

### PostgreSQL

```bash
# Installer PostgreSQL
brew install postgresql@17

# Démarrer PostgreSQL
brew services start postgresql@17

# Créer une base de données
createdb ma_base_de_donnees
```

### MySQL

```bash
# Installer MySQL
brew install mysql

# Démarrer MySQL
brew services start mysql

# Créer une base de données
mysql -u root -p -e "CREATE DATABASE ma_base_de_donnees;"
```

## 📝 Exemples d'utilisation

### Analyse de schéma

```bash
python3 scripts/analyse_schema.py --db postgresql://user:password@localhost:5432/ma_base
```

### Génération de rapport

```bash
python3 scripts/generate_report.py --db postgresql://user:password@localhost:5432/ma_base --output rapport.pdf
```

### Optimisation de requête

```bash
python3 scripts/optimize_query.py --db postgresql://user:password@localhost:5432/ma_base --query "SELECT * FROM utilisateurs"
```

## 🎯 Roadmap

- [ ] Ajouter plus de BDD (MongoDB, Redis, etc.)
- [ ] Intégrer des tests automatiques
- [ ] Créer des interfaces graphiques
- [ ] Ajouter des prédictions avec machine learning
- [ ] Support pour NoSQL

## 📞 Support

Si tu as des problèmes, dis-moi ! 🚀

## 📄 Licence

MIT License

---

**Créé avec ❤️ par Florent**
**Dernière mise à jour : 2026-04-01**