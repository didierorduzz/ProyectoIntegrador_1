-- ========================================
--  SETUP DE BASE DE DATOS PARA EL SISTEMA
--  Crea tablas, secuencias, triggers y datos iniciales
-- ========================================

-- Crear tablas principales
@01_create_tables.sql

-- Crear secuencias y triggers para autoincrementos
@02_create_sequences_and_triggers.sql

-- Insertar datos iniciales (usuarios, etc.)
@03_insert_initial_data.sql

PROMPT ============================================
PROMPT Base de datos lista. Tablas y datos cargados.
PROMPT Puedes cerrar SQL*Plus o iniciar Flask.
PROMPT ============================================