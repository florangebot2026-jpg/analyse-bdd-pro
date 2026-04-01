-- RAPPORT DE PERFORMANCE
-- Génération automatique le {{ date }}

-- 1. STATISTIQUES GLOBALES
SELECT
    '{{ db_type }}' as database_type,
    COUNT(*) as total_tables,
    SUM(table_rows) as total_rows,
    SUM(data_length + index_length) as total_size_bytes
FROM information_schema.tables
WHERE table_schema = '{{ database_schema }}';

-- 2. TABLES PAR TAILLE
SELECT
    table_schema,
    table_name,
    table_rows,
    ROUND((data_length + index_length) / 1024 / 1024, 2) as size_mb
FROM information_schema.tables
WHERE table_schema = '{{ database_schema }}'
ORDER BY (data_length + index_length) DESC
LIMIT 20;

-- 3. TABLES AVEC PLUS DE LIGNES
SELECT
    table_schema,
    table_name,
    table_rows
FROM information_schema.tables
WHERE table_schema = '{{ database_schema }}'
ORDER BY table_rows DESC
LIMIT 20;

-- 4. INDEXES
SELECT
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE schemaname = '{{ database_schema }}'
ORDER BY tablename, indexname;

-- 5. VUES
SELECT
    table_schema,
    table_name,
    view_definition
FROM information_schema.views
WHERE table_schema = '{{ database_schema }}'
ORDER BY table_name;

-- 6. PROCEDURES STOCKÉES
SELECT
    routine_schema,
    routine_name,
    routine_type,
    routine_definition
FROM information_schema.routines
WHERE routine_schema = '{{ database_schema }}'
ORDER BY routine_name;

-- 7. TABLES AVEC PLUS DE COLONNES
SELECT
    table_schema,
    table_name,
    COUNT(*) as column_count
FROM information_schema.columns
WHERE table_schema = '{{ database_schema }}'
GROUP BY table_schema, table_name
ORDER BY column_count DESC
LIMIT 20;

-- 8. TABLES AVEC PLUS DE NULLS
SELECT
    table_schema,
    table_name,
    COUNT(*) as total_rows,
    SUM(CASE WHEN is_nullable = 'YES' THEN 1 ELSE 0 END) as nullable_rows,
    ROUND(100.0 * SUM(CASE WHEN is_nullable = 'YES' THEN 1 ELSE 0 END) / COUNT(*), 2) as nullable_percentage
FROM information_schema.columns
WHERE table_schema = '{{ database_schema }}'
GROUP BY table_schema, table_name
ORDER BY nullable_percentage DESC
LIMIT 20;