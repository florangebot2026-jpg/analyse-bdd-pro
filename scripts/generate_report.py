#!/usr/bin/env python3
"""
Script pour générer des rapports sur les performances de la base de données
"""

import argparse
import sys
from typing import Dict, List, Any
import json

def generate_performance_report(db_type: str, connection_string: str) -> Dict[str, Any]:
    """
    Génère un rapport de performance

    Args:
        db_type: Type de base de données
        connection_string: Chaîne de connexion

    Returns:
        Dictionnaire avec les informations de performance
    """
    try:
        if db_type == 'postgresql':
            import psycopg2
            conn = psycopg2.connect(connection_string)
            cursor = conn.cursor()

            # Récupérer les statistiques
            cursor.execute("""
                SELECT schemaname, tablename,
                       n_live_tup as row_count,
                       n_dead_tup as dead_rows,
                       last_autovacuum, last_analyze
                FROM pg_stat_user_tables
                ORDER BY n_live_tup DESC
            """)

            tables = []
            for row in cursor.fetchall():
                tables.append({
                    'schema': row[0],
                    'table': row[1],
                    'row_count': row[2],
                    'dead_rows': row[3],
                    'last_autovacuum': row[4],
                    'last_analyze': row[5]
                })

            cursor.close()
            conn.close()

        elif db_type == 'mysql':
            import mysql.connector
            conn = mysql.connector.connect(connection_string)
            cursor = conn.cursor()

            # Récupérer les statistiques
            cursor.execute("""
                SELECT table_schema, table_name,
                       table_rows, data_length, index_length
                FROM information_schema.tables
                WHERE table_schema = DATABASE()
                ORDER BY table_rows DESC
            """)

            tables = []
            for row in cursor.fetchall():
                tables.append({
                    'schema': row[0],
                    'table': row[1],
                    'row_count': row[2],
                    'data_length': row[3],
                    'index_length': row[4]
                })

            cursor.close()
            conn.close()

        else:
            raise ValueError(f"Type de base de données non supporté: {db_type}")

        return {
            'db_type': db_type,
            'tables': tables,
            'total_tables': len(tables),
            'total_rows': sum(t['row_count'] for t in tables),
            'total_size': sum(t['data_length'] + t['index_length'] for t in tables)
        }

    except Exception as e:
        print(f"❌ Erreur lors de la génération du rapport: {e}")
        sys.exit(1)

def generate_json_report(performance_info: Dict[str, Any]) -> str:
    """
    Génère un rapport JSON

    Args:
        performance_info: Informations de performance

    Returns:
        Chaîne JSON
    """
    return json.dumps(performance_info, indent=2, ensure_ascii=False)

def generate_text_report(performance_info: Dict[str, Any]) -> str:
    """
    Génère un rapport texte

    Args:
        performance_info: Informations de performance

    Returns:
        Rapport texte
    """
    report = []
    report.append("=" * 80)
    report.append("RAPPORT DE PERFORMANCE")
    report.append("=" * 80)
    report.append(f"Type de base de données: {performance_info['db_type'].upper()}")
    report.append(f"Nombre de tables: {performance_info['total_tables']}")
    report.append(f"Nombre total de lignes: {performance_info['total_rows']:,}")
    report.append(f"Taille totale: {performance_info['total_size']:,} octets")
    report.append("")
    report.append("-" * 80)

    for table in performance_info['tables']:
        report.append(f"\n📋 TABLE: {table['schema']}.{table['table']}")
        report.append("-" * 80)
        report.append(f"Nombre de lignes: {table['row_count']:,}")
        report.append(f"Taille des données: {table['data_length']:,} octets")
        report.append(f"Taille des index: {table['index_length']:,} octets")

    report.append("")
    report.append("=" * 80)

    return "\n".join(report)

def main():
    parser = argparse.ArgumentParser(description="Générer un rapport de performance")
    parser.add_argument('--db-type', type=str, required=True,
                       choices=['postgresql', 'mysql', 'mssql'],
                       help='Type de base de données')
    parser.add_argument('--connection', type=str, required=True,
                       help='Chaîne de connexion')
    parser.add_argument('--output', type=str, default='rapport_performance.json',
                       help='Fichier de sortie (par défaut: rapport_performance.json)')

    args = parser.parse_args()

    print(f"📊 Génération du rapport de performance...")

    # Générer le rapport
    performance_info = generate_performance_report(args.db_type, args.connection)

    # Générer les formats
    json_report = generate_json_report(performance_info)
    text_report = generate_text_report(performance_info)

    # Sauvegarder les rapports
    with open(args.output, 'w') as f:
        f.write(json_report)

    with open(args.output.replace('.json', '.txt'), 'w') as f:
        f.write(text_report)

    print(f"✅ Rapport JSON sauvegardé dans: {args.output}")
    print(f"✅ Rapport texte sauvegardé dans: {args.output.replace('.json', '.txt')}")

if __name__ == '__main__':
    main()