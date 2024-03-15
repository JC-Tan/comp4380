SELECT
  pgClass.relname   AS tableName,
  pgClass.reltuples AS rowCount,
  count(*) as column_count,
  pg_size_pretty(pg_total_relation_size(quote_ident(pgClass.relname))) tableSize
FROM
  pg_class pgClass
INNER JOIN
  pg_namespace pgNamespace ON (pgNamespace.oid = pgClass.relnamespace)
INNER JOIN
  information_schema."columns" ON (pgClass.relname = information_schema."columns".table_name)
WHERE
  pgNamespace.nspname NOT IN ('pg_catalog', 'information_schema') AND
  pgClass.relkind='r'
GROUP by tableName, tableSize, rowCount order by tableSize desc;
