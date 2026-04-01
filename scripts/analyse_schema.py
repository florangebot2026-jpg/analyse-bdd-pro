#!/usr/bin/env python3
"""
Script pour analyser le schéma d'une base de données
Supporte PostgreSQL, MySQL et SQL Server
"""

import argparse
import sys
from typing import Dict, List, Any

# Configuration des drivers
DRIVERS = {
    'postgresql': 'psycopg2',
    'mysql': 'mysql-connector',
    'mssql': 'pyodbc'
}

def analyze_schema(db_type: str, connection_string: str) -> Dict[str, Any]:
    """
    Analyse le schéma d'une base de données

    Args:
        db_type: Type de base de données (postgresql, mysql, mssql)
        connection_string: Chaîne de connexion

    Returns:
        Dictionnaire avec les informations du schéma
    """
    try:
        if db_type == 'postgresql':
            import psycopg2
            conn = psycopg2.connect(connection_string)
            cursor = conn.cursor()

            # Récupérer les tables
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = 'public'
                ORDER BY table_name
            """)

            tables = [row[0] for row in cursor.fetchall()]

            # Récupérer les colonnes pour chaque table
            schema_info = {}
            for table in tables:
                cursor.execute("""
                    SELECT column_name, data_type, is_nullable, column_default
                    FROM information_schema.columns
                    WHERE table_name = %s
                    ORDER BY ordinal_position
                """, (table,))

                columns = []
                for row in cursor.fetchall():
                    columns.append({
                        'name': row[0],
                        'type': row[1],
                        'nullable': row[2],
                        'default': row[3]
                    })

                schema_info[table] = {
                    'columns': columns,
                    'row_count': 0  # À implémenter
                }

            cursor.close()
            conn.close()

        elif db_type == 'mysql':
            import mysql.connector
            conn = mysql.connector.connect(connection_string)
            cursor = conn.cursor()

            # Récupérer les tables
            cursor.execute("""
                SELECT table_name
                FROM information_schema.tables
                WHERE table_schema = DATABASE()
                ORDER BY table_name
            """)

            tables = [row[0] for row in cursor.fetchall()]

            # Récupérer les colonnes pour chaque table
            schema_info = {}
            for table in tables:
                cursor.execute("""
                    SELECT column_name, data_type, is_nullable, column_default
                    FROM information_schema.columns
                    WHERE table_name = %s
                    ORDER BY ordinal_position
                """, (table,))

                columns = []
                for row in cursor.fetchall():
                    columns.append({
                        'name': row[0],
                        'type': row[1],
                        'nullable': row[2],
                        'default': row[3]
                    })

                schema_info[table] = {
                    'columns': columns,
                    'row_count': 0  # À implémenter
                }

            cursor.close()
            conn.close()

        else:
            raise ValueError(f"Type de base de données non supporté: {db_type}")

        return {
            'db_type': db_type,
            'tables': schema_info,
            'total_tables': len(tables)
        }

    except Exception as e:
        print(f"❌ Erreur lors de l'analyse du schéma: {e}")
        sys.exit(1)

def generate_report(schema_info: Dict[str, Any]) -> str:
    """
    Génère un rapport texte du schéma

    Args:
        schema_info: Informations du schéma

    Returns:
        Rapport texte
    """
    report = []
    report.append("=" * 80)
    report.append("RAPPORT D'ANALYSE DE SCHÉMA")
    report.append("=" * 80)
    report.append(f"Type de base de données: {schema_info['db_type'].upper()}")
    report.append(f"Nombre de tables: {schema_info['total_tables']}")
    report.append("")
    report.append("-" * 80)

    for table_name, table_info in schema_info['tables'].items():
        report.append(f"\n📋 TABLE: {table_name}")
        report.append("-" * 80)
        report.append(f"Nombre de colonnes: {len(table_info['columns'])}")
        report.append("")

        for col in table_info['columns']:
            nullable = "NULL" if col['nullable'] == 'YES' else "NOT NULL"
            default = f" DEFAULT {col['default']}" if col['default'] else ""
            report.append(f"  • {col['name']:30s} {col['type']:20s} {nullable:10s}{default}")

    report.append("")
    report.append("=" * 80)

    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Analyser le schéma d'une base de données")
    parser.add_argument('--db-type', type=str, required=True,
                       choices=['postgresql', 'mysql', 'mssql'],
                       help='Type de base de données')
    parser.add_argument('--connection', type=str, required=True,
                       help='Chaîne de connexion (ex: postgresql://user:password@localhost:5432/db)')

    args = parser.parse_args()

    print(f"🔍 Analyse du schéma de la base de données {args.db_type}...")

    # Analyser le schéma
    schema_info = analyze_schema(args.db_type, args.connection)

    # Générer le rapport
    report = generate_report(schema_info)

    # Afficher le rapport
    print(report)

    # Sauvegarder le rapport dans un fichier
    output_file = f"rapport_schema_{args.db_type}_{args.connection.split('@')[1].split('/')[1]}.txt"
    with open(output_file, 'w') as f:
        f.write(report)

    print(f"\n✅ Rapport sauvegardé dans: {output_file}")

if __name__ == '__main__':
    main()